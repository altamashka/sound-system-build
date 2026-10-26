# JMOD plywood: can we use Possling's 150 × 300 sheets?

Checked 12 Oct 2026 against the JMOD 2.02 guide (p. 9 and p. 11) and the `JMOD 2.0.step` model, which contains the designer's own nest: every part for two cabinets placed on its stock sheet. Positions below are read from that model.

## Short answer

- **Yes for the 12 mm parts.** Buy the 150 × 300 sheets and have Possling cut each one down to **1220 × 2440 mm**. The designer's nests then fit unchanged, with no CAM edits.
- **The 12 mm sheet alone is not enough.** All eight flare parts are **18 mm** (guide parts index, p. 11). You also need one 18 mm birch panel of at least **1220 × 1530 mm** for both cabinets.
- **Don't order the parts themselves custom-cut.** The JMOD parts have holes, pockets, handle recesses and 3D flare contours that only the CNC can make. A panel saw can only give you blanks.

## Thickness and material

| Material | Parts | Guide says (2 cabinets) |
| --- | --- | --- |
| 12 mm birch | top/bottom, sides, rear frame, access panels, handle braces, L and D braces, rear spine | 2 sheets |
| 18 mm birch | upper/lower and left/right flares, inner and outer | 1 sheet |

12 mm matches the plans for the panels. The model's 12 mm parts measure 12.0–12.3 mm, so measure the real Possling thickness and set it in the CAM (Build Guide A4).

## Panel sizes, per cabinet (from the model)

| Part | Qty | Thickness | Size (mm) |
| --- | --- | --- | --- |
| Top / bottom panel | 2 | 12 | 420 × 749.2 |
| Side panel | 2 | 12 | 420 × 456 |
| Rear panel frame | 1 | 12 | 455 × 733 (open frame; the D braces are nested inside it) |
| Access panel | 2 | 12 | 322 × 443.5 |
| Handle brace | 2 | 12 | 364.6 × 445 |
| D brace | 2 | 12 | 137.4 × 220 |
| L brace | 1 | 12 | 107 × 107 |
| Rear spine | 1 | 12 | 75 × 455 |
| Upper / lower outer flare | 2 | 18 | 81.8 × 724 flat |
| Left / right outer flare | 2 | 18 | 119 × 456 flat (22.5° bevels on the table saw) |
| Upper / lower inner flare | 2 | 18 | cut from one "UL flare stock" block, 524 × 740, shared by both cabinets |
| Left / right inner flare | 2 | 18 | cut from one "LR flare stock" block, 642.7 × 918.4, shared by both cabinets |

## How the designer's nest sits on a 150 × 300 sheet

The CAM uses a 4 × 8 ft stock (1219.2 × 2438.4 mm). The parts take up:

| CAM sheet | Area used by parts | Fits a 1220 × 2440 blank? |
| --- | --- | --- |
| 12 mm sheet 1 | 1179 × 2328 mm (tops/bottoms, sides, handle and L braces) | Yes |
| 12 mm sheet 2 | 1183 × 1307 mm (rear frames, access panels, spines, D braces) | Yes, with about 1220 × 1120 left over |
| 18 mm sheet | 1184 × 1508 mm (all flares) | Yes, on a 1220 × 1530 blank |

Parts are spaced 6.4 mm apart (the ¼″ bit), with a 10 mm edge margin, so the CNC's kerf is already allowed for. Possling's saw kerf (about 4 mm) only matters for the two cuts that make each blank.

![Cut plan](JMOD%20cut%20plan%20on%20Possling%20sheets.svg)

**Why cut the sheets down to 1220 × 2440 instead of using the full 1500 × 3000:**

1. A 1500-wide sheet is wider than a typical 1250 × 2500 router bed, and the guide only asks for a 4 × 4 ft bed. Confirm the bed size at Alternative Makers. If it really takes 1500 × 3000, the cut can be skipped.
2. The "Handle Recess Bottom" setup flips the 12 mm sheet, and the flip lines up only if the sheet is the width in the CAM. A blank cut to 1220 mm keeps the designer's setups valid. If the blank comes out a millimetre or two off, set the stock to the measured size in Fusion and regenerate.
3. Two people can carry a 1220 × 2440 board (about 25 kg in 12 mm). A full 150 × 300 sheet is about 37 kg.

**Could both cabinets' 12 mm parts go on one 150 × 300 sheet?** No. They need about 4.0 m² before spacing, against 4.4 m² usable, which is over 90% packing with 6.4 mm gaps between every part. It's not realistic, and it would mean rebuilding the CAM. Two sheets it is.

## Sheets and cost

The planned build is **2 JMODs**.

| | 12 mm (Possling, €148.28) | 18 mm | Total |
| --- | --- | --- | --- |
| Per cabinet | 1 sheet, €148.28 | about half of a 1220 × 1530 panel | €148.28 + 18 mm share |
| 2 cabinets | 2 sheets, **€296.56** | one 1220 × 1530 panel | €296.56 + 18 mm + cutting |

- I could not open Possling's site (it blocks automated access), so I couldn't check whether they stock 18 mm birch in 150 × 300 or what they charge per cut. At the Build Plan's assumed €110–150 per 18 mm sheet, one full sheet makes the 2-cabinet total about **€410–450**, or **€205–225 per cabinet**. That's against the Build Plan's €152 per cabinet, which assumed 4 × 8 boards.
- An 18 mm 150 × 300 sheet uses only about 40% of its area for the JMOD flares. The remaining 1500 × 1466 piece can hold the SKRAMs' 18 mm turn panels (F, 489 × 584, four needed), so it isn't wasted if Possling also supplies the SKRAM wood.
- Cutting needed: 2 cuts per 12 mm sheet (rip to 1220, crosscut to 2440) and 2 for the 18 mm. That's 6 cuts in total.

## Custom-cut parts instead?

Having Possling cut every part to size would cost more and give worse parts:

- About 20 cuts per cabinet, and only the rectangular 12 mm outlines. The rear-frame opening, handle cut-outs and recesses, 40+ holes (including the M6 tee-nut holes), pockets and every flare contour would still need doing by hand or on the CNC.
- A CNC doesn't save time on loose pre-cut parts: each would need its own setup and zero.
- It throws away the designer's tested nests and CAM.

The one custom cut worth paying for is cutting the full sheets down to CNC blanks, as above.

## What to ask Possling

*Bitte um Angebot: 2 × Multiplex Birke BFU 100, 12 mm, BB/BB (Art. 400545), jeweils zugeschnitten auf 1220 × 2440 mm, Reststücke bitte mitliefern. Außerdem: Führen Sie Birke Multiplex 18 mm BB/BB? Falls ja, 1 Platte zugeschnitten auf 1220 × 1530 mm, Rest mitliefern. Bitte mit Zuschnitt- und Lieferkosten nach Berlin.*
