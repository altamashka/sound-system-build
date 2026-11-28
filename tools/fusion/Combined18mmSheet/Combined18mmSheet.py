from pathlib import Path
import time

import adsk.cam
import adsk.core
import adsk.fusion


def build_combined_job(doc):
    """Prepare the already opened copy of the local JMOD Fab CAM archive."""
    design = adsk.fusion.Design.cast(doc.products.itemByProductType('DesignProductType'))
    cam = adsk.cam.CAM.cast(doc.products.itemByProductType('CAMProductType'))
    root = design.rootComponent
    jmod = cam.setups.itemByName('18mm Top')
    if not jmod or any(s.name == 'Classix III - 18 mm blank profiles' for s in cam.setups):
        raise RuntimeError('Open a fresh copy of the JMOD Fab CAM prep archive.')
    if not jmod.operations.itemByName('Flare Bevels - outer strips with 1 mm retaining skin'):
        raise RuntimeError('The source archive is missing the prior Fab CAM preparation.')
    if not jmod.operations.itemByName('Flare Bevels - outer final depth ONLY with hold-down').isSuppressed:
        raise RuntimeError('The JMOD final release operation should be suppressed.')

    old_stocks = jmod.stockSolids
    old_sheet = next(b for b in old_stocks if b.name == '18mm Stock')
    remaining_stocks = [b for b in old_stocks if b.name != old_sheet.name]
    if len(remaining_stocks) != 2:
        raise RuntimeError('Expected two separately indexed flare blocks.')
    origin = old_sheet.boundingBox.minPoint
    if abs(old_sheet.boundingBox.maxPoint.z - origin.z - 1.8) > 1e-6:
        raise RuntimeError('The source needs nominal 18 mm JMOD stock.')

    def collect(items):
        collection = adsk.core.ObjectCollection.create()
        for item in items:
            collection.add(item)
        return collection

    def box(feature, name, x, y, w, h):
        # Fusion model coordinates are centimetres. X is the short sheet axis.
        centre = adsk.core.Point3D.create(origin.x - 0.5 + (x + w / 2) / 10,
                                          origin.y - 0.5 + (y + h / 2) / 10,
                                          origin.z + 0.9)
        frame = adsk.core.OrientedBoundingBox3D.create(
            centre, adsk.core.Vector3D.create(1, 0, 0),
            adsk.core.Vector3D.create(0, 1, 0), w / 10, h / 10, 1.8)
        solid = adsk.fusion.TemporaryBRepManager.get().createBox(frame)
        body = root.bRepBodies.add(solid, feature)
        if not body:
            raise RuntimeError(f'Could not create {name}')
        body.name = name
        return name

    feature = root.features.baseFeatures.add()
    feature.name = '2500 × 1250 nominal sheet and Classix blanks'
    feature.startEdit()
    stock_name = box(feature, 'Combined 18 mm sheet', 0, 0, 1250, 2500)
    names = []
    for pair, y in enumerate((1529, 1818), 1):
        for label, x, width in (
            ('Side A', 15, 406), ('Side B', 437, 406),
            ('Top', 859, 180), ('Bottom', 1055, 180),
        ):
            names.append(box(feature, f'Classix {pair} {label}', x, y, width, 273))
    for pair, y in enumerate((2107, 2303), 1):
        for label, x, width, depth in (
            ('Front blank', 15, 370, 180), ('Back blank', 401, 370, 180),
            ('Brace blank', 787, 237, 180), ('Mount doubler', 1040, 180, 150),
        ):
            names.append(box(feature, f'Classix {pair} {label}', x, y, width, depth))
    feature.finishEdit()

    stock = root.bRepBodies.itemByName(stock_name)
    parts = [root.bRepBodies.itemByName(name) for name in names]
    if not stock or any(part is None for part in parts):
        raise RuntimeError('Fusion did not persist the new sheet bodies.')
    stock.isLightBulbOn = False


    # Keep the designer's flare models, tool selections and reverse stock.
    jmod.stockSolids = collect([stock, *remaining_stocks])
    setup_input = cam.setups.createInput(adsk.cam.OperationTypes.MillingOperation)
    setup_input.name = 'Classix III - 18 mm blank profiles'
    setup_input.models = parts
    setup_input.stockSolids = [stock]
    classix = cam.setups.add(setup_input)

    # Preserve the earlier archive's stock-top Z practice. The two top-side
    # jobs must use exactly the same lower-left corner on the shared sheet.
    stock_top = stock.boundingBox.maxPoint.z * 10
    expected_wcs = [(origin.x - 0.5) * 10, (origin.y - 0.5) * 10, stock_top]
    for setup in (jmod, classix):
        params = setup.parameters
        params.itemByName('wcs_orientation_mode').expression = "'modelOrientation'"
        params.itemByName('wcs_origin_mode').expression = "'stockPoint'"
        params.itemByName('wcs_origin_boxPoint').expression = "'top 1'"
        matrix = setup.workCoordinateSystem.asArray()
        actual = [matrix[i] for i in (3, 7, 11)]
        axes = [matrix[i] for i in (0, 1, 2, 4, 5, 6, 8, 9, 10)]

        if any(abs(a - b) > 1e-4 for a, b in zip(actual, expected_wcs)):
            raise RuntimeError(f'{setup.name}: unexpected datum {actual}')
        if any(abs(a - b) > 1e-6 for a, b in zip(axes, [1,0, 0, 0, 1, 0, 0, 0, 1])):
            raise RuntimeError(f'{setup.name}: work axes differ from the Fab axes')

    add_classix_profile(jmod, classix)
    generate_top_paths(cam, [jmod, classix])
    return design


def add_classix_profile(jmod, classix):
    ref = jmod.operations.itemByName('2D Contour9')
    op = classix.operations.createInput('contour2d')
    op.displayName = 'Classix outside profiles - leave 1 mm skin'
    op.tool = ref.tool
    for key, expression in (
        ('bottomHeight_mode', "'from stock top'"),
        ('bottomHeight_offset', '-17 mm'),
        ('doMultipleDepths', 'true'),
        ('maximumStepdown', 'tool_diameter / 2'),
        ('compensation', "'left'"),
        ('compensationType', "'computer'"),
        ('entry_radius', 'tool_diameter * 0.1'),
        ('entry_distance', 'tool_diameter * 0.1'),
        ('doRamp', 'true'),
    ):
        op.parameters.itemByName(key).expression = expression
    param = adsk.cam.CadContours2dParameterValue.cast(op.parameters.itemByName('contours').value)
    curves = param.getCurveSelections()
    for part in classix.models:
        selection = curves.createNewSilhouetteSelection()
        selection.inputGeometry = [part]
    param.applyCurveSelections(curves)
    classix.operations.add(op)


def generate_top_paths(cam, setups):
    operations = adsk.core.ObjectCollection.create()
    for setup in setups:
        for operation in setup.allOperations:
            if not operation.isSuppressed:
                operations.add(operation)
    future = cam.generateToolpath(operations)
    deadline = time.monotonic() + 90
    while not future.isGenerationCompleted:
        if time.monotonic() >= deadline:
            raise RuntimeError('Fusion has not completed toolpath generation.')
        adsk.doEvents()
        time.sleep(0.05)
    for operation in operations:
        if not operation.isToolpathValid or not operation.hasToolpath or operation.hasError:
            raise RuntimeError(f'Check toolpath: {operation.name}')


def save_nominal_archive(design, destination):
    manager = design.exportManager
    if destination.exists():
        raise RuntimeError(f'Choose a new export filename. Already exists: {destination}')
    options = manager.createFusionArchiveExportOptions(str(destination))
    if not manager.execute(options):
        raise RuntimeError('Fusion could not export the nominal archive.')


def run(_context):
    app = adsk.core.Application.get()
    dialog = app.userInterface.createFileDialog()
    dialog.title = 'Open JMOD 2.0 - Fab CAM prep.f3d'
    dialog.filter = 'Fusion archive (*.f3d)'
    if dialog.showOpen() != adsk.core.DialogResults.DialogOK:
        return
    source = Path(dialog.filename)
    manager = app.importManager
    doc = manager.importToNewDocument(manager.createFusionArchiveImportOptions(str(source)))
    design = build_combined_job(doc)
    destination = source.with_name('Classix III + JMOD - Fab CAM nominal.f3d')
    save_nominal_archive(design, destination)
    app.userInterface.messageBox(
        f'Saved nominal CAM to {destination}. Verify the measured stock, fixture and cutter before posting.'
    )
