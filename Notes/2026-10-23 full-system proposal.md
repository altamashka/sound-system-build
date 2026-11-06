> **Historical working note, 23 October 2026.** This is the previous full-system proposal, retained for its research and sources. The [current build plan](../SKRAM%20%2B%20JMOD%20Build%20Plan.md) sets the first steps. Dates, prices and proposed quantities below may be out of date; the newer guides and sourcing review take precedence.

Build proposal · v3.1 · 23 Oct 2026 · For collective review

# SKRAM + JMOD Build Plan

Four horn-loaded 21″ subs and two multiple-entry-horn tops, CNC-cut and assembled at Alternative Makers, deployed as a centre sub cluster with the JMODs on poles left and right and targeted at summer 2027 festival season. Amplification, the SKRAM driver and the sub count are still open: this version sets out the options and says what has and has not been verified. Companion documents: [Sound Setup Guide](../Sound%20Setup%20Guide.md) (measuring, aligning, limiting and operating the rig) and [Build Guide](../Build%20Guide.md) (cutting, assembly, wiring and checks).

- Cabinets: **4 + 2**
- Project cost: **€11.5–15.9k**, provisional with makerspace wood and supplied nests
- Per person (8 people): **€1,432–1,993**, provisional; exclusions below
- Build window: **12 months**
- Amp channels: **6–8**

- [01 System](#01-system)
- [02 Cabinet costs](#02-cabinet-costs)
- [03 Drivers](#03-drivers)
- [04 Amplification](#04-amplification)
- [05 DSP & measurement](#05-dsp--measurement)
- [06 Fabrication](#06-fabrication)
- [07 Phasing](#07-phasing)
- [08 Stack, stereo & sub count](#08-stack-stereo--sub-count)
- [09 Solana](#09-solana)
- [10 Decisions](#10-decisions)
- [11 Risks](#11-risks)
- [12 Verified and open checks](#12-verified-and-open-checks)

**23 October sourcing update.** [Wood sourcing review](../Wood%20sourcing%20review.md) records the supplied makerspace prices, current retailer comparisons and outstanding specifications. At displayed makerspace prices the full rig uses €3,020.25 of wood with original nests, €2,237.22 with all SKRAMs batch re-nested, or €2,712.63 when the first pair is unmodified and only the second pair is re-nested. VAT is not stated in the portal. The headline replaces only the old wood allowance; it still excludes the separately flagged DCX464 uplift and any other stale-price corrections.

<details>
<summary>Changes from earlier versions</summary>

Changes from v2 (11 Oct 2026)

Working layout decided: sub cluster in the centre, JMODs pole-mounted left and right, JMODs built first (§08, §10). The five open items from v2 are closed or advanced: the JMOD high-band PEQ Q is found and two printed settings turn out to be wrong (§05); the shared-coax limiter values are derived from B&C's ratings (§05); the SKRAM subsonic filter now rests on owner reports (§05); the amp-DSP candidates are checked (§04); the JMOD bolt count is 8 for two cabinets (Build Guide B3). New from the design files: the SKRAM CAM assumes 1250 mm-wide boards and mirrors the sheet when it flips it, one outline is cut full depth in one pass, and the SKRAM nests waste about five sheets of plywood across four cabinets (§06, §02). Two cost flags: 16 Ω DCX464 listings are higher than the €403 assumed, and the plywood count can fall from 19 to 14 sheets (§02). The Build Guide is split into a JMOD part and a SKRAM part, and the Sound Setup Guide has corrected JMOD filters and a centre-cluster alignment method.

Changes from v1

Sub count doubled to four SKRAM. Amplification reopened as three lanes with real price evidence (§04). SKRAM driver recommendation is the 21DS115, not a "higher-end" swap (§03). SKRAM height is 914 mm, which makes a two-high stack with a JMOD about 2.3 m (§08). JMOD pole mounts are external hardware per the guide, so they do not touch the CNC files. Plain PETG and PCTG are sanctioned for the printed throat adapter, so a missing PETG-CF nozzle is not a blocker. JMOD CAM is freeform 3D and is not a flat cut sheet (§06). Table saw and extra printers are now available. Genre fit, stereo versus mono, and where to save money are covered at the end of §02 and in §08.

</details>

## 01 System

Both designs are open-source and settled. SKRAM is Josh Ricci's single-21″ horn-loaded reflex sub. JMOD is JW Sound's multiple-entry-horn top. They cross at 80 Hz. The working layout is a centre cluster of SKRAMs, with the JMODs on poles left and right. Side stacks are a later option.

|  | SKRAM | JMOD 2.02 |
| --- | --- | --- |
| Designer | Josh Ricci | John White / JW Sound |
| Format | Horn-loaded reflex, single 21″ | 3-way MEH, 2×12″ + coax CD |
| Dimensions (W × H × D) | 610 × 914 × 813 mm | 750 × 470 × 420 mm |
| Weight | 52 kg cab + 14.7 kg driver (21DS115), \~70 kg finished | 34 kg |
| Range | Tuning 29.5 / 25.5 / 20.5 / 14.5 Hz | 80 Hz – 18.5 kHz, F3 55 Hz |
| Coverage | — | 90° × 60° CD, H control to 320 Hz |
| Plywood, per cab | 3 sheets 18 mm + 1 sheet 12 mm | 1 sheet 12 mm + ½ sheet 18 mm |
| Part types | 20 (A–T) | 13 |
| Joinery | Dado + rabbet, flat 2D CNC | Butt joints, freeform 3D flares, 22.5° bevels on outer flares |
| 3D printing | None | 1 throat adapter, 170 × 120 × 90 mm |
| Amp channels | 1 (or ½ if two share a channel) | 2 with FB464 (3 if tri-amped) |
| Quantity | 4 | 2 |

Vent tuning

SKRAM has four vents, each greater in area than a 6″ pipe. Blocking vents retunes the cabinet: all open 29.5 Hz, three 25.5 Hz, two 20.5 Hz, one 14.5 Hz. Tuning is a deployment decision, not a build decision — it can be changed per event.

SKRAM orientation, confirmed

v1 listed SKRAM as 610 × 813 × 914 mm without saying which is height. The STEP part files settle it: the side panel is 813 × 914 mm, the top and bottom panels are 584 × 813 mm, and the back panel is 584 × 888 mm. So width is 610 mm (24″), depth 813 mm (32″), and **height 914 mm (36″)**. The cut sheet's three-view drawing agrees.

## 02 Cabinet costs

**Current wood baseline (23 October):** Alternative Makers lists BB/BB birch, 2500 × 1250 mm, at €167.79 (18 mm) and €139.83 (12 mm), VAT basis/specification unconfirmed. The original cost tables below are retained as dated estimates so other unrefreshed prices are not presented as new quotes. See the reconciliation below and [Wood sourcing review](../Wood%20sourcing%20review.md). The old Hornbach €112/€88 mixed-core, 1220-wide boards are not equivalent procurement stock.

| Line | SKRAM, each (21DS115) | JMOD, each |
| --- | --- | --- |
| Drivers | €530–600 | €827 |
| Plywood, historical allowance (superseded) | €400–500 | €152 |
| Hardware, ports, handles | €120–180 | €100–130 |
| Filament | — | €25 |
| Finish | €60–80 | €40–60 |
| Per cabinet | €1,110–1,360 | €1,050–1,250 |
| Pair | €2,220–2,720 | €2,100–2,500 |

Choosing the 21SW152 instead adds roughly €80–210 per SKRAM, or €320–840 for four. See §03 for why that is not recommended by default.

### Full project

| Component | Low | High |
| --- | --- | --- |
| 4 × SKRAM | €4,440 | €5,440 |
| 2 × JMOD | €2,100 | €2,500 |
| Stack hardware (cups, stands, socket plates, straps, dollies) | €300 | €700 |
| Amplification + DSP, lanes A–B (§04) | €2,500 | €4,600 |
| 2 × B&C FB464 | €190 | €240 |
| Measurement kit | €110 | €250 |
| Cabling, rack, looms | €400 | €700 |
| Makerspace fees and consumables (placeholder) | €300 | €800 |
| Total | €10,340 | €15,230 |

Two lines are weak. Stack hardware is an estimate and pole-cup prices were not researched (candidates and the stand ratings are now in the Build Guide, B11 and D1; the JMODs start on poles, so this line is needed in stage 1). Makerspace fees are a placeholder: I could not find public information for Alternative Makers, so membership, CNC time and bit wear are unknown. Ask them. Lane C amplification (§04) would add about €3,600 to the high figure.

### Split across the collective

6 people**€1,720–2,540***€144–212 / month*

8 people**€1,290–1,900***€108–159 / month*

10 people**€1,030–1,520***€86–127 / month*

Monthly figures assume the full amount spread evenly across the twelve-month build window. Actual outlay is lumpy — see §07.

### Current plywood budget and sourcing, 23 October

| Scenario | 18 mm | 12 mm | Makerspace wood total |
| --- | ---: | ---: | ---: |
| First JMOD pair | 1 | 2 | **€447.45** |
| Stage 1, original nests | 7 | 4 | **€1,733.85** |
| Full rig, original nests | 13 | 6 | **€3,020.25** |
| Stage 1, both SKRAMs re-nested | 6 | 3 | €1,426.23 |
| Full rig, all four SKRAMs batch re-nested | 10 | 4 | **€2,237.22** |
| Full rig, first SKRAM pair original / second pair re-nested | 12 | 5 | **€2,712.63** |

Re-nests are unverified planning targets; original CAM also needs the documented corrections and simulation. The conservative sequence proves the first pair before optimising the second: **17 sheets, not 14**. Full batch re-nesting saves €783.03; the staged 17-sheet route saves €307.62. Recovering earlier offcuts may improve the staged count only after inventory and layout verification. Allow for accessories/test cuts or mistakes separately. Buy **2500 × 1250**, not 1220-wide boards.

**Recommendation:** workshop birch for the first JMOD pair if the spec/VAT checks pass; seek delivered batch quotes before SKRAM procurement. Possling BB/BB cut-rate estimate is €401.56 for the JMOD pair, but its published local delivery is €84.95 below €2,000 merchandise value, making that route €486.51 before any extra cuts/unloading. Cheaper matching-format merchant listings warrant a freight quote for the larger batches. Possling's cheaper standard 2500 × 1250 boards are BB/C, whereas its BB/BB full sheets are 3000 × 1500. Core and glue quality must be compared separately from face grade. Evidence and cost thresholds are in the sourcing review.

**Budget reconciliation, not a complete re-quote:** the old full-project table includes €1,904–2,304 of plywood. Replace that with €3,020.25 for original nests: **€11,456–15,946**, about **€1,432–1,993 each at eight**. Full batch re-nesting gives **€10,673–15,163**. The historical stage-1 rows sum to **€7,620–11,250**; replacing embedded wood (€1,104–1,304) gives **€8,250–11,680** with original nests. Other prices remain dated; add the separate DCX464 uplift below if applicable, and workshop fees missing from the stage-1 table. The old collective/monthly and phase allowances are historical and must be refreshed before collecting contributions.

**Cost flag, DCX464.** 16 Ω DCX464 listings I found are €551 (Sonovente, VAT basis unclear) and €586 including VAT (Toutlehautparleur), against the €403 assumed in §03. If those are the real prices, the two JMODs cost about **€300–370 more** than shown, and the totals in this section rise by that amount. I could not open the Sonovente page to confirm the VAT basis. Re-quote before ordering.

### Where to save

Ranked by money saved per unit of risk. The first few cost almost nothing in sound quality or operating hassle.

| Idea | Saves | What you give up |
| --- | --- | --- |
| Stage 1 = 2 SKRAM + 2 JMOD. Add pair 2 only if events call for it | €2,250–2,760 (cabinets, drivers, plywood), plus a second CNC block and build time | Sub headroom at big or outdoor events (§08) |
| Buy the 8 Ω 21DS115 and a sub amp that can drive two per channel, so pair 2 later needs no new amp | Avoids a second sub amp later (about €850–2,150) | Nothing; slightly less power per sub in stage 1 |
| Amp lane A instead of B (§04), buying only matched, tested units | About €0.8–1.7k | Warranty and in-box limiters |
| Trade quotes for plywood: BB/BB, void-free, price breaks | Unknown; may offset the retail risk above | A few hours of emails |
| UMIK-1 only, no EMX-7150 | €140 | Nothing; the UMIK-1 is enough for REW |
| Own Speakon looms, used rack | €100–300 | Some build time |
| Delay stands and socket plates until the stack arrangement is chosen (§08) | €150–400 | Placement flexibility for the JMODs in stage 1 |

Not worth cutting: the validated JMOD drivers (an unvalidated woofer saves about €200 per cabinet for an unknown acoustic result), the FB464s (needs more amp channels without them), birch plywood (MDF is heavier and weaker in the dados), and the DS115 itself (the cheapest 21″ in §03 once current prices are checked).

Stage 1 total (2 SKRAM + 2 JMOD, same amp lanes):

| Component                                     | Low    | High    |
| --------------------------------------------- | ------ | ------- |
| 2 × SKRAM                                     | €2,220 | €2,720  |
| 2 × JMOD                                      | €2,100 | €2,500  |
| Stack hardware                                | €200   | €450    |
| Amplification + DSP, lanes A–B (§04)          | €2,500 | €4,600  |
| 2 × B&C FB464                                 | €190   | €240    |
| Measurement kit (UMIK-1)                      | €110   | €140    |
| Cabling, rack, looms                          | €300   | €600    |
| Historical total                             | €7,620 | €11,250 |

With the current makerspace wood and original nests, stage 1 is provisionally €1,031–1,460 per person at eight, before the DCX464 uplift and workshop fees. Use the reconciliation above instead of the historical per-person figures.

Draft plywood request (German, not sent): *Bitte um Angebot: Birke Multiplex 18 mm und 12 mm, 2500 × 1250 mm, BB/BB, BFU 100, lückenfrei im Kern, Staffelpreise ab 10/25/50 Platten, Zuschnitt- und Lieferkosten nach Berlin.*

## 03 Drivers

### SKRAM · 21″ options

Ricci's notes name the 21DS115 and the Lavoce SAN214.50 as the drivers the design was optimised for, and say the 21SW152, 18Sound 21NLW9601 and others should also match. IPAL drivers work but were deliberately not the target.

| Driver | Approx. € incl. VAT | Weight | Rating | Note |
| --- | --- | --- | --- | --- |
| B&C 21DS115 | \~570 (Thomann); £495 UK | 14.7 kg | 1700 W AES, 99 dB | The reference driver. Neodymium. Xmax about 15 mm. Strong motor. |
| B&C 21SW152 | \~650–780 EU shops; £579 UK | 18.5 kg | 2000 W AES / 4000 W prog., 96 dB | Neodymium. More power handling, 3 dB lower rated sensitivity, 4 kg heavier. |
| 18Sound 21NLW9601 | \~1,000–1,100 (€837 ex VAT) | \~14 kg | 1800 W | Neodymium. About double the DS115 price, no meaningful weight saving. |
| Lavoce SAN214.50 | \~750–810 | \~15 kg | 1700 W AES, 3400 W prog. | Neodymium. Named by Ricci. v1's €380–450 and 1200 W figures do not match current listings: it now costs more than the DS115. |
| B&C 21IPAL | \~980 ex VAT | 23 kg | 5000 W prog. | 1 Ω driver for Powersoft IPAL amplifier modules. Out of scope. |

Recommendation

**21DS115.** An earlier draft of this plan treated the 21SW152 as the higher-end choice. The data does not support that for this cabinet. The DS115 is the driver the cabinet was optimised for, it is lighter than the SW152, it is rated about 3 dB more sensitive, and it costs less than every other 21″ in the table. The SW152's advantage is power handling, which only matters above the 1,000–1,500 W per sub this rig will run. The one real step up in the B&C range is the IPAL, which needs IPAL-class amplifier modules and is out of scope. Do not mix driver models across the four.

Two cautions on specs: the retail "99 dB" figure for the DS115 is higher than calculated values (about 97 dB) in the databases checked, and the 8 Ω Thiele-Small figures disagree between sources (Fs 30–36 Hz). Check B&C's own datasheet before relying on any simulation.

### JMOD · driver set

The JMOD driver set is already premium, so there is no meaningful step up.

| Position | Driver | Qty / pair | Approx. € | Note |
| --- | --- | --- | --- | --- |
| Midbass | B&C 12NDL88 | 4 | 212 ea | Standard recommended, validated by JW Sound. |
| Midbass, ultra premium | 18Sound 12NTLW3500 | 4 | Not priced | Listed in the guide as TBD, unvalidated. |
| Coax CD | B&C DCX464 | 2 | 403 ea | 16 Ω preferred for noise floor. |
| Coax CD alt | BMS 4594HE | 2 | \~500 ea | Requires cabinet depth modification. Not recommended. |

Budget and unvalidated alternatives exist for the woofers but save about €200 per cabinet against an unquantified acoustic risk: the published targets and .mdat were measured with 12NDL88s.

### Impedance and wiring

JMOD's guide states 4/8/16 Ω woofers are all acceptable — wire for the desired load. Two 12NDL88 per cabinet:

| Driver Z | Wiring | Load | Note |
| --- | --- | --- | --- |
| 8 Ω × 2 | Parallel | 4 Ω | Full amp power, simplest wiring. Default choice. |
| 8 Ω × 2 | Series | 16 Ω | Only if amp channels are power-limited at low Z. |
| 16 Ω × 2 | Parallel | 8 Ω | Middle option. |

SKRAM is a single driver, sold in 4 Ω and 8 Ω. The wiring choice depends on the amp lane (§04): one SKRAM per channel at 4 Ω, or two 8 Ω SKRAMs in parallel on one channel.

## 04 Amplification

This section is open. The collective favours Powersoft; the evidence below shows where that is cheap and sensible and where it is not.

### What the rig needs

| Load | Qty | Impedance | Target power |
| --- | --- | --- | --- |
| SKRAM (21DS115, 1700 W AES) | 4 | 4 Ω | 1,000–1,500 W each |
| JMOD LF | 2 | 4 Ω | 700–1,000 W each |
| JMOD mid+HF via FB464 | 2 | 8–16 Ω | 300–500 W each |

### Two ways to wire the subs

| Wiring | Channels (with FB464 on JMODs) | Trade-off |
| --- | --- | --- |
| One SKRAM per channel (4 Ω) | 4 sub + 4 JMOD = **8** | Each sub gets its own limiter and a fault stays contained. Needs ≥1,000 W per channel. |
| Two 8 Ω SKRAMs in parallel per channel (4 Ω load), one channel per stack | 2 sub + 4 JMOD = **6** | Fewer channels, so cheaper amps. Needs ≥2,000 W per channel. A limiter event or channel failure takes out both subs in a stack. |

If pair 2 is a possibility, buy the 8 Ω DS115 and a sub amp that can drive two per channel (K3, XTi 6002 or Duecanali class). One 8 Ω sub per channel works in stage 1, and pair 2 later parallels onto the same channels with no new amp. With 4 Ω drivers you are locked to one per channel on a channel of at least 1,200 W.

### What is on the market

Power is per channel into 4 Ω. "Used" prices are asks, not sales; the German listings are private sellers with no warranty and were posted on 05 May 2026 (they appeared still live on 09 Oct but may be gone).

| Option | Channels · power | DSP | Price evidence | Fit |
| --- | --- | --- | --- | --- |
| Powersoft X4 (touring, 1U, 15 kg) | 4 · 3,000 W | Yes (ETH, or Dante) | Used €4,750–6,120 ex VAT, three dealers, 21-day warranty on two. New \~$10.7–12k. | Oversized: three times what the drivers can use. Skip. |
| Powersoft K3 (touring, EOL) | 2 · 2,600 W | DSP version exists; the €850 ad is non-DSP | €850 private (3 units, Nordrhein); £1,327 eBay UK; £2,135 dealer. | Right size for the 6-channel plan (two subs per channel). |
| Powersoft K2 DSP (touring, EOL, \~8 kg) | 2 · 1,950 W | Yes | No used listings found. | Right size for two subs per channel; rare. |
| Powersoft M50Q (touring, EOL, 1U, 7.4 kg) | 4 · 1,250 W | Standard model: none stated. HDSP+ETH variant has DSP. | €950 private (1 unit, Nordrhein), DSP unstated. No HDSP+ETH used listings found. | Best used fit for one sub per channel, or for the JMODs. |
| Powersoft M28Q (touring, EOL, 1U) | 4 · 700 W | As M50Q | \~€700 private ask. | Fits the JMODs (LF 700 W plus coax), not the subs. |
| Powersoft Quattrocanali 2404 / 4804 (install) | 4 · 600 W / 4 · 1,200 W | Yes (DSP or DSP+D) | New \~€3,500 / \~€4,100 (4804 listed out of stock). No used found. | Capable, expensive; install-series. |
| Powersoft Duecanali 4804 (install) | 2 · 2,400 W | Yes | Price on request. | Fits two subs per channel. |
| Crown XTi 4002 | 2 · 1,200 W | Yes, in-box | \~€1,139 new in Germany (comparison site, verify); B-stock \~€1,000. | Good match for one sub per channel; warranty. |
| Crown XTi 6002 | 2 · 2,100 W | Yes, in-box | £1,869 incl. VAT at one UK shop (steep discount, verify); $2.8–3.1k US. | Fits two subs per channel. |
| Lab Gruppen FP 10000Q | 4 · 2,100 W | None | Used \~$2,550–2,900; new £2,590. | No DSP and not cheaper than Powersoft used. |
| Linea Research 44M10 | 4 · \~2,500 W | Yes | \~£4,493 new; no used found. | Over budget. |

K-series, M-series and their DSP variants are all end-of-life per Powersoft's own pages, so used units are the only supply and future service is uncertain. The X-series (X4) is current.

### Outboard DSP, if the amps have none

| Unit | Price evidence | Notes |
| --- | --- | --- |
| dbx DriveRack 4800 | Used \~$1,800–2,000 | 4 in / 8 out, real limiters, discontinued. |
| miniDSP Flex Eight | \~€800 new (Dutch retailer) | 2 in / 8 out, RCA outputs. No limiter in the spec found; a compressor can be abused as one. Still in production. |
| miniDSP 4x10 HD | \~€665 | Balanced outputs on terminal blocks. Availability uncertain; no limiter found. |

**Checked against the Sound Setup Guide's requirements (11 Oct 2026; detail in Sound Setup Guide §2).** The open item "I haven't verified every candidate processor has real limiters" is now answered for the ones I could reach. The DriveRack 4800 has PeakStopPlus limiting and the 12 dB Linkwitz–Riley slope JW's woofer low-pass needs, but no documented RMS limiter. The Flex Eight has a per-output compressor, not a documented limiter, and its "+12 dB" display is 0 dBFS, so thresholds are easy to misread. The 4x10 HD could not be confirmed either way. In-box DSPs: the **Crown XTi has a peak limiter only and no 12 dB LR slope**; **Powersoft amps without DSP have only a built-in clip limiter and a "long term" limiter**, which protect the amp, not our drivers; the M-series DSP variant lists peak, RMS and frequency-dependent RMS limiters. Consequence for the lanes below: a Powersoft is only worth buying here if it is a DSP variant, and a Crown XTi works for the subs but not exactly for the JMOD woofer channel.

### Three lanes

| Lane | Configuration | Cost | Pros | Cons |
| --- | --- | --- | --- | --- |
| A · Used Powersoft + outboard DSP | 1 × K3 for the subs (two per channel) + 1 × M50Q or M28Q for the JMODs + DriveRack or Flex Eight | \~€2,200–4,900. About €2,600–3,500 if the private asks are still available. | Cheapest. Light 1U Powersoft amps. Replaceable later. | No warranty. Protection depends on the outboard DSP. EOL. Condition unknown. Without in-box DSP you lose Powersoft's main advantage. |
| B · New Crown XTi with in-box DSP | 1 × XTi 6002 for the subs (two per channel) + 2 × XTi 4002 for the JMODs | \~€3,900–4,600 | Warranty, in-box limiters, available now. Matches the power needs. | Not Powersoft. Reliability reports are anecdotal. Weight not checked. |
| C · New Powersoft install | 2 × Quattrocanali 4804 DSP+D (8 channels, one sub per channel) | \~€8,200+ | One model, one software, in-box DSP, spare channels. | Roughly double lane B. Install-series. 4804 DSP+D listed out of stock. |

Recommendation

Not a decision for me to make, but the evidence points one way: a Powersoft's main value here is in-box DSP and limiting, and most used units found do not have it. If the collective wants Powersoft and can wait, watch the used market for DSP-equipped K2, K3 or M-series amps and Quattrocanali. Otherwise choose between A (cheapest, more risk) and B (safest, not Powersoft). Whatever is bought, buy amps late: nothing else depends on them, and the cabinets do not change with the lane. Replace them later without touching a cabinet.

Before buying any used amp: confirm the exact variant (DSP or not), test every channel under load, ask for serial and firmware, get a dated photo of the rear panel, and confirm that Powersoft's current Armonía software supports that model. I could not verify that last point.

Buy the FB464s regardless of lane. They halve JMOD channel requirements and de-risk the coax while the collective is still learning to set limiters. See §05 for a caveat.

## 05 DSP & measurement

Both designers publish *acoustic* targets, not filter settings. The Solana guide states it directly: electrical crossover points and slopes are not equal to acoustic ones. Filters are shaped until the measurement matches the target. Wherever the DSP lives (in the amp or outboard), the presets and limiter settings need documenting and backing up before any event.

### JMOD published targets

| Band | Delay | Gain | HPF | LPF |
| --- | --- | --- | --- | --- |
| Low | 0.4 ms | 0 dB | 80 Hz LR4 | 195 Hz LR2 |
| Mid | 0 ms | −4 dB | 370 Hz LR4 | 3600 Hz BU3 |
| High | 0.22 ms, polarity inverted | −5 dB | 3600 Hz BU2 | — |

Plus PEQs on the mid and high bands (guide p.7). Raw measurements and EQ/XO settings ship as Raw Measurements and EQXO Settings.mdat — an REW file. Open it before building; it is the reference the build gets compared against.

**The printed PEQ list is wrong in two places, and the REW file has the right values.** I read the filter sets stored inside the .mdat and checked them numerically against the file's own EQ'd traces (Sound Setup Guide §6.2). Mid band: the boost is at **640 Hz** (the page says 540 Hz), PEQ 2 is Q1.85. High band: the file has **three** peaking filters, 3,450 Hz −7.5 dB Q1.3, **6,000 Hz +5.0 dB Q5.0** and **8,000 Hz +2.5 dB Q2.5**; the page lists "6000Hz +2.5dB Q" and stops, so the Q is missing from the printed guide itself and the 8 kHz filter is absent. The numbers fit the file's traces to 0.02 dB; the printed ones do not (0.55 dB and 0.84 dB scatter, worst points 2.0 and 2.5 dB off). This closes the "Q is cut off" open item. It proves what produced JW's published traces, not what is in his hardware preset, so ask JW to confirm. The file also defines the acoustic targets: woofers 80 Hz LR4 high-pass with 500 Hz LR6 low-pass, mid 500 Hz LR6 high-pass with 4,000 Hz LR4 low-pass, high 4,000 Hz LR4 high-pass.

### JMOD published limiter settings

The guide (p. 7) also publishes limiter values, as voltages at the speaker terminals:

| Channel | Peak limiter (threshold / attack / release) | RMS limiter (threshold / attack / release) |
| --- | --- | --- |
| 12NDL88 pair (2 × 8 Ω in parallel) | 105 V / 12.5 ms / 200 ms | 75 V / 2,500 ms / 5,000 ms |
| DCX464 Mid (16 Ω) | 59 V / 2.7 ms / 21 ms | 42 V / 1,600 ms / 3,200 ms |
| DCX464 HF (16 Ω) | 50 V / 1 ms / 2 ms | 35 V / 800 ms / 2,400 ms |

Working these back to watts shows the rule: the RMS limiter sits at the driver's nominal (AES) power, and the peak limiter at its program power, twice nominal (about +3 dB in voltage). B&C's own pages now confirm the ratings behind it: DCX464 16 Ω is 110 / 220 W (mid) and 80 / 160 W (HF), 12NDL88 is 700 / 1400 W. The same rule gives the starting point for the SKRAM. This also means the processor must accept limiter thresholds in volts, or take the amplifier's gain, or the collective will be converting by hand (see the Sound Setup Guide, §7).

### FB464 caveat

The FB464 crossover splits the coax at 3.6 kHz (18 dB/octave on the LF side, 12 dB/octave on the HF side). That matches JW's published 3600 Hz BU3 and BU2 split, which is reassuring. But the published high-band delay, polarity, level and the 370 Hz mid HPF cannot be set independently behind a passive network on one shared channel. As far as I could tell from the .mdat's contents, it holds tri-amp traces (DCX MID, DCX HIGH, Target MID) and no FB464 trace. Expect to measure and re-tune this route rather than load published numbers. The FB464 comes in 8 Ω and 16 Ω versions to match the DCX464 (16 Ω preferred), at about €80–100 each ex VAT.

What the research changed. (1) The mid and HF PEQs can be reapplied to the shared channel almost unchanged, because the passive split keeps each in its own section; the exception is the 3,450 Hz −7.5 dB filter, which would also cut the mid across the crossover, so leave it out at first. (2) **Limiters are derived, not guessed**: modelling an ideal split with B&C's ratings, the mid section limits at about 42–45 V RMS on real music and the HF section only at 36 V if the signal is HF-only. Start at **35 V RMS and 50 V peak** (safe for any spectrum) and raise toward 42 V and 59 V only after measuring. The v2 guess (JW's HF values) was safe but needlessly strict on the mid. (3) **The FB464 exists in two versions**: the standard one protects with series filament bulbs (B&C publishes no power rating); the **FB464V2** has higher-power inductors and no bulbs, so only the DSP limiter protects the drivers. A 16 Ω V2 is listed but was out of stock at the one EUR source I found. (4) B&C pairs the network with its **ME464 horn**, not the JMOD's, so expect the combined response to need shaping above 3.6 kHz.

### SKRAM subsonic filter

The designer publishes no filter, and I found no measured excursion data for a 21DS115 in a SKRAM. Owner reports, all secondhand (read as search-result summaries; the AVS Forum pages sit behind an access gateway I did not use), run corners between about 23 and 31 Hz with all vents open: a 12 dB Butterworth at 23 Hz and later 27 Hz; a 24 dB Linkwitz–Riley at 31 Hz; and a seller who ran a 20 Hz cutoff with one vent blocked (about 25 Hz tuning). The Sound Setup Guide (§6.3) now starts at **27 Hz, 24 dB per octave Butterworth with all vents open**, and 24, 20 and 15 Hz for three, two and one vent open (extrapolated, weaker evidence), and gives three checks to confirm it on the built cabinets. It is still a start value, the one setting not to trust blindly, but it is no longer a bare guess.

### Kit

| Item | Cost | Note |
| --- | --- | --- |
| miniDSP UMIK-1 | €110 | USB, individually calibrated, no interface needed. |
| EMX-7150 + interface | €250 | What JW Sound used for the published measurements. |
| REW | Free | — |

Sequencing

Buy the mic in month one, not when the first cabinet is finished. It is needed to verify SKRAM vent tuning and it is the cheapest item on the list. Learning REW on a single-driver sub is materially easier than learning it on a three-way.

## 06 Fabrication

The equipment table below is as reported by the collective. I could not find public information on Alternative Makers, so fees, booking rules, supervision requirements and the CNC's real stock size are unconfirmed.

| Requirement | Source | Available |
| --- | --- | --- |
| CNC router, 4′×4′ minimum | JMOD guide | Reported: Mekanika Full Board Fab CNC |
| Dado + rabbet joinery | SKRAM parametric model | Yes — same machine |
| ¼″ compression bit + ball end mill | JMOD CNC setup | Confirm tooling is stocked |
| Fusion (free personal licence) with a post for the router | JMOD CAM | Needed. See below. |
| Table saw, 22.5° bevels | JMOD parts prep | Yes — now set up |
| Trim router + ¼″ roundover | Both designs | Yes |
| Brad / staple nailer | JMOD assembly | Yes — pneumatic |
| 3D printer, 170×120×90 mm | JMOD throat adapter | Yes — 5 × Prusa Core One, 250×220×270, plus further printers |
| Filament for the throat adapter | JMOD guide, p.9 | PETG-CF preferred, but plain PETG, PETG-GF and PCTG are rated GOOD; ASA/ABS ACCEPTABLE; avoid PLA, TPU, PVB |
| Hardened nozzle | CF/GF filament only | Plain PETG and PCTG run on a standard nozzle |
| Dust extraction | 19 sheets of ply | Yes — throughout |

### Machine time to book

| Job | Quantity | Note |
| --- | --- | --- |
| CNC — SKRAM pair 1 | 6 × 18 mm, 2 × 12 mm | 20 part types, dado/rabbet, flat 2D |
| CNC — SKRAM pair 2 | 6 × 18 mm, 2 × 12 mm | Same files, second block |
| CNC — JMOD pair | 1 × 18 mm, 2 × 12 mm | Freeform 3D, three flipped setups including handle recesses |
| Total sheets | 19 original; 14 all batch re-nested; 17 first pair original / second pair re-nested (§02) | Book each pair as one block, not per cabinet |
| Print — JMOD adapters | 2 × 438 cm³ | \~1 kg filament, \~45–50 machine hours; under 25 h each across two printers |

SKRAM is flat, JMOD is not

SKRAM's STEP contains only planar and cylindrical surfaces, so it is flat 2D work. The package carries three Fusion CAM files (Mar 2024, May 2026, Jun 2026), each with 12 toolpaths. **I have now compared them and read their settings** (Build Guide C5): all three have the same seven setups; the May file has every toolpath flagged invalid (stale); the June file differs from May only in the 12 mm outline's `side` setting and has valid toolpaths, so **use the June 2026 file**. The stock is a fixed **2500 × 1250 mm** box, one **3 mm flat end mill** at 5,000 rpm and 1,000 mm/min, with the 18 mm sheets cut in an underside and a topside setup. Findings to act on: the nests need **1250-wide boards**; the flip mirrors the sheet about its width, so a sheet that is not exactly the width in the file puts the underside pockets off; Z zero is the spoilboard, so sheet thickness errors show up as dado depth errors; sheet 2's outline and four pocket operations are set to cut full depth in one pass; and the driver, hatch and screw holes are in the DXFs but not in the STEP parts. I did not run or simulate any of it.

SKRAM is an imperial design

Dimensioned in inches — 24″×32″×36″ exactly. The parametric spreadsheet specifies 10-32 and ¼-20 threaded inserts, which are not standard EU stock; substitute M5 and M6. US designs assume ¾″ (19.05 mm) and ½″ (12.7 mm) plywood. The Tinker & Party STEP files are foldered as 12 mm and 18 mm, so conversion appears done — but verify the RootDim sketch against the actual measured thickness of the sheets you buy. Dado joinery compounds a thickness error across every joint, and with four cabinets any error is built four times.

JMOD cannot be cut from flat 2D drawings

Unlike SKRAM, JMOD's flares are contoured 3D parts. The STEP contains 104 freeform (B-spline) surfaces alongside planar and cylindrical ones, and the Fusion file holds a finished CAM job of 6 setups and 18 operations, 16 with a ¼″ compression bit and 2 with a ¼″ ball-nose. The guide describes the two flip setups: the inner left/right flares stay joined to one stock piece and are flipped to mill the cone-recess contours, and the inner upper/lower flares are flipped to mill the throat-adapter mounting flanges. That means:

- The toolpaths are the design. Anyone cutting JMOD needs Fusion, or a CAM program that can rebuild 3D finishing passes from the STEP. A DXF export is not enough.
- The post-processor has to match the makerspace's router. The file was generated on the designer's own setup, so check units, stock size, zero position and the machine's controller before the first cut.
- Ball-nose depths depend on real sheet thickness and flip registration. Measure the birch before cutting and cut a test piece first.
- I checked the file's contents (tool list, setup and operation counts, surface types) but did not run or simulate the toolpaths. Open it in Fusion and review the setups before booking. Read since v2 (Build Guide B5): the stock is a solid taken from the model, and the STEP carries 4 × 8 ft (1219.2 × 2438.4 mm) stock bodies, so it fits 2500 × 1250 boards and has about 0.8 mm to spare on 1220 boards; the compression bit runs at 16,000 rpm and 4000 mm/min, the ball-nose at 19,000 rpm; and the operations named "Mark holes" may only mark centres, so some tee-nut holes may need drilling by hand.
- The supplied throat-adapter STL is **169.9 × 120.0 × 90.0 mm**, so the guide's "170 × 110 × 90 mm minimum build volume" is one direction short unless the part is rotated; our printers fit it either way.

JMOD needs finish work the drawings do not show

Assembly steps 9 and 10 call for filler and sanding to bridge gaps between the printed throat adapter and the plywood flares, and between the flare panels themselves. The transition where the woofer mounts has to be flat enough to seal. Budget time and a session of hand work per cabinet.

JMOD pole mount

The JMOD guide recommends external pole-mount hardware, since space inside is tight. Position it on the centre of mass, 245 mm from the front lip with 12NDL88s. This is a bolt-on part, not a CNC change, and **because the JMODs start on poles it is part of the first build**, not an accessory. Stands: the K&M 21436 is rated 40 kg, too thin a margin for a 34 kg cabinet outdoors; the K&M 21435 (steel tripod, 1430–2240 mm, 5.9 kg) is listed at 50 kg by one retailer, and earlier sellers gave 35 kg, so confirm with K&M. My static tip-over estimate for a 34 kg JMOD on such a stand at full height is about 12 m/s (45 km/h) of steady wind unballasted, about 15 m/s with 20 kg of ballast, which is why the Build Guide (D1) sets a working limit of about 8 m/s gusts and requires ballast and guying. Pole-cup candidates, a skid-plate construction and the checks are in Build Guide B11.

## 07 Phasing

Tops before subs. Two JMODs make a working system the day they are finished — F3 is 55 Hz. JMOD also needs three sheets of plywood against SKRAM's sixteen, so it is the cheaper and faster first phase. The SKRAMs follow in two pairs, and each stage is usable on its own. Phase allowances below are historical estimates; use the 23 October wood totals in §02 and refresh remaining purchases before ordering.

Sep – Oct 26

#### Decisions and setup

- Vote the open items in §10
- Makerspace membership; ask for fees, CNC rates, supervision and booking rules
- Open the JMOD .f3d in Fusion, review the 6 setups, and confirm the makerspace can post and run them
- Buy UMIK-1, install REW, open the JMOD .mdat
- Verify SKRAM RootDim against real sheet thickness
- Quote original (19), batch-re-nested (14), and conservative staged (17) sheet scenarios; buy only the selected next batch

€150–300

Nov – Dec 26

#### JMOD procurement

- Order 4× 12NDL88, 2× DCX464, 2× FB464 (matching impedance)
- Order 3 sheets plywood (12 mm, 12 mm and 18 mm; the JMOD stock is 4 × 8 ft, so 2500 × 1250 boards fit)
- Buy external pole flanges and two stands rated for a 34 kg cabinet (50 kg or more), plus ballast bags (Build Guide B11, D1)
- Book CNC; print both throat adapters

€2,500–2,850

Jan – Feb 27

#### JMOD build

- CNC cut, 22.5° bevels, tee nuts, roundovers
- Staged glue-up, filler and sanding
- Finish and hardware, including the pole flange and its skid plate

€200–350

Feb – Mar 27

#### Amplification for the tops and first sound

- Buy the JMOD amplification and the DSP (lane A or B), rack, Speakon looms
- Ground-plane measure at 10° off-axis; tune to published targets
- Two JMODs on stands: system is usable from here

€1,650–3,250

Mar – Apr 27

#### SKRAM pair 1 procurement

- Order 2× 21DS115 (8 Ω if two per channel)
- First SKRAM pair: order 6 × 18 mm + 2 × 12 mm, **€1,286.40** at displayed makerspace prices, on **2500 × 1250** boards. Six-sheet batch re-nest is a separate validated-CAM option, not the conservative first-pair baseline
- Buy the sub amplification
- Book CNC block

€3,000–4,750

Apr – May 27

#### SKRAM pair 1 build

- Cut, dry-fit, assemble both cabinets
- Handles, vents, connectors, finish
- Castors or skid, vent blocks (the centre-cluster baseline needs no socket plates on the SKRAM tops; they return with side stacks)

€360–520

May – Jun 27

#### Integration

- Sub/top alignment, delay and polarity
- Set vent tuning for typical use
- Limiters, presets, transport and storage solved
- Shakedown event with one SKRAM per JMOD

€200–400

Jun – Aug 27

#### SKRAM pair 2 (stage 2)

- Order 2 more drivers; wood is 6 × 18 mm + 2 × 12 mm (€1,286.40) as supplied, or 5 × 18 mm + 1 × 12 mm (€978.78) after validated pair re-nesting; audit saved offcuts first
- Second CNC block, build, finish
- Add the second pair to the centre cluster (a row of four); re-measure and re-set the alignment, or move toward side stacks if the programme calls for it (§08)

€2,250–2,760

Stage 2 is not a dependency for the first events. If it slips, the rig runs two SKRAMs together in the centre with JMODs on poles left and right, which is a complete system. Swap the JMOD and SKRAM phases only if the programme is bass-led and a tops-only period would be unusable in practice; the cost is that nothing makes sound until roughly March.

## 08 Stack, stereo & sub count

Question: four SKRAMs in two-high stacks, a different or additional sub type, or a rethink of the cabinets. Recommendation: stay with four SKRAMs and two JMODs, and settle the arrangement before pair 2.

### Working baseline and growth path (decided 11 Oct 2026)

**Baseline: Arrangement C with poles.** The SKRAMs sit together in a centre cluster and the two JMODs stand on poles left and right (a row of four SKRAMs is 2.44 m wide, a stage-1 pair 1.22 m). The subs behave as one source, nothing but the JMODs is lifted above floor level, each top gets its own delay (Sound Setup Guide §9.7), and the JMOD pole flange is part of the first build (Build Guide B11). The earlier recommendation to plan a socket plate on the SKRAM top for two-high stacks is no longer needed in stage 1.

**Growth path: side stacks.** Later, SKRAMs, SKHORNs or similar bass bins go under the JMODs on the sides so the tops reach mounting height without poles. A SKRAM is 914 mm high, so a two-high stack with a JMOD on top is about 2.3 m (arrangement A). That puts bass sources at the sides again, so the "power alley" returns in proportion to the bass the side stacks carry; the Sound Setup Guide §10.3 lists options to test (high-pass the side-stack bass cabinets higher so the centre cluster keeps the lowest octave; give them their own delay; or accept two groups if the stacks are close). **SKHORN** (JW Sound hosts Ricci's design): two 21″ drivers, 610 × 812 × 1371 mm, 195 lb (about 88 kg); JW Sound deployed 8 SKRAM and 2 SKHORN at a 2025 festival. I could not identify the "Paraflex type O" design you mention; I found only forum discussion of a "Paraflex" mid-high design (the plans appear to be shared in a Facebook post, not on a plans site) and no plan set, so tell me what you mean before I research it.

**Future mid-tops other than JMOD.** JMODs are the expensive line (about €1,050–1,250 each). Leads for cheaper or complementary tops, none researched beyond their pages: JW Sound's **SAWMOD** (a "shared aperture waveguide module", a point source for monitoring, fill and small mains, plans and a paper released), **JMOD-M** (an arrayable 110° × 55° variant, 80 kg, 145 × 73 × 63 cm, still "under development/rework"; JW's JMOD FAQ also mentions medium-coverage arrayable tops in development), the **Solana** (§09, 12.5 kg point source), and JW's **DH350-based MEH** (prototype, 60 Hz to 16 kHz, 106 dB, battery-powered). **Dedicated bass bins** for 80 to 160 Hz remain the JMOD FAQ's own suggestion if mid-bass is thin. None of these has been priced or built, and the build-path work in the Build Guide is JMOD and SKRAM only.

### Dimensions and weights

- One SKRAM: 610 W × 914 H × 813 D, about 70 kg finished with a 21DS115.
- One two-high SKRAM stack: 1,828 mm. With a JMOD on top, 2,298 mm. With a 300–500 mm pole or stub, 2.6–2.8 m.
- A stack of two SKRAMs and a JMOD weighs about 175 kg. The upper SKRAM is lifted about 914 mm.

### Arrangements A and B

| | A · Two-high stack | B · Side-by-side pair + pole |
| --- | --- | --- |
| Footprint | 0.61 × 0.81 m | 1.22 × 0.81 m |
| JMOD height | Centre about 2.1 m, 2.3 m top (more with a pole) | Centre about 2.1 m with a 1 m pole on one cab |
| Lifting | Upper cab to 914 mm, \~70 kg | Floor level only |
| Stability | Tall and heavy: needs straps, locating hardware, wind limits | Lower centre of gravity; pole load of 34 kg |
| Sub coupling | Good up to about 90 Hz (spacing under a quarter wavelength) | Good up to about 140 Hz |

Arrangement B avoids the heavy overhead lift and the height. Arrangement A is compact on stage. Either way, plan a socket plate on the SKRAM top that takes the JMOD's external cup, so the JMOD moves between a stand and a sub without modification. Get a rigger or an experienced stage crew to sign off on how any stack is strapped before the first event.

### Genre fit

For IDM, techno, house, UK garage, UK dubstep and UK techno this is the right kind of rig, with moderate confidence. I found no independent measurements of SKRAM or JMOD and have not heard either. The JMOD figures below are the designer's own, read off his charts (about ±2 dB).

What fits:

- **Sub range.** With all four vents open SKRAM is tuned to 29.5 Hz, and builders describe usable output from roughly 20 to 120 Hz (forum accounts, not measurements). Techno and house kicks sit around 45–65 Hz and garage and dubstep bass lines around 35–60 Hz, inside that range. Leave the vents open by default, close them only for programme with real content below about 30 Hz, and keep a 25–30 Hz high-pass on. This is my reasoning from how vented boxes behave, not designer guidance.
- **Tops.** JMOD is a point-source three-way with 90° × 60° pattern control (horizontal to 320 Hz, vertical to 500 Hz) from 80 Hz to 18.5 kHz. That suits clarity-first genres: hats, vocals, fine detail and a consistent tone across the floor.
- **Headroom.** JW's chart puts one JMOD at about 121 dB at 3% distortion and 129 dB at 10% around 80–100 Hz, and about 130 dB across 200 Hz–1 kHz.

What could disappoint:

- **Mid-bass punch, 80–200 Hz.** Garage, dub and UK techno lean on this band. Here two 12-inch drivers per JMOD carry it while the SKRAMs are tuned to sound big below 80 Hz, so in a large room the subs will outrun the tops. JW himself suggests dedicated bass bins up to about 160 Hz for the best use of the bandwidth. If 80–160 Hz feels thin once tuned, the fix is more JMODs or bass bins, not more SKRAMs. Do not pre-buy either.
- **Scale.** For a few hundred people indoors, two SKRAMs and two JMODs should already have ample output. At larger or open-air events the JMODs reach their limit around 80–150 Hz before the subs do. Four SKRAMs still earn their place for weight at low drive levels.
- **Quiet material.** IDM and ambient expose noise. JW's sensitivity chart shows roughly 97 dB/W/m for the woofers and about 110 dB for the coax mid, so amplifier hiss is audible on horns this sensitive. Use the 16 Ω DCX464 as he advises, keep amp input gain low, and check each amp's noise floor and fan noise before buying.
- **Venue rules.** In Germany audience-exposure limits matter more than raw output. DIN 15905-5 (2007 edition) cited 99 dB(A) over 30 minutes and 135 dB(C) peak at the loudest audience position. A 2022 edition replaced it and I could not confirm its limits. Bass is lightly weighted in dB(A), so the subs are rarely the constraint, but a peak reading near the stacks can be. Check the permit conditions for each event.

### Stereo or mono

Recommended default: **stereo tops, mono subs.** The two-stack design already supports it, so it costs no hardware. Mono is only a switch: sum the DJ mixer's output, or feed both sides the same signal.

Why: bass in dance music is essentially mono and carries little directional information below about 100 Hz, so a summed low band avoids cancellation from out-of-phase low content. The tops stay stereo for width and detail. With 90° horizontal coverage and stacks a few metres apart, most of the floor hears both sides, and listeners off to the sides hear mostly the nearer stack. Some DJs prefer full-band mono in clubs for consistency at off-centre positions, so keep that option.

What it adds to the work:

1. **Routing.** L and R in; the tops get L and R high-passed at about 80 Hz; the subs get L+R low-passed at about 80 Hz. Do the sum in the DSP matrix or at the mixer. Confirm the chosen amp or processor can sum before buying: the outboard units in §04 and Powersoft's DSPs should, but I have not verified the Crown XTi.
2. **Presets.** One preset per stack, mirrored: same filters, delays and limits. Tune one stack fully with REW, copy it to the other, then verify.
3. **Measurement.** Per stack: JMOD bands to the published targets, the sub, then sub-to-top alignment, exactly as for mono. Stereo adds three checks, an hour or two in total: overlay the left and right stacks at the same mic distance (they should match within about 1 dB); play mono pink noise through both subs and confirm they add instead of cancelling (a polarity check); and listen at centre, left and right.
4. **Delays.** Nothing new if the mix position is equidistant from both stacks. If not, delay the nearer stack. The sub-to-top delay is the same on both sides.
5. **Layout, the real cost.** Two sub groups spaced across a stage and playing the same bass interfere with each other (the "power alley"): listeners off the centre line hear the two sides at different times, which carves notches that EQ cannot fix. Feeding both the same mono signal does not prevent this; the spacing causes it. The remedy is physical: keep the subs together.

### Arrangement C: centre sub cluster

All four SKRAMs together in the centre (a row of four, 2.4 m wide and 0.9 m tall, or a 2 × 2 block), with the JMODs on stands or poles left and right for stereo. The subs behave as one source, so low-end evenness is best, and a row needs no lifting above floor level. The costs are heavier-duty stands for the JMODs (rated well above 34 kg, not priced) and a per-side delay on each top so it lines up with the sub cluster at the mix position. The JMODs' external pole cups already allow this. Use A or B instead only if the room is small or the two stacks stay close together, a few metres at most. I found no firm spacing standard for dance-music clusters, so verify by measuring at the centre and at two or three off-axis positions.

| | A · Two-high stacks | B · Side-by-side pairs + pole | C · Centre sub cluster, JMODs on stands |
| --- | --- | --- | --- |
| Stereo tops | Yes | Yes | Yes |
| Sub interference | Two sub groups, spaced as far as the stacks | Same as A | One group: best |
| Lifting | Upper SKRAM to 914 mm | Floor only | Floor only (row of four) |
| Extra hardware | Socket plates, straps | Poles | Heavy-duty stands, per-side delays |

### Why four SKRAMs

- One design, one driver, one CAM set. SKRAM's CAM files are flat 2D and already exist, so pair 2 is repetition, not learning.
- Every sub is interchangeable, and every sub maps to the same amp load, so a failed cab or driver is a swap, not a re-patch.
- A 2:1 sub-to-top ratio suits a bass-led programme.
- Four subs share the work, so each runs well below its limits at a given level: cleaner bass and less compression. That is about headroom and cleanliness more than raw loudness, which venue rules may cap (see Genre fit).
- Pair 2 can be paid for and built after the rig is already working.

### What it costs

- Weight: four SKRAMs are about 280 kg, plus 68 kg of JMODs. A van is needed, not a car.
- Storage and transport for 16 sheets' worth of cabinets (610 × 914 × 813 mm each) needs a location before the build, not after.
- Lifting: two people per SKRAM at minimum; dollies or a lift for anything above floor level.

### Alternatives considered

- **A different or additional sub type.** Nothing found beats SKRAM as an open, available package. Josh Ricci's Othorn plans are reported as withdrawn. I could not verify whether Skhorn plans are public. A diyAudio thread, "SKRAM 20 smaller with 18", discusses a smaller 18″ variant that I did not read. Celestion's Scoop 18 kit and dual-21 plans are other leads I did not check. A fourth cabinet type also means new CAM, a new driver and a different amp mapping, with no evidence that SKRAM output is the limit.
- **Dedicated bass bins for 80–160 Hz.** The JMOD FAQ itself suggests them (kickbins crossed no higher than 200 Hz). Worth revisiting only if the rig lacks punch between 80 and 160 Hz once measured. Until then the JMOD's own 12-inch pair covers that range.
- **A smaller sub if weight bites.** Ricci's thread mentions a true half Skhorn at 24 × 32 × 27.71 in. It is a different design and not in the package.
- **Fewer subs for stage 1.** Two SKRAMs and two JMODs is the original plan, and it works. Pair 2 is optional.

No independent measurements of JMOD or SKRAM were found in this pass. The designers' own published measurements are the reference.

## 09 Solana

Deferred to a later phase. Not costed into the 2027 plan.

The Solana is JW Sound's compact 2-way point source — 4× 6.5″ B&C 6NDL38 around a 1″ DH450, in a 3D-printed algorithmically optimised waveguide. 90°×90° symmetric, 12.5 kg, crossing to subs at 100 Hz. Its role in this system is DJ booth monitoring, not front of house.

| Line | Per cabinet |
| --- | --- |
| 4 × 6NDL38 + 1 × DH450 | €530 |
| Plywood, ½ sheet 18 mm | €62 |
| PETG-CF, \~2.1 kg | €70 |
| Hardware, inserts, pole mount | €90 |
| Each | \~€750 |
| Pair | \~€1,500 |

Printing is the long-lead item: 2,533 cm³ of solid volume per cabinet, \~1.7 L of filament, and roughly 200–240 machine hours for a pair. Across five Core Ones that is 45–50 hours of wall clock. The waveguide prints as four quarters at 188 × 188 × 157 mm, which fits the Core One bed comfortably.

Trigger condition

Revisit when booth monitoring becomes a limiting factor at real events — not before. Nothing in the 2027 build depends on this decision, and the print files do not expire.

## 10 Decisions

Items that need resolving at this meeting. Everything else can wait.

1. #### Build order

   JMOD pair first, then SKRAM pair 1, then SKRAM pair 2.

   → JMOD first. Working system by March; cheaper, faster first phase.
2. #### Sub count

   Four SKRAMs in two stacks, or two SKRAMs as the baseline with the second pair as an option.

   → Four, built as two pairs. Stage 2 does not block first events.
3. #### SKRAM driver

   21DS115 (reference, lighter, cheaper) or 21SW152 (more power handling, heavier, lower sensitivity).

   → 21DS115.
4. #### Sub wiring

   One SKRAM per channel (8 channels) or two per channel (6 channels).

   → Follows the amp lane: one per channel with XTi 4002 or M50Q, two per channel with K3 or XTi 6002.
5. #### JMOD active or passive coax

   Tri-amp at 10 channels, or bi-amp with FB464 at 8 or 6. Sets the amp purchase.

   → FB464, accepting that the published mid/HF numbers need re-tuning (§05).
6. #### Amp lane

   A used Powersoft + outboard DSP, B new Crown with in-box DSP, or C new Powersoft install. Or wait for a DSP-equipped used Powersoft.

   → Not decided. Buy late either way.
7. #### Stack arrangement and stereo or mono

   Two-high stacks, side-by-side pairs with a pole, or a centre sub cluster with the JMODs on stands (§08). Stereo tops with mono subs is the recommended default.

   → **Decided 11 Oct 2026 for now: centre sub cluster, JMODs on poles, stereo tops with mono subs.** Side stacks that remove the poles are a later stage (§08); revisit before pair 2.
8. #### Contribution model

   Even split across 6–10, or weighted. €1,290–1,900 per person at 8, spread over twelve months but lumpy in practice.
9. #### Ownership

   Who owns the rig if someone leaves. Agree before the first order, not after.
10. #### Storage and transport

    Four SKRAMs are about 280 kg. Two-person lift per cabinet, van not car. Needs a location before build, not after.
11. #### Roles

    CNC and CAM, assembly, DSP and measurement, procurement. JMOD needs someone who can run Fusion CAM. Naming roles now prevents the tuning falling to whoever is left.

## 11 Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| JMOD toolpaths cannot be flattened to 2D | No DXF fallback; wrong post, stock or zero ruins sheets | Review the .f3d setups in Fusion, confirm the post for the makerspace router, cut a test piece, name a CAM owner |
| SKRAM metric conversion unverified | Dado errors compound across every joint, now four cabinets | Check RootDim against measured sheet thickness before any cutting; the CAM's Z zero is the spoilboard, so thickness errors show up directly as dado depth (Build Guide C5) |
| SKRAM CAM board width and sheet flip | The CAM is built for 1250-wide boards and mirrors the sheet when it flips; on a 1220 board the underside pockets land about 30 mm off the topside outlines, and the 12 mm nest does not fit | Buy 2500 × 1250 boards; set the stock width in all seven setups to the measured sheet width; add dowel registration; cut a test sheet |
| SKRAM CAM cutting depths | Sheet 2's outline and four pocket operations are set to cut full depth in one pass with a 3 mm cutter | Switch multiple depths on (about 5 mm steps) before running; simulate (Build Guide C5) |
| Alternative Makers capabilities and fees unverified | Schedule or budget surprise | Ask for fees, CNC rates, supervision and booking rules in phase 1 |
| Used amp quality or availability | No warranty; the private listings may be gone; EOL models have uncertain service | Buy from a dealer or with a test period; confirm the variant and Armonía support; consider lane B |
| No in-box DSP on cheap used amps | Driver damage from a user error with no limiter | Outboard DSP with real limiters (DriveRack-class); set conservatively; restrict who changes presets |
| FB464 route is not measured in the package | Published mid/HF targets do not map one to one | Measure and re-tune; keep tri-amp as a fallback; start the shared-channel limiters at 35 V RMS and 50 V peak (derived in the Sound Setup Guide §6.1) and leave the 3,450 Hz −7.5 dB PEQ out at first |
| Printed JMOD DSP settings contain errors | A builder who types the printed guide's values gets a 540 Hz mid boost and no 8 kHz filter | Use the .mdat values (640 Hz; 6 kHz +5 dB Q5; 8 kHz +2.5 dB Q2.5), confirm with JW, and measure |
| Pole-mounted JMOD tips over in wind | A 34 kg cabinet at about 2.5 m falls toward the audience; static estimate about 12 m/s (45 km/h) unballasted | Rated stand, ballast, guy lines, a working limit near 8 m/s gusts, a cordon, rigger sign-off (Build Guide D1) |
| Two-high stack stability | Tip or fall of a \~175 kg stack at 2.3–2.8 m | Strapping and locating hardware, wind limits, rigger sign-off; consider arrangement B |
| Lifting injuries | Upper SKRAM is \~70 kg at 914 mm | Team lift or lifting aid; arrangement B avoids it |
| Two separated sub groups playing the same bass | Uneven bass across the floor; notches EQ cannot fix | Keep subs together (arrangement C or close stacks); measure at several positions |
| JMODs run out of headroom at 80–150 Hz in big rooms | Thin or compressed mid-bass at high level while the subs are comfortable | Match the rig to the room; add JMODs or bass bins later, not more SKRAMs |
| Amp hiss and fan noise on quiet material | Audible on sensitive horns in IDM or ambient sets | 16 Ω DCX464, low amp input gain, check noise floor before buying, keep amps away from the audience |
| Audience-exposure limits | Permit conditions (DIN 15905-5 in Germany) cap level or peaks near the stacks | Check each venue's conditions; set DSP limiters accordingly |
| Plywood price/specification | Makerspace: €3,020.25 original nests; €2,237.22 full batch re-nest; €2,712.63 conservative staged route; VAT unconfirmed | Compare delivered quotes and manufacturer specs; buy to the selected validated nest |
| Plywood quality for CNC | Voids or mixed cores affect dados and the 3D flares | Specify birch throughout and void-free; inspect before cutting |
| B&C stock and lead times | DCX464 and 21″ drivers are not always immediate in EU | Order at phase start, not phase end; confirm stock before committing to dates |
| Imperial hardware in SKRAM spec | 10-32 and ¼-20 inserts not EU stock | Substitute M5 / M6; adjust hole sizes in CAM |
| Stand ratings | 40 kg stand under a 34 kg cabinet (K&M 21436); the K&M 21435 is listed at 50 kg by one retailer only | Confirm the rating with K&M; use the steel 21435 or heavier, ballast it, and ask the pole-flange maker for its rated load (Build Guide B11, D1) |
| Tuning skill concentrated in one person | Rig unusable if they are away | Two people through the REW workflow from phase one; back up amp and DSP presets |
| CNC booking capacity for 19 sheets | Schedule slip | Book blocks in advance; one block per pair |

Costs are estimates for discussion, not quotes. Everything in §02 and §04 should be re-quoted locally before any order is placed.

## 12 Verified and open checks

### Checked in the design packages

SKRAM orientation and part sizes (STEP); SKRAM geometry type and CAM file count; JMOD CAM contents (6 setups, 18 operations, tools) and freeform geometry; filament ratings; the pole-mount note; the 3.6 kHz FB464 split against the published DSP; the .mdat's contents.

**Added on 11 Oct 2026, read directly from the files** (not simulated or cut): the filter sets and trace notes inside the .mdat, rebuilt and compared with the file's EQ'd traces; the JMOD STEP's per-part sizes, stock bodies (4 × 8 ft) and hole schedule, and the throat adapter's four Ø6.6 mm mounting holes on a Ø102 mm circle; the JMOD CAM's tools, speeds and setups; the throat-adapter STL (169.9 × 120.0 × 90.0 mm, 438 cm³); all three SKRAM CAM files (stock 2500 × 1250 mm, one 3 mm cutter, valid or invalid toolpaths, parameter differences, depth settings); the SKRAM STEP part sizes, the 2019 DXFs (inches; baffle with 8 driver holes on a Ø527 mm circle; hatch with 18 fasteners) and the parametric spreadsheet's parameter names; and the wiring diagrams on guide pages 21 and 22.

### Checked on the web, 09 Oct 2026 (dealer listings and Powersoft's own pages; prices change)

- Powersoft: [X4](https://www.powersoft.com/en/products/touring-amps/x-series/x4), [K3 end-of-life page](https://www.powersoft.com/en/products/touring-amps/k-series/k3/), [Quattrocanali 4804 DSP+D at Sonovente](https://www.sonovente.com/powersoft-amplificateur-avec-dsp-et-dante-p105648.html), [Quattrocanali 2404 DSP+D at Huss Licht & Ton](https://www.huss-licht-ton.de/print_product_info.php/en/products_id/39213)
- Used Powersoft: [X4 at 10kused](https://www.10kused.com/?p=123355), [M50Q ad](https://radar.stereonet.com/listing/47757-powersoft-m50q-4-kanal-class-d-touring-endstufe), [K3 ad](https://radar.stereonet.com/listing/47760-powersoft-k3-ohne-dsp-2-kanal-touring-endstufe-3x-verfugbar), [M28Q ad](https://radar.stereonet.com/listing/47755-powersoft-m28q-4-kanal-class-d-endstufe-1he)
- Drivers: [21DS115](https://www.thomann.co.uk/bc_21ds115.htm), [21SW152](https://www.thomann.co.uk/bc_21sw152.htm), [21SW152 8 Ω at Toutlehautparleur](https://en.toutlehautparleur.com/speaker-b-c-speakers-21sw152-8-ohm-21-inch.html), [21NLW9601 at Bax](https://www.bax-shop.co.uk/21-inch-speakers/18-sound-21nlw9601-21-inch-bass-speaker-1800-w-8-ohms)
- Other: [FB464 at Sonovente](https://www.sonovente.com/en-gb/b-and-c-crossover-464-16-ohms-p93207.html), [Crown XTi 6002 at Bax](https://www.bax-shop.co.uk/amplifiers/crown-xti-6002-amplifier), [Crown XTi 4002 price comparison](https://www.guenstiger.de/Produkt/Crown/XTi_4002.html), [Hornbach birch plywood](https://www.hornbach.de/s/Birke), [K&M 21436 at Kirstein](https://www.kirstein.de/en/Live-Studio/Accessories-Live-Studio/Speaker-Stands/K-M-21436-Speaker-Stand-Aluminum.html)

### Added in the second pass, 09 Oct 2026

[Lavoce SAN214.50 at Steinigke](https://steinigke.de/en/mpn12602637-lavoce-san21450-4-21-subwoofer-neodymium-magnet-aluminium-basket-driver.html), [subwoofer interactions and the "power alley" (ProSoundWeb)](https://www.prosoundweb.com/subwoofer-interactions-avoiding-the-power-alley/), [the power alley (Fulcrum Acoustic)](https://fulcrum-acoustic.com/education/the-power-alley-a-k-a-troubling-interactions-of-subwoofers), [DIN 15905-5 listing](https://www.din.de/en/standard/din-15905-5/101214193). JMOD distortion-limited SPL, sensitivity and directivity are read from pages 5–6 of the JMOD guide.

### Checked on the web, 11 Oct 2026

[B&C DCX464 16 Ω](https://www.bcspeakers.com/en/products/coaxials-hf/1-4/16/DCX464-16), [FB464 16 Ω](https://www.bcspeakers.com/en/products/crossovers/0/16/FB464), [12NDL88](https://www.bcspeakers.com/en/products/lf-driver/12/8/12NDL88) and [21DS115](https://www.bcspeakers.com/en/products/lf-driver/21/8/21DS115) (ratings, mounting dimensions; the DCX464 and 21DS115 bolt circles); [FB464V2 16 Ω at Toutlehautparleur](https://en.toutlehautparleur.com/2-way-fb4648v2-crossover-for-b-c-speakers-dcx464-and-dcx462-16-16-ohm-3600-hz-18-12-db-octave-more-power-handling-without-light-bulb-protection.html); [JW Sound: SKRAM](https://www.jwsound.live/designs/riccis-skram-subwoofer), [SKHORN](https://www.jwsound.live/designs/riccis-skhorn-subwoofer), [SAWMOD](https://www.jwsound.live/designs/sawmod), [JMOD-M](https://www.jwsound.live/designs/jmodm-medium-format-array), [DH350 MEH](https://www.jwsound.live/designs/dh350based-multiple-entry-horn); Powersoft [M50Q](https://www.powersoft.com/en/products/touring-amps/m-series/m50q/) and [K3](https://www.powersoft.com/en/products/touring-amps/k-series/k3/) pages; Crown XTi, dbx DriveRack 4800 and miniDSP Flex Eight feature pages (sources in Sound Setup Guide §D); [K&M 21435, 21436 and 21459 at Canford](https://www.canford.co.uk/Products/53-3660_K&M-21459-LOUDSPEAKER-STAND-Pair-with-carry-case-black); pole-flange listings (Adam Hall SM 700, K&M 195/8, RCF AC-TT-PMA, Gravity GSF36M10M); [Penn-Elcom H1105](https://parts-express.com/Penn-Elcom-H1105-Recessed-Steel-PA-Cabinet-Handle-260-705); EU tee-nut bore sizes; [Neutrik NL8MPR cutout drawing](https://www.farnell.com/cad/3475533.pdf). Owner reports on SKRAM high-pass settings came from search-result summaries only; the AVS Forum pages themselves were not opened.

### Not verified

**23 October material update:** member-portal sheet and consumable prices are supplied, but VAT, stock, manufacturer/core/glue specification, bulk discounts, reservations and external-sheet handling remain open. The portal Ø3 mm bit is only 17 mm cutting length (€23.57), so it is not the saved SKRAM cutter for 18 mm through-cuts; verify suitable tooling. Discs are €0.70 each. Membership/machine fees remain open. See the sourcing review for web evidence.

Alternative Makers' equipment, fees and booking rules; that either CAM runs on the makerspace's router and post (nothing was simulated or cut); whether current Armonía software supports every K and M-series variant; Powersoft service for end-of-life models; current status and condition of the May 2026 private ads; Crown XTi 4002 and 6002 live prices and weights; DCX464 VAT basis (the Sonovente page would not open); pole-flange ratings and prices; the K&M 21435's rating (one retailer says 50 kg, K&M's own page was not read); independent SPL or response measurements for SKRAM or JMOD (the JMOD figures in §08 are the designer's own, read off a chart, and I found no SKRAM output figure at all); the SKRAM subsonic filter beyond owner reports; JW's hardware preset versus the .mdat filters; the limit values in the 2022 edition of DIN 15905-5; whether each amp's DSP can sum left and right for the subs (not verified for any candidate); the Crown XTi, Powersoft K3 DSP and miniDSP 4x10 HD limiter and filter details beyond the retailer and product-page summaries; trade prices for birch plywood; what "Paraflex type O" is.

SKRAM · Josh Ricci, files by Tinker & Party · JMOD 2.02 & Solana 2.0 · John White, JW Sound · Build plan v3, 11 Oct 2026
