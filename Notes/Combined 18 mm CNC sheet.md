# Combined Classix III and JMOD sheet

28 November 2026. Start at the [sound system build plan](../SKRAM%20%2B%20JMOD%20Build%20Plan.md).

The nominal 2500 × 1250 × 18 mm sheet fits the blanks for two Classix III kitchen cabinets and the flares for two JMODs. Use flat, uncoated BB/BB birch with a sound core. The bedroom drawer needs other stock with this layout. The JMOD's 12 mm parts have separate stock and setups.

## Rebuild the local Fusion archive

Use the saved `Exports/JMOD 2.0 - Fab CAM prep.f3d` as input. This is Ben's local working copy with the revised JMOD tabs and retaining skin. The designer's download is the starting point if that working copy is missing. The two files have different CAM settings. [JW Sound plans and licence, guide p. 23](https://www.jwsound.live/designs/jmod)

In Fusion, open **Utilities → Scripts and Add-Ins**. On the **Scripts** tab use **+** to select the [Combined18mmSheet folder](../tools/fusion/Combined18mmSheet), then select the script and choose **Run**. Pick the local Fab CAM archive. The script opens a separate Fusion document, regenerates the two top-side jobs and saves `Classix III + JMOD - Fab CAM nominal.f3d` next to the input. Keep both archives local. The script and this note are versioned here so the setup can be recreated without redistributing the adapted JMOD model.

The nominal job uses X across the 1250 mm side and Y along the 2500 mm side. Both top setups use the shared lower-left sheet corner and **Z zero at the top of the stock**. The two JMOD reverse setups still use their own block datums. The new full sheet extends 5 mm in the negative X and Y directions from the original JMOD stock corner. The Classix blank outlines begin at Y = 1529 mm from the new corner. The nearest outline is 15 mm from a sheet edge. There is a 16 mm gap between projects and a roughly 10 mm gap inside the designer's JMOD layout.

## What was checked in Fusion

The exported archive reopened with seven setups and 22 valid enabled operations. The final JMOD outer-strip release is suppressed. The Mekanika CNC router post produced six metric, one-tool test files for the combined 18 mm job. The Classix paths cover all 16 outside profiles at Z = −17 mm from the stock top, leaving a nominal 1 mm skin. The Classix front, back and brace panels are solid blanks. The test exports were checked on the computer. Fixture, machine simulation and scrap checks are pending.

Follow the first-face order in Fusion: JMOD compression cutter, JMOD ball nose, then Classix blank profiles. For the LR reverse face use the ball nose before the compression cutter. The UL reverse face uses the compression cutter. Keep the two reverse-face datums separate. The top-side outputs share a sheet origin. The posted moves get close to the split between the projects, and some reverse paths extend past the edges of their blocks. Use the measured fixture and keep screws clear of the full cutter sweep, including lead-ins. The post makes an XY move before its first Z move, so confirm the tool is already clear of stock and hold-down before starting any program.

## Check before exporting for the Fab

- Measure usable length and width, thickness, flatness and face grain. Adjust the thickness-dependent Classix blanks and check the clearance again if the sheet differs from the nominal dimensions. Confirm the machine's working Z agrees with the file, especially if the probe routine references the spoilboard. [Classix III workshop pack](https://github.com/altamashka/woodworking/blob/main/kitchen-speakers/Workshop%20pack.md#2-cut-and-label-the-panels) · [Alt Makers Fab runbook](https://github.com/altamashka/woodworking/blob/main/01%20Preparation/05%20CNC%20the%20birch%20sheet.md)
- The Classix models are blanks. Measure the actual drivers, port and terminal cup and trial the openings on scrap. Follow the workshop pack for the reinforcement, brace openings and other fitting details. Keep the kitchen parts supported through the openings and outside profiles.
- Preserve the JMOD tab and skin settings, the two joined inner-flare blocks and the upper/lower block's locating corner. Keep the saved final outer-strip release operation suppressed until the individual strips have verified hold-down. Confirm the actual compression cutter, 6.35 mm ball nose, collets and feeds. Mark the fixture and screws in the layout.
- Regenerate and simulate all affected top and reverse operations with the measured stock and workholding. Check operation order, depths, part retention and cutter, holder and dust-shoe clearance. Use the shop-approved Mekanika post in millimetres and one cutter per file, and prove the setup and flips on scrap before cutting the whole sheet. [Mekanika Fab and machine travel](https://www.mekanika.io/en/products/fab) · [Autodesk Mekanika post](https://cam.autodesk.com/hsmposts?p=mekanika)
