# Wood sourcing review · 23 October 2026

Recommendation: use Alternative Makers for the first JMOD pair if its birch specification and VAT basis check out. Its convenience premium over Possling's published cut-to-size rates is only about €46 before transport. Seek a delivered quote for the SKRAM batches: the makerspace is convenient, but not the cheapest material source. No order or supplier message has been sent.

## Evidence and scope

Reviewed the local Build Guide, SKRAM + JMOD Build Plan and Sound Setup Guide, especially material specifications, bills of materials, CAM constraints, purchasing phases and budgets. This is a sourcing and document-consistency review, not a fresh CAD extraction, CAM simulation or verification of every electronics price. Existing design-file findings remain attributed to the 11 October review. Solana remains deferred and outside these totals.

Makerspace prices below come from Benjamin's pasted member-portal Materials page on 23 October, not a live authenticated stock check. It says purchases go on the next invoice. It does not state VAT treatment, manufacturer, core construction, glue class, stock quantity or reservation/storage policy. Treat displayed amounts as provisional final prices for comparison; confirm whether VAT is included. If they are net, multiply makerspace totals by 1.19.

## Suitable material

The current build calls for **uncoated birch throughout, BB/BB faces, sound core without problematic voids, nominal 12 and 18 mm, 2500 × 1250 mm**. Ask for the manufacturer's datasheet, ply count and EN 314-2 bonding class (prefer class 3 for this touring build), EN 636 classification, thickness tolerance and condition. Inspect edges/offcuts and measure actual sheets before CAM. BB/BB is a surface grade, not a guarantee of an identical core or bonding specification. WISA describes BB as a patched technical face grade; matching that label alone does not establish identical material. [WISA surface grading](https://www.wisaplywood.com/specifying-wisa/about-birch-plywood/)

| Makerspace option | Displayed sheet price | €/m² (3.125 m²) | Assessment for this build |
| --- | ---: | ---: | --- |
| Birch multiplex 12 mm BB/BB | €139.83 | €44.75 | Correct nominal stock; subject to specification checks |
| Birch multiplex 18 mm BB/BB | €167.79 | €53.69 | Correct nominal stock; subject to specification checks |
| Brown phenolic-coated birch 15 mm | €133.00 | €42.56 | Wrong thickness; not a direct substitute |
| Brown phenolic-coated birch 18 mm | €156.50 | €50.08 | Only €11.29 less per sheet; coating changes glue/finish preparation, so do not substitute without a tested process |
| Maritime pine 12 mm I/II | €70.81 | €22.66 | Different species/construction; not an equivalent birch purchase |
| Maritime pine 19 mm I/II | €134.47 | €43.03 | Different construction and 1 mm thicker than the metric CAM; requires design/CAM review |

HDF/MDF listed in the portal is 3–5 mm and does not meet either cabinet's stock specification. It may be useful for templates, not these enclosures. The cheaper pine and brown stock are not recommended for the first builds; the potential saving does not justify a material/process change while proving the supplied files. This is an engineering recommendation, not a claim that pine cabinets can never work.

## Retail comparison

Public listings checked 23 October 2026; they remain indicative prices, not reserved stock or delivered quotations. Retail figures below include VAT as stated by each supplier. Equivalent-sheet figures are calculated at 3.125 m²; invoicing area and rounding can differ.

| Supplier / route | 12 mm €/m² | 18 mm €/m² | 12 mm per required blank | 18 mm per required blank | Important qualification |
| --- | ---: | ---: | ---: | ---: | --- |
| Alternative Makers | €44.75 | €53.69 | €139.83 | €167.79 | Exact nominal format, already at workshop if in stock; VAT unconfirmed |
| Possling BB/BB, cut-to-size | €38.50 | €51.50 | €120.31 | €160.94 | Calculated from published area rates; confirm 2500 × 1250 blanks, charge basis, cutting fees and stock |
| Possling BB/BB, full 3000 × 1500 | €32.95 | €45.50 | €148.28 actual larger sheet | €204.75 actual larger sheet | More area for less per m², but more cash per unchanged nest; trim/re-nest and handle offcuts |
| Possling BB/C, 2500 × 1250 | €28.60 | €39.50 | €89.38 listed | €123.44 listed | Different reverse-face grade; not the agreed BB/BB comparison |
| F.W. Becker BB/BB, 2500 × 1250 | €28.26 | €37.49 | €88.31 | €117.16 | Birch throughout, 9/13 plies, EN 636-2, EN 314/3 listed; Pfungstadt supplier, Berlin freight/private-customer terms unconfirmed |
| Reinke BB/BB, 2500 × 1250 | €35.80 | €44.95 | €111.88 | €140.47 | Price benchmark only: Einbeck supplier advertises delivery within about 30 km, not a verified Berlin delivery option |

Sources: [Possling raw birch list](https://www.possling.de/preisliste/M%C3%B6bel-_und_Plattenwerkstoffe/Multiplexplatten/Multiplexplatten_Birke%2C_roh_BFU-100/katalog/5622/0/21/liste/5/list.php), [Possling 18 mm cut-to-size listing](https://www.possling.de/preisliste/M%C3%B6bel-_und_Plattenwerkstoffe/Multiplexplatten/katalog/5622/18/18/galerie/1/list.php), [Becker product range](https://shop.holz-becker.net/de/holzwerkstoffe/multiplex-platten/birke-multiplex/birke-multiplex-quer-furniert-rubric-10156.html), [Reinke prices](https://www.holzmarkt-reinke.de/birke-multiplex-bb-bb-24-mm), [Reinke delivery area](https://www.holzmarkt-reinke.de/).

Possling's cut listing has a confusing 18 mm piece-price display alongside €51.50/m². The calculations use the area rate, **not a confirmed quote for our blanks**. Its cheap standard 2500 × 1250 stock is BB/C; its BB/BB full stock is 3000 × 1500. Do not mistake the cheaper grade or a theoretical area-equivalent price for a purchasable matching board. Buying one larger sheet for every unchanged nest would cost €501.31 for the JMOD pair or €3,551.43 for the original full rig, before cuts/delivery. Larger-stock re-nesting might improve this, but has not been demonstrated.

## Correct quantities and material budgets

Counts below are base enclosure stock, excluding mistakes and any accessories that cannot be recovered from offcuts. Confirm stock for pole skid plates, port blocks, dollies/rails and test coupons in the final nest. Re-nested counts are planning targets, not simulated layouts.

| Scenario | 18 mm sheets | 12 mm sheets | Makerspace | Possling cut-rate estimate | Becker material estimate |
| --- | ---: | ---: | ---: | ---: | ---: |
| First purchase: two JMOD | 1 | 2 | **€447.45** | €401.56 | €293.78 |
| Stage 1: two JMOD + two SKRAM, supplied nests | 7 | 4 | **€1,733.85** | €1,607.81 | €1,173.34 |
| Full rig, supplied nests | 13 | 6 | **€3,020.25** | €2,814.06 | €2,052.91 |
| Stage 1, both SKRAM re-nested | 6 | 3 | €1,426.23 | €1,326.56 | €967.88 |
| Full rig, all four SKRAM re-nested together | 10 | 4 | **€2,237.22** | €2,090.63 | €1,524.81 |
| Full rig, first SKRAM pair supplied, second pair re-nested | 12 | 5 | **€2,712.63** | €2,532.81 | €1,847.44 |

The old 14-sheet claim and instruction to cut the first pair unmodified were inconsistent as a purchasing plan. Four SKRAMs re-nested together use eight regular 18 mm sheets plus one shared F-panel sheet, and two 12 mm brace sheets; add the JMOD's 1 + 2. If the first pair consumes its original six 18 mm and two 12 mm sheets, and only the second pair is optimised (five 18 mm plus one 12 mm), the combined rig uses **17 sheets**, saving €307.62 against 19. Recovering large offcuts from the first pair may improve that, but requires an actual inventory and validated nest. Do not buy 19 then assume the material saving has already happened.

Full re-nesting saves **€783.03** in makerspace material (3 × 18 mm + 2 × 12 mm). That is separate from any supplier saving and does not include additional CAM labour or CNC-time savings. A single SKRAM is €643.20 of makerspace wood as supplied; a fully batch-re-nested four-SKRAM run averages €447.44 per SKRAM. A JMOD is €223.73 per cabinet, allocated across the pair.

## Transport and the convenience premium

Possling publishes classic local delivery at **€84.95 below €2,000** merchandise value and **€62.95 from €2,000**, with unloading help required; crane unloading adds €28.95. Confirm postcode 13357, access, tax basis if unclear in the quotation, cut-order lead time and makerspace acceptance. These are delivery charges, not transport into the CNC room. [Possling delivery service](https://www.possling.de/lieferservice.php)

Using those charges as displayed, and assuming one delivery per comparison, no extra cutting fee and makerspace prices final:

- JMOD pair: Possling €401.56 + €84.95 = **€486.51**; makerspace **€447.45**, €39.06 cheaper. Collection only wins if its total cost is below the €45.89 material difference.
- Stage 1 supplied: Possling €1,607.81 + €84.95 = **€1,692.76**, only €41.09 below makerspace before cutting/unloading charges. Convenience can readily justify that margin.
- Full rig supplied: Possling €2,814.06 + €62.95 = **€2,877.01**, €143.24 below makerspace. This assumes one bulk delivery and storage; splitting into phases changes the result.
- Full rig re-nested: Possling €2,090.63 + €62.95 = **€2,153.58**, €83.64 below makerspace, again before extra charges.

Becker's gross-material advantage is **€153.67 for the JMOD pair**, **€560.51 for stage 1 supplied**, **€967.34 for the full supplied rig**, or **€712.41 for the full re-nested rig**. Those are the maximum combined freight, handling and extra procurement costs before its cash saving disappears. A national freight quote could therefore be worthwhile for the SKRAM batch; do not travel to collect in Pfungstadt merely to chase its sticker price. No Berlin freight price was verified.

The makerspace avoids a separate supplier trip/delivery booking if material really is available where it will be cut. Confirm permission to use externally supplied sheets, receiving/storage arrangements and any handling charge before comparing delivered quotes. Next-invoice billing improves timing but is not itself a discount. Do not assume sheets can be reserved, stored for free or returned.

## Document audit and budget implications

- The old Hornbach €88/€112 reference is mixed-core and 1220 mm wide. It is not the matching birch/1250 mm procurement baseline. The existing SKRAM brace nest does not fit that width.
- The original per-cabinet plywood allowances (€400–500 SKRAM, €152 JMOD) understate makerspace supplied-nest costs (€643.20 and €223.73 respectively). The original project totals are historical estimates, not current quotations.
- Replacing only those embedded wood allowances moves the old full-rig €10,340–15,230 to **€11,456–15,946** with makerspace supplied nests, or **€10,673–15,163** with full batch re-nesting. Calculation: remove €1,904 at the low end / €2,304 at the high end; add €3,020.25 or €2,237.22. These remain provisional: other prices were not refreshed, and the existing separate DCX464 uplift of about €300–370, uncertain workshop charges and unresolved electronics choices still apply.
- The old stage-1 table sums to **€7,620–11,250**. Makerspace supplied-nest wood replaces embedded €1,104–1,304, giving **€8,250–11,680**, before the DCX464 uplift and missing workshop fees. Its per-person sentence was inconsistent; use the table and identify exclusions.
- The portal's **3 mm cutter is two-flute with 17 mm cutting length, €23.57**. The saved SKRAM CAM describes an 18 mm flute and a different flute-count entry. Do not use the portal bit as a direct replacement for 18 mm through-cutting; cutter length, clearance, workholding and feeds need operator approval/regenerated CAM. It is not either JMOD ¼-inch tool. Sanding discs are €0.70 each; consumption is not known. Membership and machine rates remain unconfirmed.
- The plan's introduction and §01 still described side stacks despite the centre-cluster decision later in the document; corrected. Stage-2 fallback wording also now follows the centre cluster. The JMOD machining summary now acknowledges three flipped setups (including handle recesses), consistent with Build Guide B5.
- Sound Setup Guide reviewed for material consequences; no DSP retuning follows merely from buying birch with matching measured dimensions. It contains its existing measurement and equipment open items; they have not been re-certified by this sourcing review.

## Next procurement steps

1. Ask Alternative Makers whether listed prices include VAT; obtain birch manufacturer/datasheet, core/glue specification, available quantities, reservation rules and permission/fees for external sheets. Ask for a collective/batch discount.
2. Provisionally budget **€447.45 for the first JMOD pair's 2 × 12 mm + 1 × 18 mm**. Use workshop stock if it passes those checks and competing delivered quotes do not beat it materially.
3. Request matching **2500 × 1250 mm BB/BB birch throughout** quotes from Possling and a cheaper merchant such as Becker, delivered to Bornemannstr. 9, 13357 Berlin, with cutting, VAT, unloading and lead time itemised. Quote the next batch and full-run alternatives without committing to all sheets now.
4. Prove the first SKRAM CAM and decide when to re-nest. Buy for the selected scenario, preserving useful offcuts; do not count the 14-sheet saving until the relevant nests have been regenerated and simulated.

Draft enquiry, not sent: *Bitte um Bruttoangebot für Birke-Multiplex durchgehend Birke, BB/BB, unbeschichtet, Fertigmaß 2500 × 1250 mm, 12 und 18 mm. Bitte Hersteller, Lagenzahl, Verleimung nach EN 314-2, EN-636-Klasse, Dickentoleranzen und verfügbare Mengen angeben. Erste Bestellung: 2 Platten 12 mm und 1 Platte 18 mm; zusätzlich Staffelangebot für insgesamt 6 Platten 12 mm und 13 Platten 18 mm bzw. bei bestätigter Nestoptimierung 4 Platten 12 mm und 10 Platten 18 mm. Bitte Zuschnitt, MwSt., Lieferung nach Bornemannstr. 9, 13357 Berlin, Abladebedingungen und Lieferzeit getrennt ausweisen. Keine Transportteilung ohne vorherige Freigabe des Zuschnittplans.*
