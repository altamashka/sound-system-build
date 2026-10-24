Working guide · v2.1 draft · 23 Oct 2026 · For collective review

# Build Guide

How to cut, assemble, wire, finish and check the JMOD and SKRAM cabinets. Version 2 splits the two builds into separate, self-contained parts so each can be printed and worked from on its own: **Part B is the JMOD**, **Part C is the SKRAM**. Shared material is in Part A (read once) and Part D (deployment and handover). **We build the JMODs first**, so start at Part B.

Companion documents: [Sound Setup Guide](Sound%20Setup%20Guide.md) (measuring, aligning, limiting and operating the rig; it starts where each build part ends) and the [SKRAM + JMOD Build Plan](SKRAM%20+%20JMOD%20Build%20Plan.md) (budget, schedule, decisions).

**Contents**

- **A · Shared basics**: A1 reading the tags · A2 licences · A3 safety · A4 materials and sheet counts · A5 tools · A6 CNC workflow
- **B · JMOD build (first)**: B1 at a glance · B2 what matters to the builder · B3 bill of materials · B4 cut list · B5 CAM review · B6 print the throat adapter · B7 parts prep · B8 dry fit · B9 assembly · B10 drivers, wiring, connectors · B11 pole mount · B12 finish · B13 test and acceptance · B14 time and build calendar · B15 open items
- **C · SKRAM build**: C1 at a glance · C2 what matters to the builder · C3 bill of materials · C4 cut list and sheet nests · C5 CAM review · C6 before assembly · C7 assembly · C8 driver and wiring · C9 hatch, vents, handles, feet · C10 finish · C11 test and acceptance · C12 time · C13 open items
- **D · Deployment and handover**: D1 JMOD stands and the sub cluster · D2 hand-over card · D3 transport and storage · D4 roles and schedule · D5 sources

**What changed from v1**

- The JMOD and SKRAM builds are separate parts with their own bill of materials, cut list, CAM review, assembly, wiring, test card and open items.
- Facts read from the design files that v1 could not read: the stock sizes both CAMs assume, the SKRAM tool and cutting data, the differences between the three SKRAM CAM files, per-part sizes and hole schedules for both designs, the throat adapter's mounting pattern.
- Resolved: the JMOD bolt count (**4 per cabinet, 8 for two**), the Speakon wiring pin assignment, the DCX464 and 12NDL88 specifications, the 21DS115 bolt circle, the SKRAM stock size.
- Catches found in the files (details in B5, B6, C4, C5): the printed adapter is 120 mm in one direction against the guide's 110 mm; the SKRAM CAM assumes 1250 mm-wide boards and mirrors the sheet when it flips it; one SKRAM outline is cut full depth in one pass; the SKRAM nests waste about five sheets of plywood across four cabinets.
- New: pole-mount design and stand checks for the JMODs (B11, D1), build calendars, expected meter readings, and the stage-by-stage route from poles to side stacks.

## A · Shared basics

### A1 How much to trust each statement

| Tag | Meaning |
| --- | --- |
| **[Guide]** | Taken from the designer's own document (the JMOD 2.02 guide, the SKRAM cut sheet and forum notes) |
| **[Model]** | Read by me from the design files: STEP geometry, DXF, the Fusion CAM documents, the SolidWorks parameter sheet |
| **[Datasheet]** | From the manufacturer's own product page (B&C, Neutrik) |
| **[Calc]** | Worked out here; the assumptions are stated |
| **[Practice]** | Standard workshop practice, not from the designers |
| **[Open]** | Not known; check before you rely on it |

I read the CAM documents, STEP and DXF files as data. I did not open them in Fusion, simulate any toolpath or cut anything. Everything about CAM below is "what the file says"; the simulation in A6 is how you prove it.

### A2 Licence and credit

- **JMOD** is licensed CC BY-NC-ND 4.0: DIY use only. Commercial manufacture, marketing and distribution are prohibited and you may not distribute modified versions. Third-party CNC or printing services are allowed if paid only for labour and materials, do not market the parts, and the product is not for resale. Our own modifications (pole mount, finish) stay private. JW's site says the plans are free for personal use and asks for donations, which fund later releases; the collective should pay one. If the rig will be hired out or the door charged, ask JW first (john@jwsound.live is the contact in the guide, page 4). [Guide, Web]
- **SKRAM** is Josh Ricci's design. The Tinker & Party files carry his note "please give credit to Josh if you're using these great subs for commercial purposes". JW Sound also hosts the plans "with permission from Josh Ricci". No formal licence is stated. [Guide, Web]

### A3 Safety

- **Dust.** Birch plywood dust is a respiratory hazard. Extraction at the machine, P2/FFP2 mask when sanding, no dry sweeping. [Practice]
- **Machinery.** Follow the makerspace's inductions and supervision rules. Never leave a running CNC unattended unless permitted; keep an extinguisher in reach; eye and hearing protection. Do not work alone with power tools. [Practice]
- **Lifting.** JMOD 34 kg, finished SKRAM about 68 kg (52 kg cabinet plus 14.7 kg driver plus hardware). Two people for a SKRAM, always; dollies. [Guide, Datasheet, Calc]
- **Adhesives, fillers, finishes.** Polyurethane adhesive and two-part fillers need ventilation, gloves and the safety data sheet; PU adhesive bonds to skin. [Practice]
- **Stands and stacks.** A JMOD on a tripod stand is a 40 kg load with its centre of gravity about 2.5 m up. See D1 for the tip-over estimate and the rules that follow from it.

### A4 Materials and sheet counts

**Sourcing update, 23 October 2026.** See [Wood sourcing review](Wood%20sourcing%20review.md) for supplier evidence and delivered-cost comparisons. Alternative Makers lists uncoated BB/BB birch, 2500 × 1250 mm: **12 mm €139.83; 18 mm €167.79** per sheet. VAT, manufacturer, birch-throughout core, glue class and availability still need confirmation. Matching BB/BB labels establish face grade, not identical core/bond quality. First JMOD pair: **€447.45**; stage 1 as supplied: **€1,733.85**; full rig as supplied: **€3,020.25**. These supersede the old Hornbach material allowance. [User-supplied portal, Calc]

**Plywood.** Birch, BB/BB faces, void-free core, bonding class suitable for the conditions. Acclimatise sheets flat in the workshop for two days. Measure the real thickness of every sheet type at six or more places with calipers and record the mean and spread. [Practice]

**Board size is a real constraint.** The two designs assume different sheets:

| Job | What the file assumes | What that means for German boards |
| --- | --- | --- |
| JMOD, all three sheets | STEP stock bodies of 1219.2 × 2438.4 mm (4 × 8 ft), 12 mm ×2 and 18 mm ×1. The CAM stock is a solid derived from the model, not a fixed size [Model] | Fits 2500 × 1250 with room, and 2500 × 1220 with 0.8 mm to spare in the narrow direction, so check the real extents of the nest in Fusion before buying 1220 boards |
| SKRAM, all seven setups | Fixed box 2500 × 1250 mm, 18 mm or 12 mm thick, model placed 10 mm in from the left and front edges [Model] | Needs 1250-wide boards. My scan of the saved toolpaths puts the nests at about 2478 × 1148 mm (18 mm sheet 1), 2308 × 1186 mm (sheet 2), and **873 × 1227 mm for the 12 mm sheet**, which does not fit a 1220-wide board with its 10 mm margin [Model, heuristic] |

The plan's Hornbach prices are for 2500 × 1220 boards. Buy 2500 × 1250 (the draft trade request already asks for that), or re-nest the 12 mm parts.

**Sheets needed (base enclosure stock; re-nests unverified).** The SKRAM nests waste plywood. 18 mm sheet 3 contains one part (the 180° turn panel F, about 490 × 584 mm) and the single 12 mm sheet is about one third used.

| Scenario | 18 mm | 12 mm | Total sheets |
| --- | --- | --- | --- |
| Stage 1 as supplied: 2 JMOD + 2 SKRAM | 1 + 6 = 7 | 2 + 2 = 4 | 11 |
| Full rig as supplied: 2 JMOD + 4 SKRAM | 1 + 12 = 13 | 2 + 4 = 6 | **19** (the plan's figure) |
| Stage 1 re-nested | 1 + 5 = 6 | 2 + 1 = 3 | 9 |
| Full rig re-nested | 1 + 9 = 10 | 2 + 2 = 4 | **14** |

"Re-nested" means sharing F-panel stock and putting the 12 mm parts of two SKRAMs on each 12 mm sheet. These are planning targets requiring regenerated, simulated CAM. Full batch optimisation saves **€783.03** at the makerspace prices (3 × 18 mm + 2 × 12 mm), giving **€2,237.22** for the rig's wood. **The 14-sheet target assumes all four SKRAMs participate.** Our conservative sequence remains: prove the first SKRAM pair with the original layouts, then optimise the second pair. That uses **12 × 18 mm + 5 × 12 mm = 17 sheets**, costing **€2,712.63**, unless a verified offcut inventory and revised nest improve it. Do not budget 14 while consuming the first pair's full eight sheets. Quantities exclude mistakes and accessories that cannot be recovered from offcuts. [Calc from existing Model findings; not simulated]


**Other portal stock.** Phenolic-coated birch is not a drop-in glue/finish substitute; maritime pine is a different material, and its 19 mm stock does not match 18 mm CAM. Keep uncoated birch for the first builds. See the sourcing review.

**Adhesives and sealants.** JMOD: a polyurethane construction adhesive, as the guide says "construction adhesive"; check pot life so the staged glue-up in B9 is not rushed. SKRAM: a waterproof PVA (D3 or D4) or PU wood glue on every dado, plus a PU or MS-polymer sealant bead at internal corners. Test any product on offcuts including a glue joint before finishing over it. [Practice]

**Fasteners, with metric equivalents.** Both designs come from US sources. The JMOD is already metric. The SKRAM's spreadsheet names 10-32 and ¼-20 inserts, which are not standard EU stock; use M5 and M6.

| Item | Hole in the design | EU tee nut / insert note |
| --- | --- | --- |
| JMOD M6 tee nuts (rear frame) | Ø7.94 mm (5/16″) [Model] | EU four-prong M6 tee nuts list a bore of 7.2–8.0 mm, so 7.94 is at the loose end; test a nut in an offcut and add a drop of epoxy if it spins [Web] |
| JMOD M5 tee nuts (inner flares) | Ø6.4 mm [Model] | EU M5 range 6.2–6.8 mm [Web] |
| JMOD hatch clearance | Ø6.4 mm (M6) [Model] | M6 socket cap, 25 mm |
| SKRAM driver baffle | 8 × Ø7.9 mm (5/16″) on Ø527 mm [Model, DXF] | Suits M6 tee nuts (Ø7.94 barrel); see C8 |
| SKRAM hatch | 18 × Ø7.14 mm (0.281″, ¼″ clearance) [Model, DXF] | Substitute M6; see C9 |
| SKRAM handles | 4 × Ø5.1 mm per handle [Model] | M5 screws |

### A5 Tools

**Portal tooling check, 23 October.** The listed €23.57 Ø3 mm cutter has **17 mm cutting length and two flutes**. It is not a direct replacement for the saved SKRAM 18 mm-flute tool for 18 mm through-cuts, nor for either JMOD ¼-inch cutter. Confirm adequate cutting length/clearance and regenerate feeds/toolpaths with the CNC operator. Sanding discs are €0.70 each; quantities and machine fees remain unknown.

| For | Items |
| --- | --- |
| CNC | JMOD: ¼″ compression bit and ¼″ ball-nose (2-flute, ball 1.4″ flute length). SKRAM: 3 mm flat end mill, long enough for 18 mm. Spoilboard, hold-down, dust extraction |
| Measuring | Calipers, steel rule, tape, framing square, straightedge ≥ 600 mm, feeler gauges, digital protractor or bevel gauge, a moisture meter if available |
| Cutting and shaping | Table saw (22.5° bevels), trim router with ¼″ roundover, random-orbit sander, files, a long sanding block (400 mm+) |
| Assembly | Many clamps (see B9 and C7), ratchet straps, 18-gauge brad nailer, drill and bits, hex keys, 10 mm spanner (the M6 flange bolts are hex AF10), rubber mallet, scrap blocks |
| Electrical | Crimp tool for the ¼″ spade and Faston terminals, soldering iron, multimeter (true-RMS), wire strippers, heat-shrink, 1.5 V cell for polarity |
| Printing | A printer with at least 120 mm in one horizontal direction (see B6) |
| Safety | Dust extraction, FFP2 masks, eye and hearing protection, gloves, first-aid kit, fire extinguisher |

### A6 CNC workflow

The makerspace's own procedure overrides these steps. [Practice]

**Before you book.**

- [ ] Someone has Fusion (free personal licence) and has opened the CAM file.
- [ ] Units, stock, zero position and tool numbers are what the makerspace's router expects.
- [ ] The post-processor matches the controller; simulate every setup and read the simulation, including the flips.
- [ ] Ask the makerspace: membership and CNC rates, supervision, which bits are stocked (¼″ compression, ¼″ ball-nose, 3 mm flat), spoilboard condition, hold-down method (screws, vacuum, tabs), dust extraction, maximum block length. I could not find public information on Alternative Makers.
- [ ] Measure your sheets (A4), compare with the CAM thickness and width, and fix the CAM (not the saw) if they differ.

**On the day.**

1. Sheet flat on a clean spoilboard, held as the makerspace requires, no screws in the toolpath.
2. Set zeros exactly as the CAM defines them.
3. **Air cut** first, with Z raised well clear, to prove path, orientation and units.
4. **Test piece** from the same sheet before the first real sheet: for SKRAM a dado-and-tongue coupon; for JMOD a section of flare and a flip-registration check.
5. Cut. Watch the first minutes. Extraction on. Stop at any odd sound or smell.
6. Remove parts, snip tabs, deburr, sand edges lightly.
7. Label every part in pencil at once: part ID, cabinet number, inside or outside.
8. Calipers on a few parts against the drawing; record.
9. Keep offcuts for clamp blocks, test coupons and spares.

---

## B · JMOD build

### B1 At a glance

| | |
| --- | --- |
| What | JW Sound's JMOD 2.02 multiple-entry horn top: two 12″ midbass drivers and a coaxial compression driver on a 3D-printed throat adapter and CNC-cut flares [Guide] |
| Size, weight | 750 W × 470 H × 420 D mm, 34 kg [Guide] |
| Coverage, range | 90° × 60° constant directivity, horizontal control to 320 Hz and vertical to 500 Hz; 80 Hz to 18.5 kHz; Fb 70 Hz, F3 55 Hz, F10 45 Hz [Guide] |
| Drivers | 2 × B&C 12NDL88 (4.95 kg each), 1 × B&C DCX464 16 Ω (3.64 kg) = 13.5 kg of drivers, so the empty shell is about 20 kg [Datasheet, Calc] |
| Plywood, two cabinets | 2 sheets 12 mm and 1 sheet 18 mm, birch [Guide] |
| CNC | Fusion CAM: 6 setups, 18 operations, ¼″ compression bit and ¼″ ball-nose, three flips [Model] |
| Printing | One throat adapter per cabinet, 169.9 × 120.0 × 90.0 mm, 438 cm³ [Model] |
| Amplification | Tri-amp (3 channels, NL8) or bi-amp through the B&C FB464 (2 channels, 4-pole). Our working assumption is the FB464 [Plan] |
| Biggest risks | CAM and flip registration; the woofer seat being flat enough to seal; the throat-adapter transition; stand stability once it is on a pole |

### B2 What matters to the builder

The horn is the acoustics; the woodwork is only the container that holds the horn shape. In practice that means:

- **Everything inside the horn must be smooth.** Steps, gaps and filler ridges where the printed adapter meets the plywood flares change the response. Guide steps 9 and 10 are not optional cosmetics. [Guide, Practice]
- **The woofer seat must be flat and airtight.** The guide says the transition where the woofer mounts "needs to be flat for the woofer to seal properly". [Guide]
- **The ports are part of the tuning.** The bandpass and reflex ports were optimised for low air speed; the ¼″ roundover on the bandpass ports is part of that, and a rough or unrounded port edge chuffs. [Guide]
- **The throat adapter has indexing geometry** at the rear to make the build repeatable. Use it. [Guide]
- **Weight and handling.** About 34 kg with an external pole cup carrying all of it. The cup mounting is structural (B11).

### B3 Bill of materials

Quantities are for **two cabinets**. "Buy" includes spares. Counts that the guide gives are marked [Guide]; I checked each against the STEP model.

| Item | Guide qty | Buy | Notes |
| --- | --- | --- | --- |
| Birch ply, 12 mm | 2 sheets | 2 | STEP stock 1219.2 × 2438.4 mm each [Model] |
| Birch ply, 18 mm | 1 sheet | 1 | Holds the flare blocks for both cabinets |
| B&C 12NDL88 | 4 | 4 | 4, 8 or 16 Ω all accepted; **8 Ω in parallel (4 Ω load) is our default**. Ø315 mm, bolt circle Ø298, cutout Ø282, depth 140, 4.95 kg; 700 W nominal / 1400 W program; Xmax 8 mm [Datasheet] |
| B&C DCX464, 16 Ω | 2 | 2 | Preferred for noise floor. Ø152 × 78 mm, 3.64 kg, four M6 holes on Ø102 mm; mid section 110 / 220 W, HF section 80 / 160 W [Datasheet] |
| B&C FB464, 16 Ω | 2 (bi-amp) | 2 | Match 16 Ω to the 16 Ω driver. **Two versions exist**: the FB464 (series filament-bulb protection) and the FB464V2 (no bulbs, higher-power inductors). See B10 and the Sound Guide §6.1 |
| Penn-Elcom H1105 recessed handle | 4 | 4 | Or Parts Express 262-821. Body about 220 × 162 × 64 mm; cutout 6¾″ × 4¼″ (171 × 108 mm) [Model, Web] |
| Penn-Elcom H1105G handle gasket | 4 | 4 | |
| M5 × 30 socket cap screws | 16 | 20 | 4 per woofer, 2 woofers per cabinet = 8 per cabinet [Guide] |
| M5 tee nuts | 16 | 20 | 4 in each left/right inner flare, Ø6.4 mm hole [Guide, Model] |
| M6 × 25 socket cap screws | 32 | 40 | Rear access panels: 2 hatches × 8 holes = 16 per cabinet [Model] |
| M6 tee nuts | 32 | 40 | 16 in each rear panel frame, Ø7.94 mm hole [Guide, Model] |
| **M6 × 16 flange bolts** | **4** | **12** | **The guide's "4" is the count for one cabinet.** Step 13 fits four per cabinet, and the throat adapter has four Ø6.6 mm holes on a Ø102 mm circle with Ø15 × 8 mm counterbores, matching the DCX464's four M6 holes. **Eight for two cabinets**, plus spares. Hex flange head (DIN 6921 type, AF10; fits the guide's 10 mm spanner) [Model, Datasheet] |
| Neutrik speakON, 2 per cabinet | 4 | 4 | NLT4MPXX (4-pole) for the FB464 route, **NL8MPRXX** for tri-amp (the NL8MPR in the guide is discontinued and replaced by the XX version). See B10 for the cutout size [Guide, Web] |
| Neutrik Faston terminals | 32 | 40 | |
| ¼″ female spade connectors | 8 | 10 | 4 per cabinet for the DCX464; 90° type or bent (guide step 12) |
| Speaker wire, internal | 2 m | 6 m | The guide's 2 m looks short for two cabinets with a network and daisy-chain. Suggest 2.5 mm² for the woofers, 1.5 mm² for the coax [Practice] |
| Wood screws 3 × 12 countersunk | 16 | 20 | |
| Wood screws 4 × 20 panhead | 40 | 50 | Handles and side fixings |
| Gasket foam | n/s | 5 m | 3–5 mm closed-cell EPDM tape for hatches and rear [Practice] |
| Construction adhesive, filler | n/s | | PU adhesive, 2-part epoxy filler; plan about 2–3 cartridges per cabinet [Practice] |
| Printer filament | ~1 kg | 1.2 kg | 438 cm³ × PETG's 1.27 g/cm³ ≈ **556 g if solid**, so the guide's "about 1 kg" assumes a near-solid print [Calc] |
| Pole-mount parts | n/s | per B11 | 35 mm pole flange, bolts, backing plate: **needed from day one** because the JMODs start on poles |

### B4 Cut list

Sizes from the STEP assembly; the 12 mm parts are flat so these are true plan sizes. The flares are angled in the assembly, so their boxes are only indicative; the CAM holds the real flat shapes. Quantities are per cabinet.

**12 mm birch**

| No. | Part | Qty | Size (mm) | Features read from the model |
| --- | --- | --- | --- | --- |
| 1 | Top / bottom panel | 2 | 420 × 749.2 | 12 × Ø7 and 4 × Ø9 holes; the bottom panel also takes the pole mount (B11) |
| 2 | Rear panel frame | 1 | 455 × 733 | **16 × Ø7.94 (M6 tee nuts)**, 4 × Ø7, Speakon half-cutouts Ø32.5 |
| 3 | Side panel | 2 | 420 × 456 | 4 × Ø7, 4 × Ø24 |
| 6 | Access panel | 2 | 322 × 443.5 | 8 × Ø6.4 each (M6 clearance) |
| 8 | Handle brace | 2 | 364.6 × 445 | 4 × Ø7; handle cut-outs |
| 9 | L brace | 1 | 107 × 107 | |
| 10 | D brace | 2 | 137.4 × 220 | |
| 11 | Rear spine | 1 | 75 × 455 | Speakon half-cutouts Ø32.5 |

**18 mm birch** (3D parts, cut from two shared blocks)

| No. | Part | Qty | Assembled box (mm) | Where it is cut |
| --- | --- | --- | --- | --- |
| 4 | Upper / lower outer flare | 2 | 55.6 × 68 × 724 | "UL" blocks |
| 5 | Left / right outer flare | 2 | 59.3 × 110 × 456 | 22.5° bevel on the long edges (table saw) |
| 12 | Upper / lower inner flare | 2 | 130.6 × 215 × 504 | "UL flare stock" 524 × 740 mm holds all four for two cabinets; flipped for the throat-adapter flanges |
| 13 | Left / right inner flare | 2 | 226 × 227 × 456 | "LR flare stock" 642.7 × 918.4 mm holds all four for two cabinets; flipped for the cone-recess contours; 4 × Ø6.4 tee-nut holes each |
| 7 | Throat adapter | 1 | 169.9 × 120 × 90 | Printed (B6) |

**Utilisation.** Counting boxes, one cabinet's 12 mm parts are about 2.06 m², so two cabinets use about 70% of two sheets: this nest is already efficient. [Calc]

### B5 CAM review

**What the file contains.** `JMOD 2.0 Fusion.f3d` was saved by Fusion CAM 2602.1.25 (Feb 2026). It holds six setups. Stock is a solid taken from the model, so the nest, not a fixed sheet size, defines what must fit. [Model]

| Setup | Operations | Notes |
| --- | --- | --- |
| 18mm Top | Mark holes · 2D Contour8 · 2D Pocket10 · UL Bevel Roughing · 2D Contour9 · Flare Bevels | Ball-nose "Flare Bevels" machine the bevels on the upper/lower flares (the table saw does only the left/right outer flares) |
| 12mm Sheet 1 Top | 2D Contour10 · 2D Pocket11 · 2D Contour10 (2) | |
| 12mm Sheet 2 Top | Mark Holes · 2D Contour11 · 2D Pocket5 | |
| Handle Recess Bottom | 2D Pocket6 · 2D Contour6 | **Flipped (Z)** |
| LR Flares Bottom | Contour4 (3D, ball-nose) · 2D Contour12 | **Flipped (Z)**: cone-recess contours on the left/right inner flares |
| UL Flares Bottom | 2D Pocket7 · 2D Contour14 | **Flipped (Z)**: throat-adapter mounting flanges on the upper/lower inner flares |

**Tools and settings saved in the file.** The 2D operations run a **¼″ 2-flute compression bit** (1″ flute) at **16,000 rpm**, 4000 mm/min cutting, 80 in/min (2032 mm/min) plunge, 4 mm steps for contours and about 0.64 mm steps for most pockets. The 3D finishing uses a **¼″ ball-nose** (1.4″ flute) at **19,000 rpm**: "Flare Bevels" 4000 mm/min with 1.0 mm steps; "Contour4" 70 in/min (1778 mm/min) with 0.8 mm steps. Tool diameters are in inches in the file, so check your post outputs metric correctly and the tool numbers match your carousel or tool table. [Model]

**Review checklist.**

- [ ] Open in Fusion; simulate all six setups; read every flip. Confirm the stock on screen is the sheet you bought.
- [ ] Check what "Mark holes" and "Mark Holes" do. I could not tell from the file whether they cut finished holes or only mark centres. If they only mark, drill the tee-nut holes by hand to the sizes in B4 (Ø7.94, Ø6.4, Ø6.4).
- [ ] The nest is built on a 4 × 8 ft stock. On a 1220-wide board there is 0.8 mm to spare in the narrow direction; confirm the real nest width before buying 1220 boards, or buy 1250.
- [ ] Ball-nose depths depend on real sheet thickness and on the flip registration. Measure the birch, add registration (dowels or screws in the waste, as the guide's "extra stock on the bottom corner" for the UL flares suggests), and cut a test flare first.
- [ ] I did not check whether tabs are enabled in the 2D contours.
- [ ] Ask JW for the `.dwg` cutlist the changelog says was added in v1.1; it is not in our package. [Guide]

**Machine time.** The files carry no time estimates; ask the makerspace to run the simulation's estimate. Plan the JMOD pair as one block and the first cut as a learning cut. [Open]

### B6 Print the throat adapter

- **Size.** The supplied STL measures **169.9 × 120.0 × 90.0 mm** and 438.2 cm³. The guide states a minimum build volume of 170 × 110 × 90 mm, but as supplied the part needs 120 mm in the second direction. Our Prusa Core Ones (250 × 220 × 270) fit it in any orientation; for a smaller printer, rotate and check. [Model]
- **Material.** The guide rates PETG-CF, PETG-GF, plain PETG, PCTG and some others "good", ASA and ABS "acceptable", and PLA, TPU and PVB "avoid". Plain PETG or PCTG print on a standard nozzle. A dark cabinet in direct sun can push its inside toward PETG's glass transition (about 75–80 °C), so for summer festivals PETG-CF, PCTG or ASA is the safer choice. [Guide, Practice]
- **Settings.** The guide gives none. Start from a near-solid print: 100% infill, or at least 6 perimeters with 80% infill; 0.2 mm layers; 0.4 mm nozzle. At 556 g each in solid PETG the plan's 45–50 machine hours for the pair stands. [Calc, Practice]
- **Orientation.** The DCX464 seat is the flat face with four Ø6.6 mm holes; print so that face is as flat and clean as possible. Print one cheap, low-infill test in the planned orientation first to check overhangs and warping. [Practice]
- **The mounting pattern.** Four Ø6.6 mm clearance holes on a Ø102 mm circle (at 0°, 90°, 180°, 270°) with Ø15 mm counterbores, 8 mm deep. The M6 flange bolts go through the adapter and thread into the driver's own M6 holes. The adapter also carries Ø4 mm, Ø8 mm, Ø10 mm and Ø6.8 mm features that the guide does not describe (probably indexing and fixing); use the guide's photographs and the model. [Model]
- **Check each print:** warping on the seat face (straightedge and feeler gauge, ≤ 0.2 mm), layer adhesion, hole positions with calipers, then **dry-fit the DCX464 on it** and check all four bolts start by hand.
- **Before gluing**, scuff the faces that take adhesive with 120-grit; PETG is a poor glue surface otherwise. [Practice]

### B7 Parts prep

1. **Bevels.** Table saw, 22.5° on the long edges of the left/right outer flares. Test the angle and the direction on an offcut and dry-fit one flare before cutting the others. [Guide, Practice]
2. **Tee nuts.** Press 16 × M6 into each rear panel frame (Ø7.94 holes) and 4 × M5 into each left/right inner flare (Ø6.4 holes). Press with a clamp rather than hammering so the prongs seat evenly; check each flange sits flush. If a nut spins, a drop of epoxy on the barrel fixes it. The M6 hole is at the loose end of the EU range, so test a nut first (A4). [Guide, Practice]
3. **Roundover.** ¼″ (6.35 mm) roundover bit on the inside of the woofer bandpass ports, marked red in the guide, while the port edge is accessible. Test on an offcut first. [Guide]
4. **Hole check.** Verify the handle cut-outs, Speakon cut-outs and screw holes against the real hardware before assembly.

### B8 Dry fit

Dry-assemble the whole cabinet with clamps and no glue; photograph every step. The guide says "some areas may require hand sanding". Check in particular that the flares seat on the adapter's indexing geometry, and that no gap exceeds about 0.5 mm anywhere inside the horn. Mark each edge you sand. [Guide, Practice]

### B9 Assembly

Follow the guide's 16 steps in order. What I add is the check at each stage. Build both cabinets in parallel only if you have clamps for both; otherwise finish one completely and use its lessons. [Guide, Practice]

| Step | Guide's instruction | Add this |
| --- | --- | --- |
| 1 | Rear panel frame and side panels onto the bottom panel; clamp across the rear | Check both rear corners with a framing square; frame flush to the rear edges |
| 2 | Construction adhesive on the left/right faces of the adapter | Scuffed faces; a continuous bead; wipe squeeze-out out of the throat immediately |
| 3 | Adhesive, then left/right inner and outer flares and the top panel | A helper holds the flares; check the flare ends against the adapter's indexing geometry before the top goes on |
| 4 | Clamp all sides, no gaps | At least eight clamps; check every seam with a light behind it; do not over-clamp and crush the flares |
| 5 | Stand on its back; glue in the inner upper/lower flares | Adhesive on the flat that meets the adapter and on the flare sides |
| 6 | Glue in the outer upper/lower panels; slide to minimise gaps; brad-nail at the marked points | 18-gauge brads, long enough to bite but not break through a flare surface; test on an offcut |
| 7 | Face down: glue and clamp the handle braces and rear spine | |
| 8 | Glue and clamp the D braces and L brace; brad-nail the L brace; stack scrap so clamps reach | |
| 9 | Filler where needed between adapter and inner flare at the woofer seat | **Seat test:** straightedge across the seat in four directions, feeler gauge; ≤ 0.5 mm total unevenness and no step. Two-part epoxy filler, long sanding block |
| 10 | Fill and sand panel gaps in the horn; blend the adapter into the flats | 80 → 120 → 180 grit; vacuum and tack-wipe; seal the filler |
| 11 | Face down; fit handles and rear gasket | Handle cut-out 171 × 108 mm; H1105G gasket under the handle |
| 12 | Leads on the DCX464 with female spade connectors, 90° or bent | Clearance to the back is tight; dry-fit the bend before crimping |
| 13 | Seat the DCX464 on the adapter and fit **four M6 × 16 flange bolts** | Four, per cabinet. Snug and even in a cross pattern, do not overtighten the printed seat; check for an air leak at the seat afterwards (B13) |
| 14 | 12″ woofers, 4 × M5 × 30 each | B&C lists "flange and gasket thickness 13 mm"; confirm a gasket is fitted, else add foam tape |
| 15 | Wire the drivers, fit the Speakon connectors | See B10 |
| 16 | Rear access panels with M6 × 25; side handles with 4 mm wood screws | 8 screws per hatch; foam gasket under each hatch |

### B10 Drivers, wiring and connectors

**Speakon cutouts.** The STEP has two **Ø32.5 mm** connector cut-outs (each half in the rear frame, half in the spine). Neutrik's drawing gives about Ø31 mm for the 8-pole G-size flange (NL8MPR / NL8MPRXX), so the holes suit the tri-amp connector. A 4-pole D-size flange (the NL4MP family) uses a D-shaped cutout about 24 mm round with 19 mm flats, plus two screw holes, and would not cover a 32.5 mm hole; one retailer lists the NLT4MPXX as G-type, which may or may not share the larger cutout. **Before cutting the cabinet, check the real connector against the cut-out**; if it is smaller, make two small face plates. [Model, Web, Open]

**Pin assignments.** I traced the guide's page 21 and 22 diagrams.

| Route | Connector | Pins | Goes to |
| --- | --- | --- | --- |
| **Bi-amp (FB464)** | NLT4MPXX ×2 per cabinet, wired in parallel for daisy-chaining | 1+ / 1− | Both 12NDL88 in parallel |
| | | 2+ / 2− | FB464 **IN+ / IN−** |
| | FB464 outputs | W+ / W− | DCX464 **mid (outer ring)** |
| | | T+ / T− | DCX464 **HF (inner dome)** |
| **Tri-amp** | NL8MPR(XX) ×2 per cabinet | 1+ / 1− | Both 12NDL88 in parallel |
| | | 2+ / 2− | DCX464 **mid (outer ring)** |
| | | 3+ / 3− | DCX464 **HF (inner dome)** |
| | | 4+ / 4− | Not used; left empty or passed through |

[Guide, Model: read from the wiring diagrams]

**Wiring rules.** Both woofers are wired in parallel. Use polarity-marked wire; ring the polarity out with the 1.5 V cell. Strain-relieve every lead. Keep wires clear of the cones and of the FB464's bulbs. Daisy-chaining a second JMOD on the second receptacle halves the impedance at the amp, so recompute the load first. [Guide, Practice]

**The FB464.** About 100 × 110 mm, 0.36 kg. B&C describes 3.6 kHz, 18/12 dB per octave, phase-aligned, and no power rating; the standard FB464 gets its protection from series filament bulbs. The V2 has higher-power inductors and no bulbs. B&C pairs it with the **ME464 300 Hz horn**, which is not the JMOD's horn, so expect the combined response to need measuring (Sound Guide §6.1). The guide does not say where to mount it; mount it on the inside face of one access panel so it can be serviced, clear of the foam gasket. [Datasheet, Practice, Open]

### B11 Pole mount

The JMODs start on poles, so this is part of the build, not an accessory. The guide recommends an **external** pole-mount cup because the inside is tight, placed **245 mm from the front lip** with 12NDL88 woofers (the centre of mass), centred left to right (375 mm from either side). [Guide]

**What the part must be.**

- A steel 35 mm pole socket (flange or cup) with a locking screw or ring lock.
- Rated well above the load: the cabinet is 34 kg; use a part rated at least 50 kg and ideally 100 kg static.
- Fixed with through-bolts and large washers into a **backing plate**, never into the 12 mm panel alone. [Practice]

**Candidates found, none confirmed for our use.** Adam Hall SM 700 (steel 35 mm flange; no load rating listed) · K&M 195/8 slip-on adapter (steel, 50 kg per one retailer) · RCF AC-TT-PMA (steel 35 mm cup, 50 kg / 110 lb per the retailer) · Gravity GSF36M10M and Adam Hall SPS 36 M10 (35 mm pole to M10 thread adapters; no load rating listed). **Ask the maker for the rated load of whichever part you pick.** [Web, Open]

**Suggested construction.** Glue and screw an 18 mm birch **skid plate**, about 300 × 300 mm, to the underside of the bottom panel, centred on the pole position, then through-bolt the flange to the plate. This spreads the load, gives the screws real wood to bite, and doubles as a stable foot when the cabinet stands on the ground. Check from the model which interior area under the bottom panel is clear (the bottom D brace and the port routes are there) before choosing bolt positions. [Practice, Open]

**Aiming.** The pattern is 90° × 60°; the guide advises getting the tops as high as reasonable and angling them down. A tilt adapter or a wedged skid plate gives the down-tilt; plan 5–10° and verify by measurement. [Guide, Practice]

### B12 Finish

- Fill and sand until the horn surface is smooth and free of ridges (B9 step 10); seal filler before painting.
- Seal end grain and every face; unsealed plywood takes up moisture.
- A tough polyurethane or textured coating survives touring. Test the product on an offcut including a glued joint.
- **Mask** before coating: gasket faces, the woofer seats, the DCX464 seat, tee nuts, connector faces, the inside of the Speakon holes.
- Keep paint out of the adapter's counterbores and the flat driver seat; a paint ridge breaks the seal.
- Label: cabinet ID, impedance, pinout, weight, on the outside and on the inside of a hatch. [Practice]

### B13 Test and acceptance

Do these with the access panels still off.

- [ ] **DC resistance** across each pair of pins, recorded and compared with the sibling cabinet. Expect: two 12NDL88 (8 Ω type, Re 5 Ω each) in parallel **about 2.5 Ω** at the NL4 or NL8. The coax and FB464 reading depends on the network and I have no figure; **record yours as the reference** and require the second cabinet to match within a few percent. [Datasheet, Calc, Open]
- [ ] **Polarity of each woofer** with the 1.5 V cell, positive to "+": the cone moves out.
- [ ] **FB464 wiring** against its W, T and IN markings; the 16 Ω network on the 16 Ω driver.
- [ ] **No loose wire** near the cones; strain relief on every connector.
- [ ] **Seals.** Hatches seal with their gaskets; no audible air leak at the woofer seats or the DCX464 seat with a low-level sine through each driver (leaks whistle or hiss).
- [ ] **Weight** recorded. Photos taken. Then close the hatches and go to §5 of the Sound Guide.

### B14 Time and build calendar

I have no measured JMOD build time. Treat the first cabinet as a learning build and log hours. A reasonable calendar for the pair, with two or three people (my plan, not a measurement):

| Day | Work |
| --- | --- |
| 0 | Start the throat-adapter prints (each about 22–25 h); order parts; measure plywood |
| 1 | CAM review in Fusion; test flare on the CNC |
| 2–3 | CNC block: all six setups, both cabinets; label parts |
| 4 | Table saw bevels; tee nuts; roundovers; dry fit; photograph |
| 5 | Staged glue-up, steps 1–6 (adhesive pot life in mind) |
| 6 | Steps 7–8; start filler |
| 7 | Filler and sanding (steps 9 and 10); seat test |
| 8 | Seal, prime, paint, mask |
| 9 | Handles, gaskets, drivers, wiring (B10); skid plate and pole flange |
| 10 | Test (B13); then the Sound Guide |

### B15 Open items (JMOD)

| Open item | How to close it |
| --- | --- |
| Whether the CAM runs on the makerspace's router and post | Simulate; ask for a test run |
| What "Mark holes" does | Fusion simulation |
| Throat-adapter print orientation and settings | Test print; ask JW |
| NLT4MPXX versus the Ø32.5 mm cut-outs | Dry-fit the real connector |
| FB464 mounting position | Decide at dry fit |
| Pole flange rating, bolt pattern and skid-plate layout | Maker's datasheet; check the model |
| Hire or door-charge use of the JMODs | Ask JW |
| Time per cabinet | Log the first build |

---

## C · SKRAM build

### C1 At a glance

| | |
| --- | --- |
| What | Josh Ricci's single-21″ vented subwoofer; four vents give four tunings [Guide] |
| Size, weight | 610 W × 914 H × 813 D mm (24″ × 36″ × 32″). Cabinet 52 kg projected, driver 14.7 kg (21DS115) [Guide, Datasheet]; about 68 kg finished [Calc] |
| Tuning | All vents open 29.5 Hz · three 25.5 Hz · two 20.5 Hz · one 14.5 Hz. Ricci says it is optimised for the 29.5 and 25.5 Hz tunings; the lower ones lose output and vent area [Guide, Web] |
| Driver | B&C 21DS115, **8 Ω**: 1700 W AES / 3400 W program, Xmax 16.5 mm, Ø547 mm, bolt circle Ø527 mm, cutout Ø508 mm, depth 255 mm [Datasheet] |
| Plywood per cabinet | 3 sheets 18 mm + 1 sheet 12 mm as supplied (about 2.25 + 0.5 re-nested, see A4) |
| Parts | 20 part types (A to T), 20 pieces of 18 mm and 21 of 12 mm [Guide] |
| CNC | Flat 2D, 7 setups (one 12 mm, three 18 mm sheets each cut from both faces), one 3 mm cutter [Model] |
| Joinery | Dado and rabbet "egg-crate"; no step-by-step assembly instructions are published |
| Biggest risks | Thickness error compounding through every dado; the sheet flip; a leaking hatch or driver seat; lifting |

### C2 What matters to the builder

- **The designer says the plans are a chassis guideline.** "The simplified layout drawing is really all that should be adhered to." Bracing, hatch and hardware may be simplified "just make sure it is solid". Outer dimensions can be adjusted "within reason". [Guide]
- **The internals are the acoustics.** The driver fires into an internal baffle (6° in the layout), then through folded chambers to the mouth; the vents tune the vented chamber. Everything between the driver and the vents must be sealed. [Guide, Model]
- **Weight.** 52 kg of cabinet is plywood; the sheets are heavy before they are cut. Do not plan to move a finished SKRAM with fewer than two people. [Guide]
- **Topology note.** Ricci calls it a single-driver sub "similar in design to the Skhorn". A diyAudio forum reply describes SKRAMs as 6th-order bandpass variants that are only slightly horn-loaded. This does not change the build, but it is why the Sound Guide treats the subsonic filter with care. [Guide, Web]

### C3 Bill of materials, per cabinet

| Item | Qty | Notes |
| --- | --- | --- |
| Birch ply 18 mm | 3 sheets as supplied | Batch re-nest: 5 per pair or 9 for four, not 2 per cabinet; see A4 |
| Birch ply 12 mm | 1 sheet (0.5 re-nested) | |
| B&C 21DS115, 8 Ω | 1 | One model and one impedance across all four cabinets. 8 Ω lets two share a channel later |
| Driver fasteners | 8 | Holes on a Ø527 mm circle at 45° pitch; hole size per B&C's drawing (see C8) |
| Hatch fasteners | 18 | ¼-20 in the original; **use M6** with threaded inserts or tee nuts; hatch holes Ø7.14 mm [Model] |
| Speakon, 4-pole | 1 | Original cut-out is for an NL4-MPR in a Ø25.4 mm (1″) hole [Guide, Model] |
| Handles, Penn-Elcom H1105 or Parts Express 262-821 | up to 6 | Optional per Ricci: one on each side panel, two on the top, two on the hatch; cut-outs are in the model. **Penn-Elcom publishes no rating for the H1105**: ask them, or treat a 68 kg cabinet as needing all four side and top handles in use [Model, Web] |
| Handle screws | 4 per handle | Ø5.1 mm holes, M5 |
| Port blocks | 3 | One single (blocks the left or right vent), one double (the middle two), one triple; 18 mm ply is my suggestion; thickness is not stated. Pilot holes in the DXFs: 8, 13 and 18 [Model, Open] |
| Hatch gasket, port-block gaskets | | Closed-cell foam strip [Practice] |
| Feet or skid, castors | | The SolidWorks assembly has "Side Rail", "Feet Rail" and a "PE 15.51 Skid"; decide what to build (C9) [Model, Open] |
| Internal wire | ~2 m of 4 mm² | Driver is 1700 W; keep the run short [Practice] |
| Wood glue, sealant, finish | | A4, C10 |

### C4 Cut list and sheet nests

Sizes from the cut sheet; thickness 18 mm unless noted.

| ID | Part | Qty | Size (mm) | | ID | Part | Qty | Size (mm) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| A | Side panel (one mirrored) | 2 | 813 × 914 | | J | Baffle brace (12) | 2 | 612 × 125 |
| B | Top / bottom | 2 | 584 × 813 | | K | Turn cap | 1 | 584 × 269 |
| C | Front | 1 | 547 × 584 | | L | Main brace | 1 | 735 × 584 |
| D | Back | 1 | 888 × 584 | | M | Top brace (12) | 2 | 528 × 135 |
| E | Hatch | 1 | 585 × 546 | | N | Top corner brace (12) | 2 | 251 × 169 |
| F | 180° turn panel | 1 | 489 × 584 | | O | Large hatch brace | 2 | 549 × 57 |
| G | Driver baffle | 1 | 625 × 584 | | P | Hatch brace | 4 | 146 × 57 |
| H | Vent panel | 1 | 660 × 584 | | Q | Middle hatch brace | 2 | 179 × 57 |
| I | Vent divider (12) | 3 | 791 × 145 | | R | Mouth brace (12) | 2 | 612 × 187 |
| | | | | | S | Baffle brace (12) | 6 | 251 × 55 |
| | | | | | T | Back brace (12) | 4 | 251 × 36 |

**How the CAM nests them** (from the part names in the nested STEP files and the saved toolpaths):

| Sheet | Parts | Parts area | Utilisation |
| --- | --- | --- | --- |
| 18 mm sheet 1 | A × 2 (one mirrored), E, G, K, O × 2, P × 4, Q × 2 (and two small rails the CAM files carry) | about 2.4 m² of 3.1 | about 78% |
| 18 mm sheet 2 | B × 2, C, D, H, L | about 2.6 m² | about 83% |
| **18 mm sheet 3** | **F only** | about 0.29 m² | **about 9%** |
| 12 mm sheet | I × 3, J × 2, M × 2, N × 2, R × 2, S × 6, T × 4 | about 1.07 m² | **about 34%** |

[Model, Calc]

### C5 CAM review

**Three CAM files, compared.** All three have the same seven setups and the same operations. [Model]

| File | Saved by | Status | What differs |
| --- | --- | --- | --- |
| `SKRAM PARALEL CAM.f3d` (Mar 2024) | Fusion CAM 2.0.18477 | Toolpaths valid | Ramp angle written as a literal 2.0°; outline selection syntax differs; 12 mm outline `side` = start-inside |
| `SKRAM PARALLEL CAM.f3d` (May 2026) | Fusion CAM 2702.1.58 | **All 12 toolpaths flagged invalid** (not regenerated) | Same parameters as June except the 12 mm outline |
| `SKRAM PARALEL CAM 2026_06.f3d` (Jun 2026) | Fusion CAM 2702.1.58 | Toolpaths valid | 12 mm outline `side` changed to start-outside and one face-selection flag cleared |

**Use the June 2026 file**, and still simulate it. The substantive change from May is only the 12 mm outline's `side` setting; the May file is the same job with stale toolpaths. [Model]

**What the file says.**

- **Stock:** fixed box **2500 × 1250 mm**, 18 mm (12 mm for the 12 mm setup), placed 10 mm from the left and front edges. User parameters in the file: `holz` = 18 mm, `braces` = 12 mm, `pockets` = 5 mm (the tongue length).
- **Tool:** one **3 mm flat end mill**, 18 mm flute length, 5,000 rpm, 1,000 mm/min cutting, plunge at one third of that, ramp entry (2°). The file's flute count (4) is a default; check what your bit really is. Coolant is set to "flood"; switch it off for a router.
- **Contours:** 5 mm steps down (a 0.2 mm finishing step is listed); compensation left; lead-in and lead-out.
- **Pockets (the dados and recesses):** stepover 0.6 × the tool (1.8 mm) and 0.5 mm stock to leave.
- **Bores:** helical, climb.
- **Order:** each 18 mm sheet is cut as a "downside" setup (pockets on the underside) and an "upside" setup (bores, pockets, outline). The outline is cut in the upside setup so the parts stay held until the end.
- **Machine time:** my rough scan of the saved toolpaths gives about 175 m of cutting moves for one cabinet, about 3 hours at 1,000 mm/min before setup, plunges and flips. Treat as ±50%. [Model, Calc, heuristic]

**Catches found. Check each before the first sheet.**

1. **Board width.** The stock is 1250 mm wide and the 12 mm nest alone is about 1227 mm. A 1220 board does not work (A4).
2. **The flip and the sheet width.** The three "downside" setups use a flipped Y axis from the same corner. The mirror line therefore depends on the stock width in the file (1250 mm). **If your real sheet is 1220 mm, the underside pockets land 30 mm off the topside outlines.** Set the stock Y in all seven setups to your measured sheet width and regenerate, or add dowel registration. [Model, Calc]
3. **Z zero is at the stock bottom (the spoilboard).** Recess depths therefore follow the sheet's top, so a sheet thinner than 18.0 mm makes every dado shallower by the difference. Measure (A4) and set `holz` and the stock Z to the measured value. [Model]
4. **One outline is cut in one pass.** Sheet 2's outline (operation 2D-Kontur3) has multiple depths switched off, and the saved toolpath has only two Z levels, so it cuts 18 mm deep in a single pass with a 3 mm cutter, while the other outlines step down 5 mm. The pockets on sheets 1 and 2 (2D-Tasche5, 6, 7, 8) have the same flag off. **Switch multiple depths on (about 5 mm steps for the outline, a small step for pockets) before running them**, or match them to the sheet-3 operations that do step. [Model]
5. **Hardware holes are missing from the STEP parts.** The 8 driver-mounting holes, the 18 hatch holes and all the 3 mm screw pilot holes are in the 2019 DXFs but not in the STEP part files, so they are probably not in the CAM either. Add them or drill them from a template. [Model]
6. **Imperial heritage.** The DXFs are in **inches**. The CAM's own metric parameters are the reliable ones; do not mix.
7. **Inside corners are R1.5 mm** from the 3 mm cutter. The model's `Bit Diameter` and `Dado Fit` parameters indicate the dados already allow for this, but check a tongue in a dado on a test coupon.
8. **Tabs.** Tab settings are defined (3 mm wide, 0.75 mm high, 24 mm pitch) but I could not confirm that tabs are enabled.

### C6 Before assembly

- [ ] Dry-fit the whole cabinet with straps, no glue. Photograph it.
- [ ] Number the joints. Check every dado, tongue and rabbet. File or sand; never force a joint.
- [ ] Drill and fit the hardware you can no longer reach once it is closed: the baffle's 8 driver holes with tee nuts from the far face, the hatch inserts or tee nuts, handle screw holes.
- [ ] Sand and seal the inside faces before assembly where practical.
- [ ] Decide the sealant. Plan to glue every joint, plus a bead of sealant in internal corners and at every junction in the airway.
- [ ] Prepare the hatch assembly (E with its O, P, Q braces) separately.

### C7 Assembly

**Proposed sequence** (mine; the cut sheet has dimensioned parts, an internal overview, a basic layout and two exploded views, but no steps). It must be proved by a dry fit. [Practice]

1. Lay one side panel flat, dados up, on a clean, flat bench.
2. Add the internal parts in the order the dry fit proves, starting with the ones that hold the rest: the bottom, the vent panel, the vent dividers and the mouth braces; then the turn panel, the **driver baffle (6° in the layout)** and the turn cap; then the main brace and the smaller braces. Glue each joint as you go and wipe squeeze-out.
3. Lower the second side panel onto the tongues. Tap it home. **Measure both diagonals** to confirm squareness before the glue sets.
4. Strap or clamp the whole cabinet. Add the top and the back with their braces.
5. Leave the hatch off. Build the hatch assembly separately (E plus O, P, Q braces), with the handle and Speakon cut-outs, and fit the gasket.
6. Cure fully (24 h for PVA) before moving it.

Write down the final sequence so the later cabinets repeat it. **Clamps and straps:** at least eight clamps plus four ratchet straps; 52 kg of plywood is hard to hold square by hand. [Practice]

### C8 Driver and wiring

- **Driver.** 21DS115 (8 Ω): Fs 34 Hz, Qts 0.27, Xmax 16.5 mm, Re 5.1 Ω, 14.7 kg, flange Ø547 mm, bolt circle Ø527 mm, baffle cutout Ø508 mm, depth 255 mm. [Datasheet]
- **Mounting.** Ricci's DXF baffle carries 8 holes of Ø7.9 mm (5/16″) on a Ø527 mm circle at 45° spacing, the same circle B&C publishes, which suits M6 tee nuts (Ø7.94 barrel). B&C's page does not give the number or diameter of the driver's own holes: **take them from B&C's drawing, or use the driver as a template, before drilling.** [Model, Datasheet, Open]
- **Install** from inside through the hatch opening, on a gasket or sealing tape; tighten in a cross pattern. Never lift the driver by the cone or the terminals. [Practice]
- **Wiring.** Speakon pins 1+ / 1− for the 4-pole connector; mark polarity. Keep the run short, strain-relieved, away from the cone. [Practice]
- **Expected readings.** DC resistance about 5.1 Ω for the 8 Ω driver (4.6–5.6 Ω at the connector). Polarity: 1.5 V cell, positive to "+", cone moves out. [Datasheet, Calc]

### C9 Hatch, vents, handles, feet

- **Hatch.** 18 fasteners around the hatch perimeter, 18 × Ø7.14 mm holes in the DXF, plus the Speakon cut-out. Fit the gasket and tighten in a cross pattern; a leaking hatch is the commonest source of noise and lost output. Which part carries the inserts is not stated in the files; read it from the SolidWorks model. [Model, Open]
- **Port blocks.** Make a single, a double and a triple per cabinet. Their DXFs are about 155 × 152, 305 × 152 and 449 × 152 mm with 8, 13 and 18 pilot holes. Add a gasket so they seal, and label them. [Model]
- **Tuning is a deployment choice.** Blocks change the tuning without any rebuild (all open 29.5 Hz, three 25.5, two 20.5, one 14.5). [Guide]
- **Handles.** Cut-outs and Ø5.1 mm screw holes are in the model for H1105 handles. [Model]
- **Feet and castors.** The model includes rails and a skid. Decide what you want: four heavy-duty castors with brakes (≥ 100 kg each) or skid rails. A centre cluster of four sits on the floor in a row, so castors matter for loading, not use. [Open]

### C10 Finish

- Fill voids and edges, sand through the grits, a half-inch roundover on the outside corners is optional per Ricci and helps durability and handling. Seal end grain and all faces.
- A tough polyurethane or textured coating survives touring. Test on an offcut including a glued joint.
- Mask: gasket faces, driver seat, inserts, Speakon holes, port-block seats.
- Protect: corner protectors, rubbing strip on the bottom edge.
- Label: ID, impedance, pinout, weight, tuning chart on the hatch. [Practice]

### C11 Test and acceptance

- [ ] Weight recorded (expect about 66–70 kg).
- [ ] DC resistance recorded; polarity checked.
- [ ] **Seal check.** Slow low-level sweeps with the vents open, then with them blocked; listen and feel at the hatch and driver seat for leaks.
- [ ] No rattles; handles and feet solid.
- [ ] Vent blocks fit and seal.
- [ ] Cabinet ID inside and outside. Then the Sound Guide §5 and §8.5, which measures all four tunings.

### C12 Time

A forum poster put the effort at roughly 25 hours for experienced builders and over 60 for people without tools. That is one person's guess, not a measurement. Plan the first cabinet as a learning build and time it. [Web, Open]

### C13 Open items (SKRAM)

| Open item | How to close it |
| --- | --- |
| Whether the makerspace can run the 3 mm cutter long enough and at these settings | Simulate; ask for a test run on offcut |
| The sheet width and thickness to put in the CAM | Measure the boards you buy |
| Hardware holes missing from the CAM | Add from the DXFs or template |
| B&C 21DS115 mounting hole size and count | B&C drawing |
| Hatch-insert part, port-block thickness, feet arrangement | SolidWorks model |
| Rating of Penn-Elcom H1105 | Ask Penn-Elcom |
| Re-nest of the F panels and the 12 mm sheet | After proving the first pair; use the 17-sheet staged budget unless verified offcut reuse improves it |
| Time per cabinet | Time the first build |

---

## D · Deployment and handover

### D1 JMOD stands and the sub cluster

**Working layout (decided).** Sub cluster in the centre, JMODs on poles to the left and right. This is Arrangement C in the Plan: the subs behave as one source, the tops get a per-side delay (Sound Guide §10), and nothing needs lifting above the floor except the JMODs on their stands. Later, side stacks of SKRAM, SKHORN or similar can replace the poles (the Plan, §08).

**Stands.** The stand rating is not a marketing figure to take on trust.

| Stand | Rating (retailer) | Height | Note |
| --- | --- | --- | --- |
| K&M 21435, steel tripod | 50 kg | 1430–2240 mm | 5.9 kg. The best candidate found |
| K&M 21436, aluminium tripod | 40 kg | 1430–2240 mm | Too thin a margin for a 34 kg cabinet |
| K&M 21459 (pair of 21450) | 50 kg per stand | 1270–1930 mm | Lower height |

Retailers list these inconsistently; confirm with K&M before buying. Tripod stands with 35 mm poles marketed at "132 lb" are marketing claims; I would not hang a JMOD on them. [Web, Open]

**Tip-over estimate** (my calculation, not an engineering sign-off). A 34 kg JMOD on a 5.9 kg tripod, pole at its maximum 2.24 m, so the cabinet's centre of mass is about 2.45 m up. Assume legs reaching 0.5 m from the axis, so the tipping edge between two legs is about 0.25 m from the axis. The cabinet's face is 0.75 × 0.47 m, drag coefficient 1.2.

| Case | Overturning wind speed |
| --- | --- |
| Unballasted | about **12 m/s** (about 45 km/h) steady |
| With 20 kg of ballast at the stand's centre | about 15 m/s |

Gusts and rocking make real stands tip earlier than a static estimate. Working rules: **always ballast and strap the stand's centre column, guy the pole if outdoors, stop using tripod-mounted JMODs above about 8 m/s (30 km/h) gusts, and keep the audience out of the fall zone.** Have a rigger confirm for your stands and sites. [Calc, Practice]

**Sub cluster.** Four SKRAMs in a row are 2.44 m wide, 0.91 m high and 0.81 m deep; a 2 × 2 block is 1.22 × 1.83 m. A row needs no lifting above floor level. Put the cluster on castors or dollies for loading and use the vent plugs to set tuning per event (Part C). Stage 1 (two SKRAMs) is a pair side by side in the centre. [Guide, Calc]

**Growth path.** Poles first; then side stacks that put the JMODs at height without poles. A SKRAM is 914 mm high, so a two-high stack with a JMOD on top is about 2.3 m. Remember that sub-carrying side stacks reintroduce two separated bass sources (Sound Guide §10.3).

### D2 Test and hand-over card

For each cabinet, before it goes to the sound team, fill and attach to the cabinet record:

| Item | Record |
| --- | --- |
| Cabinet ID, type, date | |
| Weight | kg |
| DC resistance, each circuit | Ω |
| Polarity checked (each woofer or driver) | yes / no |
| Hatch or access panel seal | pass / fail |
| Driver models and serials | |
| FB464 version and impedance (JMOD, bi-amp) | FB464 or V2 · 8 Ω / 16 Ω |
| Connector pinout | |
| Pole flange model, rating, bolt torque (JMOD) | |
| Photos | |
| Built by, checked by | |

### D3 Transport and storage

- A finished SKRAM is about 68 kg. Two-person lifts, dollies, a van with tie-down rails and ramp, straps, covers.
- Total weight: stage 1 (2 SKRAM + 2 JMOD) about 204 kg; full rig (4 + 2) about 340 kg, plus stands and amplifiers. [Calc]
- Do not stack finished cabinets on their vents or hatches. Store dry, off the floor, ports clear.
- Keep cables, covers, port blocks and spare fasteners in labelled bags with each cabinet.
- Decide where four SKRAMs and two JMODs live **before** the build.

### D4 Roles and schedule

| Role | Does |
| --- | --- |
| CAM owner | Verifies the CAM files and post; books and supervises CNC runs; owns the re-nest decision |
| Build lead | Runs assembly; keeps the sequence and photo log; signs off cabinet checks |
| Sound lead and deputy | Takes over at the Sound Guide §5; two people, not one |
| Procurement | Plywood quotes and orders, drivers, hardware, filament |

Phases follow the Plan: **JMOD pair (Nov to Feb), SKRAM pair 1 (Mar to May), SKRAM pair 2 (summer, optional)**.

### D5 Sources

- JMOD 2.02 guide (John White, JW Sound): parts index, hardware list, parts prep, assembly steps 1–16, wiring diagrams (pp. 21–22), CNC setup notes, licence, changelog. JW Sound design pages: [JMOD](https://www.jwsound.live/designs/jmod), [Ricci's SKRAM](https://www.jwsound.live/designs/riccis-skram-subwoofer), [JMOD-M](https://www.jwsound.live/designs/jmodm-medium-format-array).
- SKRAM cut sheet (27 pages), Josh Ricci's forum notes and the Tinker & Party notes file.
- Read from the design files by me: STEP part sizes and hole schedules, DXF sizes and circles, both Fusion CAM documents (setups, stock, tools, parameters, saved toolpaths), the SolidWorks parameter sheet, the throat-adapter STL.
- B&C product pages: [DCX464 16 Ω](https://www.bcspeakers.com/en/products/coaxials-hf/1-4/16/DCX464-16), [FB464 16 Ω](https://www.bcspeakers.com/en/products/crossovers/0/16/FB464), [12NDL88](https://www.bcspeakers.com/en/products/lf-driver/12/8/12NDL88), [21DS115](https://www.bcspeakers.com/en/products/lf-driver/21/8/21DS115).
- Hardware listings: [Penn-Elcom H1105 at Parts Express](https://parts-express.com/Penn-Elcom-H1105-Recessed-Steel-PA-Cabinet-Handle-260-705), EU tee-nut listings ([Hornbach M6×9](https://www.hornbach.de/p/einschlagmutter-m6x9-mm-galv-verzinkt-100-stueck/7807804/)), [K&M 21435 / 21436 / 21459 at Canford](https://www.canford.co.uk/Products/53-3660_K&M-21459-LOUDSPEAKER-STAND-Pair-with-carry-case-black).
- Owner reports on SKRAM builds: AVS Forum and diyAudio threads (referenced in the Sound Guide §6.3).

- Sourcing update, 23 October 2026: [Wood sourcing review](Wood%20sourcing%20review.md), including user-supplied Alternative Makers portal prices, retailer links, VAT caveat and corrected staged sheet counts.
