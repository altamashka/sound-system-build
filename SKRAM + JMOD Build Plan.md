Working plan · 8 November 2026 · For group review

# Our sound system: start with one JMOD

Build one JMOD top first. If we are happy with it, add one SKRAM subwoofer for the low bass. Later we can decide whether to build a second JMOD and a second SKRAM.

## 1. First build: one JMOD

The JMOD is the main speaker. The planned parts for one are:

- Two B&C 12NDL88 drivers, **8 Ω** each.
- One B&C DCX464 compression driver, **16 Ω**.
- One B&C FB464 crossover, **16 Ω**, to match the compression driver. The standard FB464 has protective bulbs; the FB464V2 does not. Check which is available.
- Uncoated birch plywood, a 3D-printed throat adapter, handles, speaker connectors, internal wire, fasteners, gasket, adhesive and finish.

The designer's layout for **two** JMODs uses two sheets of 12 mm and one sheet of 18 mm birch. We have not confirmed a smaller cutting layout for one. The current one-cabinet estimate of **€1,770–1,850** includes all three sheets, drivers, crossover and the listed cabinet materials. It excludes amplification, cables, measurement equipment, workshop fees and delivery. These are estimates, not quotes; wood prices and VAT need checking. See the [wood sourcing review](Wood%20sourcing%20review.md).

### Build it

1. Use the local `JMOD 2.0 DIY Package` folder for the designer's instructions, cutting files and 3D-print files. The package is not included in GitHub; on another device, get it from the [designer](https://www.jwsound.live/designs/jmod).
2. Check sheet size, actual thickness, machine access and cutter suitability at Alt Makers. Review and simulate the cutting files for the actual machine, then make a test cut before cutting the sheets.
3. Print the throat adapter in a material recommended by the designer and check that the driver fits. He reports using PETG-CF or PETG-GF with 50% infill; check that the workshop printer supports the chosen material. [Designer’s print advice](https://www.diyaudio.com/community/threads/jmod-v2-build-thread.429672/page-6) The designer says an **experimental cone filler** present in some files is not needed; this is a different part from the required throat adapter. [Designer’s clarification](https://www.diyaudio.com/community/threads/jmod-v2-build-thread.429672/page-9)
4. Label the cut parts and dry-assemble the whole cabinet with clamps. John White emphasises that getting this first fit right matters. [Designer’s build photos](https://www.diyaudio.com/community/threads/jmod-v2-build-thread.429672/)
5. Follow the designer's assembly order. Glue, clamp and seal the joints; keep the horn surfaces smooth and the driver seats airtight. Fit the drivers, matching crossover, connectors and gaskets. Check the wiring and polarity with the power off.
6. Have an experienced person check the wiring, amplifier settings and driver protection before playing it. Measure and tune the finished cabinet; a microphone alone does not set protection.

## Sound and amplification

For the planned **bi-amped** setup, one amp channel powers the two 12-inch drivers and a second powers the compression driver through the FB464. The FB464 splits only the compression driver's two sections. We still need electronic processing to divide and tune the sound between the 12-inch drivers and the compression driver. [Designer’s explanation](https://www.diyaudio.com/community/threads/jmod-v2-build-thread.429672/page-6)

A four-channel amp with suitable built-in processing could power one JMOD now and two in stereo later. The **CVR DSP-1504 with Dante** is a candidate, not a confirmed purchase: its filters and limiter behaviour for this exact setup still need verification. Allow for an external processor if necessary. A SKRAM needs its own amp channel and processing; with two JMODs using all four channels, the sub needs another amp. Amp brands can be mixed.

Budget separately for a calibrated measurement mic, signal cables, a correctly wired four-pole speaker cable, and a rack patch panel or breakout if needed to bring the two amp channels to one JMOD cable. The designer describes this arrangement in the [build thread](https://www.diyaudio.com/community/threads/jmod-v2-build-thread.429672/page-6). The [sound setup guide](Sound%20Setup%20Guide.md) covers measurement and operation.

## Cost overview

**Planning figures, 8 November 2026.** These are estimates for discussion, not quotes. The example uses the CVR DSP-1504 with Dante and assumes we already have a laptop and a music source.

### First JMOD: ready to make sound

| Item | Allowance |
| --- | ---: |
| JMOD cabinet, drivers, crossover and materials, including all three plywood sheets | €1,770–1,850 |
| CVR DSP-1504 with Dante | €1,505 |
| Calibrated [UMIK-1 measurement microphone](https://www.md-sound.de/MiniDSP-UMIK-1-Plug-Play-USB-Messmikrofon-Neu) | €124 |
| [USB audio interface](https://www.thomann.de/de/behringer_u_phoria_umc202hd.htm) for sending sound from the laptop | €60 |
| Speaker and signal cables, amp breakout or patch connections | €150–250 |
| Extra allowance if the throat adapter is printed by a service | €0–125 |
| Workshop, test cuts and delivery allowance | €150–350 |
| **Estimated first stage** | **€3,759–4,264** |

| Split equally | Cost per person, rounded up |
| --- | ---: |
| 3 people | €1,253–1,422 |
| 4 people | €940–1,066 |
| 5 people | €752–853 |

The amp price is based on the [seller's listing](https://www.kleinanzeigen.de/s-anzeige/cvr-audio-amplifier-pa-bass-system-endstufen/3071907788-172-5829): €1,264.47 **excluding VAT**, or approximately €1,505 at 19% German VAT; delivery and current availability are not confirmed. It is a budget candidate, not a verified system: if its processing or protection is unsuitable, an external processor or different amp will add cost. The cable allowance includes a [four-core speaker cable](https://www.thomann.de/de/cae_14720_5m_speakon.htm) and a suitable way to combine the two amp outputs; actual connections depend on the amp. The cabinet estimate already allows for materials and filament; the extra print line is a provisional allowance for outsourcing, not a quote. Workshop, delivery and cable figures are allowances, and the wood price's VAT basis remains uncertain. Professional setup, a rack and a laptop are not included. REW software is free.

### Possible expansion

These are **additional** costs after the first stage; they reuse the amp, measurement kit and any suitable wood left from the first JMOD.

| Next step | Extra for the group | Assumption |
| --- | ---: | --- |
| Add one SKRAM | €1,430–1,540 | €1,400–1,480 cabinet estimate plus €30–60 for a cable. A spare DSP-1504 channel may be usable, but its power and protection for the sub are not verified; a separate sub amp could be needed sooner. |
| Add the second JMOD | €1,370–1,560 | Roughly the first cabinet estimate minus the €447 already budgeted for all three sheets, plus €50–150 for cable and connections. Only works if the retained wood suits the second build; no extra amp is assumed. |
| Add the second SKRAM and sub amp | €2,790–3,100 | Another SKRAM, a two-channel sub amp and cables. Includes about €1,363 for a CVR DSP-3302 **without Dante**, based on the same seller's €1,145.58 before VAT; suitability and actual price remain unverified. |

If those assumptions work, **two JMODs and two SKRAMs total roughly €9,350–10,465**, including the first stage: about **€3,117–3,489 each for 3**, **€2,338–2,617 each for 4**, or **€1,870–2,093 each for 5**. Future workshop, delivery, placement hardware and any extra processing are not included. These figures are for deciding the scale of the project, not collecting money yet.

## 2. Next: one SKRAM

If the group agrees after the first JMOD, build one SKRAM with one B&C **21DS115, 8 Ω** driver. The existing estimate is **€1,400–1,480** for its cabinet, driver and fittings, excluding amplification and the other costs above. The supplied one-cabinet cutting layout uses three sheets of 18 mm and one of 12 mm birch; alternative layouts have not been verified. Use the local `SKRAM DIY Package` folder, or get [Josh Ricci’s SKRAM files](https://www.jwsound.live/designs/riccis-skram-subwoofer) on another device. Check the actual stock and machine setup, simulate and make a test cut, then dry-fit before assembly.

## 3. Possible next step

A second JMOD would give us stereo tops; a second SKRAM would add bass capacity. Decide on these after using and costing the first two cabinets. There is no commitment to a bigger system yet.

## What we need to do now

1. Agree who is involved, how costs and ownership are shared, and the initial budget.
2. Obtain the JMOD files and check the one-cabinet cutting plan, 3D print, workshop access and storage.
3. Refresh the prices and complete the shopping list, including the amp, cables and measurement kit; bring the full cost to the group before ordering.
4. Resolve the amplifier processing and protection, then build and check the first JMOD.

JMOD is designed by John White / JW Sound; SKRAM is designed by Josh Ricci. Follow the licences in the designer files. No purchases or workshop bookings have been made.
