Working guide · v2 draft · 11 Oct 2026 · For collective review

# Sound Setup Guide

How to measure, align, limit and operate the SKRAM + JMOD rig. Written for people who already mix, produce, DJ or run sound, but have not set up a multi-amped system of passive cabinets before. It is brand-neutral: processors, amps and measurement software appear only as examples.

Read §0 and §1 before the meeting. §2 is the buyer's checklist for the processor and amps. The rest is the procedure you follow once the cabinets exist. The cabinets themselves are built from the [Build Guide](Build%20Guide.md); the budget and decisions are in the [SKRAM + JMOD Build Plan](SKRAM%20+%20JMOD%20Build%20Plan.md).

**What changed in v2 (11 Oct 2026)**

- **Two JMOD settings were wrong in v1, and the printed guide is the cause.** I opened the REW file that ships with the JMOD package and read the filter sets it stores. The mid-band boost is at **640 Hz, not 540 Hz**, and the high band has **two** boosts, **6,000 Hz +5.0 dB Q5.0 and 8,000 Hz +2.5 dB Q2.5**, not the single "6000Hz +2.5dB Q?" in the guide, whose Q is cut off. Rebuilding the filters and comparing them with the file's own EQ'd traces confirms it (§6.2). This closes the "missing Q" open item and corrects it.
- **Shared-channel (FB464) limiter values are now derived, not guessed** (§6.1, §7.2 example 5), using B&C's official DCX464 ratings.
- **SKRAM subsonic filter** now has evidence behind it: owner-reported settings, and a corner of about 27 Hz for the all-vents-open case instead of 30 Hz (§6.3). It is still a start value.
- **Processor candidates have been checked** against the requirements in §2. The result matters: the Crown XTi has no RMS limiter and no 12 dB Linkwitz–Riley filter; non-DSP used Powersofts have no tunable limiters.
- **Arrangement C is now the baseline**: sub cluster in the centre, JMODs on poles left and right (§9.7, §10.3, §14.1).
- The NL8 tri-amp pin assignment is confirmed from the wiring diagram (§1).

[**0** Orientation](#s0) [**1** How the system works](#s1) [**2** What the sound side needs from the purchase](#s2) [**3** Concepts](#s3) [**4** Kit](#s4) [**5** Before power](#s5) [**6** Build the processor template](#s6) [**7** Gain structure and limiters](#s7) [**8** Measuring a cabinet](#s8) [**9** Aligning subs to tops](#s9) [**10** Stereo and mono](#s10) [**11** Verifying limiters](#s11) [**12** Tuning in a venue](#s12) [**13** Document, back up, lock](#s13) [**14** Event day](#s14) [**15** Troubleshooting](#s15) [**A** Worksheets](#sa) [**B** Quick maths](#sb) [**C** Glossary](#sc) [**D** Sources and open checks](#sd)

## 0Orientation

### What this guide is, and is not

It is a procedure, with the reasoning behind each step, for taking six or more cabinets and a pile of electronics from "plugged in" to "measured, safe and repeatable". It is not a substitute for the manufacturers' manuals for the amplifiers and processor we eventually buy. Where a step depends on a menu, it says what to find, not where to click.

### How much to trust each number

Every setting in this guide carries one of three tags.

| Tag | Meaning | What to do |
| --- | --- | --- |
| **[Published]** | Taken from a designer's or manufacturer's document for exactly this hardware | Enter it, then confirm by measurement |
| **[Calculated]** | Worked out from published ratings with a formula shown here | Recheck against your actual amps |
| **[Start]** | A sensible starting point from general practice, not from the designers | Treat as a guess until measured |

Nothing in this guide has been run on our own hardware yet. Anything marked [Start] is where the first session should spend its effort.

### The twelve-step route

1. Decide the signal architecture: channels, stereo or mono, which processor (§1, §2).
2. Build the processor template offline, at a desk (§6).
3. Calculate and enter the limiter values (§7).
4. Bench-check the amplifiers with the speakers disconnected (§7).
5. Wire and verify each cabinet before any power (§5).
6. Set gain structure and check the noise floor (§7).
7. Measure each cabinet alone, outdoors if possible, and compare with the designers' data (§8).
8. Align the subs to the tops (§9).
9. Verify the limiters behave as intended (§11).
10. Copy to the second stack, match, and check stereo and polarity (§10).
11. Tune in a venue, minimally, then document, back up and lock (§12, §13).
12. Follow the same short routine at every event (§14).

Expect the first full pass to take most of two days with two people (my estimate, not a measured figure). After that, an event setup should take well under an hour.

### Safety, before anything else

- **Hearing.** NIOSH's recommended limit is 85 dBA for 8 hours, and every 3 dB higher halves the permitted time: 94 dBA for 1 hour, 100 dBA for 15 minutes, 106 dBA for under 4 minutes. A single measurement sweep is short, but a long session near a stack is not. Wear hearing protection whenever you are in front of the cabinets at test levels, and keep every test at the lowest level that gives a clean measurement.
- **Gear.** Disconnect speakers whenever the procedure says to. Bench tests that drive an amp to full voltage will destroy a connected driver. Long sweeps and loud pink noise can overheat compression drivers.
- **People.** Agree a "stop" word before you start. The person at the laptop is usually not the person next to the cabinet.
- **Lifting and stacks.** See the build guide and §8 of the plan. Never work under a stack.

## 1How the system works

### Passive cabinets, active signal chain

Our cabinets contain only drivers, no amplifiers and no crossovers. The "active" part is the chain in front of them: a processor does the crossover, EQ, delay and limiting, and a separate amplifier channel feeds each band. This is called multi-amping or an active system, even though the cabinets are passive. The cabinets are only as safe and as good as the processor settings in front of them.

```
Source (DJ mixer, laptop)  →  Processor  →  Amplifier channels  →  Speaker cables  →  Cabinets
 L / R, balanced line          crossover       one channel per         Speakon           SKRAM subs
                               EQ, delay       band or per sub                           JMOD tops
                               limiters
```

The processor may be an outboard unit or built into the amplifiers. This guide assumes only that, somewhere in the chain, every amplifier channel has its own filters, delay, EQ and limiters.

### What each device is responsible for

| Device | Does | We set |
| --- | --- | --- |
| Mixer or source | Provides a clean line-level stereo signal | Master level at nominal, no clipping |
| Processor | Splits bands, aligns, equalises, limits | Everything in §6 and §7 |
| Amplifier | Makes the signal big | Gain or sensitivity, and nothing else |
| Cable and connectors | Delivers voltage to the right driver | Pinout, polarity, gauge |
| Cabinets | Turn voltage into sound | Nothing; they are the thing being protected and measured |

### Channels per stack

The working layout is **Arrangement C**: the SKRAMs together in a centre cluster and a JMOD on a pole on each side (§10.3). "Stack" in this guide therefore means one side: one JMOD with its two amplifier channels, plus its share of the sub cluster. The plan allows two wiring routes for the JMOD coax. The bi-amp route uses a passive crossover (the B&C FB464) and is the working assumption.

**JMOD, bi-amp route (4-pole Speakon).** [Published]

| Channel | Speakon pins | Drives |
| --- | --- | --- |
| JMOD LF | 1+ / 1− | Two 12-inch woofers in parallel |
| JMOD coax | 2+ / 2− | The FB464 input, which splits the coax driver's mid and high sections |

**JMOD, tri-amp route (8-pole Speakon).** [Published] Pins 1± carry the woofer pair, 2± the DCX464's mid (outer ring) section, 3± its HF (inner dome) section, and 4± is spare. I traced this on the guide's page 22 diagram: 1± goes to both 12NDL88 in parallel, 2± to the outer ring of the coax symbol and 3± to the inner circle. On page 21 (bi-amp) the FB464's W terminals feed the same outer ring and its T terminals the inner dome. Build the cables from the diagram rather than from this table if the two ever differ.

**SKRAM.** One amplifier channel can drive one sub or, with 8 Ω drivers in parallel, two. Which one depends on the amplifier choice (see §2).

**Stereo.** The left stack and the right stack are identical and have their own amplifier channels. Whether they receive left and right, or the same signal, is a routing choice made in the processor, not a hardware difference.

## 2What the sound side needs from the purchase

For the meeting. These are the capabilities the procedures in this guide rely on. If a candidate processor or amplifier lacks one, either decline it or plan a workaround.

### Processor (outboard, or built into the amps)

| Requirement | Why we need it | Notes |
| --- | --- | --- |
| At least 6 outputs, ideally 8 | One per amplifier channel (§1) | Fewer if some amps have their own DSP |
| Crossover filters per output: Butterworth and Linkwitz–Riley, slopes at least 12, 18 and 24 dB per octave, **including a 12 dB Linkwitz–Riley (LR2)** | JW's settings use LR4, **LR2** (the woofer low-pass at 195 Hz), BU3 and BU2 | Check that the slope is selectable per output, not fixed. Some processors offer LR only at 24 dB and above; an LR2 can then only be approximated with biquads |
| Per-output parametric EQ, at least 4 bands | The mid band alone needs 3 PEQs, the high band 2 | More is better |
| Per-output delay, resolution 0.01 ms or finer, range at least 20 ms | Sub-to-top alignment and the 0.22 ms and 0.4 ms values | Larger range helps if stacks are far apart |
| Per-output polarity invert | The published HF setting is inverted | Alignment also needs it |
| Per-output **peak limiter** and **RMS (thermal) limiter**, each with threshold, attack and release | JW publishes both, per band | A compressor alone is not a substitute; see §3.6 |
| Limiter thresholds in volts, or an amp-gain entry, or a clear dBu/dBFS map | §7 converts volts to processor units | Without any of these you are guessing |
| Input matrix or mixer: sum left and right to subs, route left and right to tops | Stereo tops, mono subs (§10) | Or sum at the mixer instead |
| Balanced analogue outputs | Long cable runs and low hum | Unbalanced outputs need adapters and care |
| Store, recall, lock and export presets | §13 | Export to a file that can be emailed or backed up |
| Level metering per output | Gain structure and clip checks | Front-panel or software |

**Candidates checked against the table (11 Oct 2026).** I went to the manufacturers' pages and spec sheets where I could. Where a manual would not load, the row says so rather than guessing.

| Candidate | Limiters | LR2 (12 dB LR) | Other findings | Verdict |
| --- | --- | --- | --- | --- |
| **Crown XTi 4002 / 6002** (in-box DSP) | **Peak limiter only** ("Peak X Plus": threshold, attack, release). **No RMS / thermal limiter is listed** | **No.** Butterworth 6/12/18/24; Linkwitz–Riley 24 and 48 only | PEQ 6 input + 8 output bands per channel (4002 listings); delay up to 50 ms; HiQnet software. L+R summing not verified | Usable for the sub channels. For the JMOD it cannot do the LF low-pass exactly (LR2) and cannot do an RMS limiter. Retailer data, not the manual |
| **Powersoft M50Q and K3, no DSP** | Built-in **clip limiter** and **"long term" limiter** (protects against steady non-audio signals). Not user-set, not tied to your drivers' ratings | n/a | Both are marked End of Life on Powersoft's own pages | **Not driver protection.** A used non-DSP Powersoft needs an outboard processor with real limiters |
| **Powersoft M-series DSP variant** (M50Q HDSP+ETH) | **Peak, RMS and frequency-dependent RMS limiters** per the datasheet summary I could reach | Not verified | The ETH/HDSP variant is the one with DSP; EOL | Meets the limiter requirement. Filter list not verified |
| **Powersoft K3 DSP** | KDSP board exists; its limiters not verified from a primary source. A user review says limiter thresholds no longer depend on amp gain when DSP is integrated | Not verified | The K3 page names ArmoníaPlus for the DSP+AESOP version only and does not say support continues for end-of-life units | Plausible; verify before buying |
| **dbx DriveRack 4800** | **PeakStopPlus limiting** and a compressor on output inserts. No RMS / thermal limiter is documented | **Yes** (LR 12/24/36/48) | 4 in / 8 out; outputs have a 6-band parametric EQ; delay up to 680 ms | Meets the filter and peak-limiter needs. Use a slow compressor as the RMS stand-in and check its attack range |
| **miniDSP Flex Eight** | **Per-output compressor**, no limiter in the product spec. Not documented as a brick-wall limiter | Via biquads | RCA outputs, about 2 V RMS maximum; the displayed "+12 dB" output is 0 dBFS, so unity is −12 dB: thresholds are easy to misread | A compressor can stand in, but needs care and a bench check |
| **miniDSP 4x10 HD** | **Could not confirm** | Not confirmed | Balanced outputs on terminal blocks | Do not count on it until the manual says so |

Conclusions that change the shopping list: (1) a Powersoft is only worth its price here if it is a **DSP variant**; (2) if the Crown XTi is chosen, plan the JMOD LF channel's low-pass as a biquad approximation of LR2 and the RMS protection as a procedure plus a conservative peak limit; (3) the cheap outboard route is the DriveRack, which has the filters and a peak limiter but not a documented RMS limiter. In every case the limiter must be **bench-checked** with the amp (§7.3, §11). Check the feature list against the table above before buying, not after.

### Amplifiers

| Requirement | Why | Notes |
| --- | --- | --- |
| Stated voltage gain in dB, or stated input sensitivity | §7 depends on it | If only a multiplier is given, convert it (×40 is 32 dB) |
| Output power into the loads we will use (4 Ω for woofers and subs; 16 Ω or 8 Ω for the coax via the FB464) | Limiter ceilings | Use the continuous rating, not a peak figure |
| Clip indicators, preferably with a switchable clip limiter | Detect headroom problems | |
| Input attenuators or a sensitivity control per channel | Gain structure | |
| Low noise floor and quiet fans | IDM and ambient material expose hiss (see the plan, §08) | Check with the speakers on, source muted |
| Stable into 4 Ω, per channel | Two 8 Ω woofers in parallel is 4 Ω | Lower impedance dips happen; check the amp's 2 Ω rating if it has one |

### Two decisions that change the procedure

1. **Amps with built-in DSP, or an outboard processor.** With built-in DSP, §6 and §7 happen in each amp's own software, usually with limiters that already know the amp's gain. With an outboard processor, you enter the gain yourself and everything depends on that number being right.
2. **One sub per channel, or two.** Two per channel halves the number of channels and limiter sets, but a limiter event affects both subs, and the limiter ceiling must be chosen for the pair.

## 3Concepts

Each subsection is short. Skip anything you already know cold.

### 3.1 Levels, units and headroom

- **dBu** is a voltage level referenced to 0.775 V RMS. **dBV** is referenced to 1 V RMS. **dBFS** is a digital level referenced to the largest value the converter can represent. **dB SPL** is a sound pressure level referenced to the threshold of hearing.
- Conversions: dBu = 20·log₁₀(V / 0.775). So 0 dBu = 0.775 V, +4 dBu = 1.23 V, +20 dBu = 7.75 V.
- A converter's analogue full scale is stated in its specification as "0 dBFS = +X dBu". Typical professional values are +18 to +24 dBu. You need this number to convert a processor's digital level into a voltage at the amp input.
- **Headroom** is the distance in dB between your normal level and the point where something clips. Music has peaks well above its average level. The ratio between peak and RMS is the **crest factor**: a sine wave has 3 dB, the pink noise used in speaker-rating tests has 6 dB, and real dance music often has 12 dB or more before mastering compression.
- A voltage ratio of 2:1 is 6 dB, and power goes as voltage squared, so +6 dB is four times the power, +3 dB twice the power.

### 3.2 What a speaker's power rating means

B&C (the maker of our drivers) defines its figures as follows. **Nominal power handling** follows the AES2-1984 method: pink noise with a 6 dB crest factor, filtered to the driver's working band, applied for two hours, with the driver still working normally afterwards. **Continuous program power** is twice the nominal rating, and B&C recommends choosing an amplifier rated at the program figure so the amp does not clip. A 6 dB crest factor means the peaks are 2:1 in voltage, so four times the average power.

Two cautions. First, "AES" figures are an average power over hours, not a peak. Second, the method was revised in 2012 with a 12 dB crest factor, so figures from different brands and years are not strictly comparable. For our drivers we use B&C's published nominal and program figures.

### 3.3 Crossovers

A crossover splits the signal into bands, one per driver or cabinet. Two decisions define it: the **frequency** where the bands meet, and the **slope** at which each band rolls off.

- A **Butterworth** filter has the flattest passband and is 3 dB down at its corner frequency. Two Butterworth bands summed together peak by about 3 dB at the crossover frequency if their slopes are even-order.
- A **Linkwitz–Riley** filter (LR) is two Butterworth filters in series. It is 6 dB down at the corner and the two bands sum to a flat response with no peak. An **LR4** (24 dB per octave) has its low-pass and high-pass outputs exactly in phase, so no polarity flip is needed. An **LR2** (12 dB per octave) has them 180° apart, so one side needs a polarity flip.
- Naming varies by brand. "LR4" means a fourth-order filter, which is 24 dB per octave, and some units label the same thing "LR24". "BU3" is a third-order Butterworth, 18 dB per octave. Always check the unit's slope in dB per octave.
- **Electrical is not acoustic.** A driver and its enclosure add their own rolloff and phase shift. The filter you set in the processor is not the filter you hear. That is why the JMOD guide publishes *acoustic target curves* and a set of electrical filters that happen to produce them, and says explicitly that results depend on drivers, amps, DSP and assembly. The job is to shape the electrical filters until the *measurement* matches the target.
- **FIR and IIR.** IIR filters (the usual kind) are cheap and have latency near zero but change phase. FIR filters can correct phase but add latency. For a first system, IIR is fine and simpler to reason about.

### 3.4 Delay, polarity and alignment

These four words get confused. Keep them separate.

- **Polarity** is a simple flip of the signal, 180° at every frequency. It is a switch.
- **Phase** is the frequency-dependent timing offset between two signals, expressed in degrees. It changes with frequency.
- **Delay** is a fixed time offset, which appears as phase that grows linearly with frequency: a delay of Δt gives 360° × f × Δt of phase at frequency f.
- **Alignment** is choosing delay and polarity so that two sources are *in phase through their crossover region*, which is roughly half an octave either side of the crossover frequency.

When two equal sources are in phase they add. As they drift apart in phase the sum falls: at 30° apart you lose about 0.3 dB, at 60° about 1.2 dB, at 90° about 3 dB, at 120° about 6 dB, and at 180° you get a null.

The practical numbers at an 80 Hz crossover:

| Timing error between sub and top | Phase error at 80 Hz | Loss in the sum |
| --- | --- | --- |
| 0.5 ms | 14° | negligible |
| 1 ms | 29° | about 0.3 dB |
| 2 ms | 58° | about 1.2 dB |
| 3 ms | 86° | about 2.7 dB |
| 6.25 ms | 180° | complete null |

So alignment to within about a millisecond is plenty at 80 Hz.

**Which source gets the delay.** A horn-loaded or vented sub has a long internal path and a lot of group delay near its tuning, so its sound usually arrives later than a top's at the same distance. You cannot make a source earlier, so you make the *other* one later: normally you add delay to the top. If the sub's acoustic centre sits physically behind the top's, it is later still. If the measurement says the opposite, the top is already late, and you delay the sub instead. Measure; do not assume.

**Speed of sound.** About 343 m/s at 20 °C, and it changes by about 0.6 m/s per degree: c ≈ 331.3 + 0.606·T(°C). So 1 ms is about 0.34 m of path. Temperature only matters when the delays you are setting span tens of metres; a sub-to-top offset of a metre or two is unaffected by a 20 °C swing.

### 3.5 Equalisation

- **Parametric EQ (PEQ)**: centre frequency, gain, and Q (narrow or wide). **Shelf**: raises or lowers everything above or below a corner. **High-pass and low-pass** filters are also EQ.
- Two kinds of EQ happen in this rig. **Voicing EQ** is part of the cabinet's tuning, such as the published JMOD PEQs, and is set once per cabinet. **System EQ** corrects how the cabinets work together and with a space, and is set per venue and kept small.
- Keep corrections gentle. Cuts are safer than boosts. Do not boost a narrow dip, because a dip caused by cancellation cannot be filled with more level. Compare with and without the EQ often, to avoid fixing something that is not there.

### 3.6 Limiters and why drivers fail

Drivers fail in two ways.

- **Thermally.** The voice coil heats over seconds to minutes. Sustained high average power burns it.
- **Mechanically.** The cone or diaphragm travels too far, in milliseconds. Large low-frequency peaks, or any content below a ported box's tuning, can slam it into its limits.

A processor guards against both with a set of protections.

| Protection | Guards against | Speed | Where it is set |
| --- | --- | --- | --- |
| **High-pass filter** (subsonic filter) | Mechanical: low-frequency excursion | Instant | Below the sub's tuning frequency |
| **Peak limiter** | Mechanical and amplifier clipping | Milliseconds | Voltage ceiling per channel |
| **RMS (thermal) limiter** | Thermal | Seconds | Average-voltage ceiling per channel |
| **Amplifier clip limiter** | Distortion that heats and breaks tweeters | Instant | In the amp, if present |

A **limiter** has a hard ceiling it never exceeds. A **compressor** gradually reduces dynamic range above a threshold. A compressor with a very high ratio and fast attack can behave like a limiter, but one without a true RMS or "thermal" stage cannot protect a coil from sustained heat. Limiters should engage before any other stage in the chain clips.

**How the JMOD designer sets them.** JW publishes limiter values per band (guide p. 7). They are voltages at the speaker terminals:

| Channel | Peak limiter (threshold / attack / release) | RMS limiter (threshold / attack / release) |
| --- | --- | --- |
| 12NDL88 pair (2 × 8 Ω in parallel) | 105 V / 12.5 ms / 200 ms | 75 V / 2,500 ms / 5,000 ms |
| DCX464 Mid (16 Ω) | 59 V / 2.7 ms / 21 ms | 42 V / 1,600 ms / 3,200 ms |
| DCX464 HF (16 Ω) | 50 V / 1 ms / 2 ms | 35 V / 800 ms / 2,400 ms |

[Published]. These follow a simple rule that you can reuse for any driver. Working his voltages back to watts, the RMS limiter equals the driver's **nominal** power (for the woofer pair, 75 V into 4 Ω is 1,406 W against two 700 W drivers), and the peak limiter equals the **program** power, which is twice nominal, or √2 higher in voltage (105 V is 1.4 × 75 V, about +3 dB). Other sources recommend a larger peak margin, up to 6 dB above the RMS setting, so treat the peak figure as the one to tune.

**Checked against B&C's own pages (11 Oct 2026).** The DCX464 16 Ω is rated **110 W nominal / 220 W continuous program** for the mid section and **80 W / 160 W** for the HF section; the 12NDL88 is 700 W nominal / 1400 W continuous program. JW's voltages reproduce these exactly: √(110 × 16) = 42.0 V and √(220 × 16) = 59.3 V (his 42 V and 59 V); √(80 × 16) = 35.8 V and √(160 × 16) = 50.6 V (his 35 V and 50 V). So the rule above is how he set them, and the DCX464 figures that v1 took from retail copy are confirmed. For the **8 Ω** DCX464 the same ratings give √(P × 8): 29.7 V / 42.0 V (mid) and 25.3 V / 35.8 V (HF).

### 3.7 Gain structure

Gain structure is how the level is shared across the mixer, processor, amp and speaker so that no stage clips early and none adds avoidable noise.

- **Clip points.** Every stage has a maximum level it can pass. The goal is that, with a signal at the maximum you want, no stage before the limiter is near clipping, and the limiters engage before any stage clips.
- **Amp gain is a trim, not a volume control.** The ProSoundWeb method sets each stage in turn, starting with the first, with a test signal just below that stage's maximum, then adjusts each following stage to just below *its* maximum. Amp input attenuators typically end up 10 to 20 dB down.
- **Noise.** Hiss comes mainly from high amp gain and from converters. Use no more gain than needed: set the processor output to drive the amp to its clip point at the limiter threshold, and no further. On very sensitive horns, any extra gain is audible as hiss between tracks.
- **Fixed-gain versus sensitivity amps.** Some amps state voltage gain in dB (26 dB is ×20, 32 dB is ×40). Others state the input voltage for full power. §7 shows how to convert either.

### 3.8 Measurement basics

- **A measurement mic** converts sound to a signal and is calibrated, so levels are in true dB SPL. Ours is an individually calibrated USB mic with two calibration files: the 0° file for a mic pointing at the speaker, and the 90° file for a mic pointing up. For subwoofers the choice barely matters.
- **A sweep** is a gliding tone. The software divides what it hears by what it played, and gets the speaker's *impulse response*, from which magnitude, phase and delay follow. Sweeps give a clean result with a good signal-to-noise ratio. **Pink noise** is a steady hiss with equal energy per octave, used to set levels and to listen.
- **The impulse response** shows when energy arrives. A top's peak is sharp. A sub's is smeared, which is why aligning subs by looking for peaks is unreliable and aligning by *phase* is preferred.
- **Windowing** cuts the response off before reflections arrive, giving a cleaner measurement at the cost of low-frequency resolution. Outdoors with nothing nearby there is nothing to window out.
- **Ground-plane measurement.** Put the cabinet on the ground and the mic on the ground in front of it. The ground reflection then arrives with the direct sound, so the ground acts as a boundary instead of causing a comb-filter ripple. The result is repeatable and independent of stand height. A cabinet a few feet off the floor with a mic at ear height does the opposite: it creates a reflection that corrupts the low mids.
- **Why 10° off axis.** JW's guide says his measurements were taken at 10° off axis horizontally, ground plane, at 2 m. The guide does not say why. A plausible reason is that a multiple-entry horn can have an on-axis anomaly that listeners do not experience. We follow the same convention so our curves can be compared with his.
- **Timing reference.** For two measurements to share a timeline, the software needs a reference. A USB mic cannot loop its output back, so the REW program offers an *acoustic timing reference*: it plays a short high-frequency chirp from a speaker with a tweeter before each sweep and uses that to synchronise. It cannot use a sub as the reference, and it does not allow multiple sweeps. §9 shows the workflow.

## 4Kit

| Item | Requirement | Examples | Status |
| --- | --- | --- | --- |
| Measurement mic | Calibrated, omnidirectional, USB or XLR with interface | miniDSP UMIK-1 (planned) | Required |
| Measurement software | Sweeps, phase, alignment tool, SPL meter | REW (free); others do the same | Required |
| Laptop | Quiet, with USB and a stereo output; Wi-Fi and background tasks off during measurements | | Required |
| Small reference speaker with a tweeter | For REW's acoustic timing reference | Any small powered monitor | Needed for Method A in §9 |
| Stereo output breakout | Separate left and right feeds from the laptop | 3.5 mm to two 6.3 mm mono | Needed with the reference speaker |
| True-RMS multimeter | Measure amp output voltage and speaker resistance | Any decent DMM | Required for §7 |
| Sine and pink noise source | A laptop tone generator is enough | REW generator, DAW | Required |
| Tape measure, laser distance meter | Distances to 1 cm | | Required |
| Thermometer | Air temperature | | Useful |
| SPL meter | Check levels independently of the mic | Phone app, or the NIOSH app | Useful |
| Speakon tester or continuity tester | Cable and pinout checks | | Required |
| 1.5 V battery | Polarity tap test on woofers | AA cell | Useful |
| Hearing protection | Flat-response earplugs for events, over-ear for measurement | | Required |
| Clamp-on current meter | Mains draw per amp | | Useful |
| Cable labels and tape | Everything labelled | | Required |

## 5Before power

Do every step with the speakers either disconnected from amplifiers or the amplifiers off.

### 5.1 Cabinet and cable checks

- [ ] Every cabinet has an ID label. Every cable has a label at both ends.
- [ ] **Pinout continuity** on each cable and each cabinet connector. For the JMOD bi-amp route: pins 1± reach the woofer pair, pins 2± reach the FB464 input.
- [ ] **DC resistance** of each driver circuit, measured at the Speakon with a multimeter. Record it. Identical cabinets should read within a few percent of each other. A reading far above or below its siblings means a wiring or driver fault.
- [ ] **Polarity of each woofer** with a 1.5 V battery: touch positive to the "+" terminal briefly. The cone should move *outward*. Do the same for each SKRAM. (Compression drivers and the coax are checked by measurement instead; you cannot see their diaphragms move.)
- [ ] For the FB464: confirm its impedance version (8 Ω or 16 Ω) matches the DCX464 version fitted.
- [ ] Speaker cable length and gauge. For a 4 Ω load, keep round-trip cable resistance under about 5% of the load, which is 0.2 Ω. Copper in 2.5 mm² cable is about 14 mΩ per metre round trip, so 2.5 mm² is good to about 14 m. 4 mm² is good to about 23 m. 1.5 mm² only to about 9 m. [Calculated from copper's resistivity]

### 5.2 Test the signal path with no amps

- [ ] Source to processor: confirm left and right arrive at the right inputs, at a sensible level.
- [ ] Processor to each amplifier input: confirm each output reaches the intended channel (use the processor's per-output meters and a tone).
- [ ] Label each amp channel with the speaker it will drive.

## 6Build the processor template

Do this at a desk, with nothing connected to speakers, and save it before touching a cabinet. Name every output clearly: L-SUB, L-LF, L-COAX, R-SUB, R-LF, R-COAX.

### 6.1 JMOD, bi-amp route (FB464)

These values begin from the designer's tri-amp settings, because the guide publishes no bi-amp preset. Expect to re-measure and adjust.

| Output | Filters | Gain | Delay | Other |
| --- | --- | --- | --- | --- |
| **LF** (12NDL88 pair) | HPF 80 Hz LR4, LPF 195 Hz LR2 [Published] | 0 dB [Published] | 0.4 ms relative to mid [Published] | Limiters from §3.6 [Published] |
| **Coax** (via FB464) | HPF 370 Hz LR4; PEQ 640 Hz +3 dB Q3.8; PEQ 920 Hz −4.5 dB Q2.5; PEQ 1970 Hz −6.5 dB Q1.85; PEQ 6000 Hz +5.0 dB Q5.0; PEQ 8000 Hz +2.5 dB Q2.5 [Published, mid and HF values reapplied to one channel]. **Leave the 3450 Hz −7.5 dB Q1.3 PEQ out at first** (below) [Start] | −4 dB [Start] | 0 ms [Start]; no separate HF delay or inversion (below) | Limiters: derived below, start RMS 35 V and peak 50 V [Calculated] |

**Why the coax needs re-tuning, and which published filters survive.** The FB464 splits the coax at 3.6 kHz, 18 dB per octave on the mid side and 12 dB per octave on the HF side (B&C's FB464 page says "18 to 12 dB/oct" without naming the sides; a summary of the FB464V2 datasheet gives 18 dB per octave low-pass and 12 dB per octave high-pass, and B&C says the V2 uses the same circuit). That matches JW's electrical 3,600 Hz BU3 and BU2, which is reassuring. Because of the split, the mid PEQs (640, 920, 1970 Hz) act almost entirely on the mid section (an ideal 12 dB per octave HF branch is already 30, 24 and 11 dB down at those frequencies) and the HF PEQs (6000, 8000 Hz) almost entirely on the HF section (an ideal 18 dB per octave mid branch is 13 and 21 dB down there), so they can be reapplied to one channel unchanged. The one that cannot is **the 3450 Hz −7.5 dB PEQ**: in the tri-amp preset it sits on the HF output alone, but on a shared channel it also cuts the mid section right across the crossover and digs a hole where the target is flat. Start without it (or at about −3 dB), measure the coax, and add it only as far as the measurement asks. [Calculated reasoning; verify by measurement]

**What cannot be copied.** The published high band also has its own −5 dB level, 0.22 ms delay and inverted polarity. Behind a passive network those cannot be set independently: B&C says the FB464 phase-aligns the mid and HF elements itself. If the measured coax shows a notch near 3.6 kHz, the physical equivalent of the tri-amp's inverted HF is swapping the T+ and T− leads at the driver; try that before touching any filter. The relative mid and HF levels are fixed by the network, which B&C designed for its ME464 horn rather than the JMOD's, so a tilt in the top octaves is expected: correct it on the coax channel with a broad shelf above 3.6 kHz, by measurement. The .mdat has no FB464 trace; it holds the three tri-amp bands. [Datasheet, Start]

**Acoustic targets for the coax.** The .mdat defines the acoustic targets each channel is trying to hit (§8.4): the woofer target is an 80 Hz LR4 high-pass with a 500 Hz LR6 low-pass; the mid target a 500 Hz LR6 high-pass with a 4,000 Hz LR4 low-pass; the high target a 4,000 Hz LR4 high-pass. Together, the mid and high targets are flat from 500 Hz upward, so the coax channel should measure flat above 500 Hz, the woofer pair flat up to 500 Hz, and the two cross at 500 Hz acoustically, whatever the electrical corners are. [Published, from the file's trace notes]

**Limiters for the shared coax channel.** Both sections are fed from one voltage, so the limiter must protect the weaker section for whatever spectrum arrives. I modelled an ideal 3.6 kHz split of the 16 Ω DCX464 behind the 370 Hz LR4 high-pass, using B&C's nominal ratings (110 W mid, 80 W HF):

| Programme at the channel | Power to mid | Power to HF | Channel RMS volts at which the first section reaches its nominal rating |
| --- | --- | --- | --- |
| Pink noise (the rating signal) | 53% | 47% | 52 V (HF limits) |
| Music, energy per octave falling 3 dB per octave above 1 kHz | 86% | 15% | 45 V (mid limits) |
| Music falling 6 dB per octave above 1 kHz | 96% | 5% | 43 V (mid limits) |
| Mid band only | 100% | 0% | 42 V (mid limits) |
| HF only (everything above 3.6 kHz) | 0% | 100% | **36 V (HF limits)** |

[Calculated: ideal filters, resistive 16 Ω loads, no network insertion loss; real music sits between the two "falling" rows.]

| Limiter | Start value | Ceiling | Why |
| --- | --- | --- | --- |
| **RMS** | **35 V**, 800 ms attack, 2,400 ms release | 42 V, once measurement shows little HF energy in real programme | 35 V is safe for any spectrum including an HF-only one. 42 V is the mid section's nominal power and is all that music needs. At 35 V the mid still receives 66–74 W on music, 60–67% of its nominal rating |
| **Peak** | **50 V**, 2.7 ms attack, 21 ms release | 59 V | 50 V is the HF section's program rating; 59 V is the mid's. Use the mid timings: the HF's 1 ms / 2 ms would modulate 370 Hz-plus material on this channel |

So the v1 guess (JW's HF values) was safe but needlessly strict on the mid: the derivation supports raising to 42 V RMS and 59 V peak after measuring, not before. For the **8 Ω** DCX464 scale by √(8 / 16): start RMS 25 V and peak 36 V, ceilings 30 V and 42 V. A broadband limiter cannot see an HF-heavy fault (feedback, a bright test tone, a harsh sweep) because the voltage it sees is mostly mid; keep HF test signals off this channel. The standard FB464 adds series filament bulbs as protection; B&C publishes no power rating for it and does not say when the bulbs act. The **FB464V2** has higher-power inductors and no bulbs, so with it the DSP limiter is the only protection: keep the start values until measured. [Datasheet, Calculated]

### 6.2 JMOD, tri-amp route

| Output | Filters | Gain | Delay | Other |
| --- | --- | --- | --- | --- |
| **LF** | HPF 80 Hz LR4, LPF 195 Hz LR2 | 0 dB | 0.4 ms | Limiters per §3.6 |
| **Mid** | HPF 370 Hz LR4, LPF 3,600 Hz BU3; PEQ 640 Hz +3 dB Q3.8; PEQ 920 Hz −4.5 dB Q2.5; PEQ 1,970 Hz −6.5 dB Q1.85 | −4 dB | 0 ms | Limiters per §3.6 |
| **HF** | HPF 3,600 Hz BU2; PEQ 3,450 Hz −7.5 dB Q1.3; **PEQ 6,000 Hz +5.0 dB Q5.0; PEQ 8,000 Hz +2.5 dB Q2.5** | −5 dB | 0.22 ms | **Polarity inverted** |

[Published] for all of the above, **read from the filter sets stored in JW's .mdat**, not from the printed guide. In REW a BU3 low-pass is a Q = 1.0 second-order section plus a first-order section; an LR4 is two Q = 0.71 sections; an LR2 is one Q = 0.5 section (that is how the file stores them). The check of the file follows.

**Where these numbers come from, and why they differ from the printed guide.** The printed page 7 lists, for the mid band, "PEQ 3: 540Hz | +3dB | Q3.8" and, for the high band, "PEQ 1: 3450Hz | −7.5dB | Q1.3" and "PEQ 2: 6000Hz | +2.5dB | Q" with the Q cut off (the page itself, not just our copy, ends there). The REW file that ships with the package (`Raw Measurements and EQXO Settings.mdat`, 3 Feb 2026, the same date as revision 2.02) stores the real filter sets on the raw traces and prints the same settings in the notes of the "XO+EQ" traces: mid boost at **640 Hz**, and a high band with **three** peaking filters, 3,450 Hz −7.5 dB Q1.3, **6,000 Hz +5.0 dB Q5.0** and **8,000 Hz +2.5 dB Q2.5**. I checked this numerically rather than trusting either source: I rebuilt each filter as a standard biquad at 48 kHz and compared "raw trace + filters" with the file's own XO+EQ trace.

| Band | Candidate filter set | Mean offset | Scatter (std. dev.) | Worst point |
| --- | --- | --- | --- | --- |
| LOW | 80 Hz LR4 + 195 Hz LR2 (printed) | 0.01 dB | 0.02 dB | 0.12 dB |
| MID | boost at **540 Hz** (printed) | 0.01 dB | 0.55 dB | 2.0 dB |
| MID | boost at **640 Hz** (.mdat) | 0.01 dB | **0.02 dB** | 0.11 dB |
| HIGH | 6,000 Hz +2.5 dB (printed reading) | 0.53 dB | 0.84 dB | 2.5 dB |
| HIGH | 6,000 Hz +5.0 dB Q5.0 and 8,000 Hz +2.5 dB Q2.5 (.mdat) | −0.02 dB | **0.02 dB** | 0.10 dB |

A correct filter set leaves a flat constant offset; only the .mdat values do. So the printed page has a transposition (540 for 640) and a garbled high-band entry (the Q is missing and the 8 kHz filter is absent). **What this does and does not prove:** it proves the file's published XO+EQ traces were generated with the .mdat values. It does not prove the filters in JW's own hardware preset, so confirm with a measurement of your own build and ask JW (john@jwsound.live) to confirm and issue an erratum. The mid PEQ 2 Q is 1.85 in the file (1.8 on the page, a rounding). [Calculated from Published]

### 6.3 SKRAM subs

| Item | Value | Tag |
| --- | --- | --- |
| Low-pass | 80 Hz LR4, to match the JMOD's 80 Hz LR4 high-pass | [Start] |
| Subsonic high-pass | 24 dB per octave Butterworth. Start corner by vent setting: **27 Hz** with all four open (29.5 Hz tuning), **24 Hz** with three (25.5 Hz), **20 Hz** with two (20.5 Hz), **15 Hz** with one (14.5 Hz). Evidence below | [Start], supported for the all-open case only |
| Gain | 0 dB, then trim in §9 so the sub's passband level matches the top's | [Start] |
| Delay | 0 ms: the sub is the timing reference; delay goes on the tops | [Start] |
| Limiters | Computed in §7, using the amplifier's gain and the loading | [Calculated] |
| EQ | None to start | |

**The subsonic filter is still the one setting not to trust blindly.** Horn-loaded and vented cabinets stop loading the cone below their tuning, and the cone then moves very far for very little sound; in a horn, bottoming out can be silent, so do not rely on listening for it. Ricci's notes publish no filter, and I found no measured excursion data for a 21DS115 in a SKRAM. What exists is owner reports, all secondhand: I read them as search-result summaries, because the AVS Forum pages themselves sit behind an access gateway that I did not use.

| Report | Vents | Filter |
| --- | --- | --- |
| An owner of 21DS115 SKRAMs | All open (about 28 Hz) | Started with a 23 Hz, 12 dB Butterworth high-pass; later preferred all open with 12 dB Butterworth at **27 Hz** |
| Another owner | Not stated | Runs the SKRAMs high-passed at **31 Hz**, LR 24 dB per octave |
| A seller of a built 21DS115 SKRAM | One vent blocked (about 25 Hz) | **20 Hz** cutoff, "on for its whole life" on a single amp |
| Ricci | | Optimised for the 29.5 and 25.5 Hz tunings; lower tunings lose output and vent area |

Owners therefore run corners from about 23 to 31 Hz with all vents open. **27 Hz at 24 dB per octave** sits in the middle of that spread and is steeper than the 12 dB filter the one owner is comfortable with, so it is the more protective setting; that replaces v1's 30 Hz, which was a guess. The three-, two- and one-vent corners are extrapolated at about 0.9 × the tuning frequency and are weaker evidence. [Start, anecdotal evidence]

**How to confirm it on our own cabinets** (my suggestions; nothing here is designer guidance):

1. **Impedance.** If you have an interface and a series reference resistor, REW can plot impedance: the dip between the two impedance peaks of a vented box marks the tuning, and the high-pass should sit at or just above it. The UMIK-1 alone cannot do this.
2. **Distortion against level.** Measure a stepped sine at the corner frequency and about 10 Hz above it, raising the level in 3 dB steps. A steep rise in distortion marks where the cone is running out of room; set the limiter below that.
3. **Look at the cone.** With the hatch off, sweep a low-level sine (1–2 W) down from 40 Hz to 15 Hz and watch for the frequency where the excursion starts to grow quickly. The hatch off changes the loading, so treat it as a coarse check only.

### 6.4 Signal routing for stereo and mono

For stereo tops with mono subs (the recommended default; see §10):

- Left tops get input L, right tops get input R.
- Both sub channels get L + R, with each input trimmed by about −6 dB before the sum so a mono signal does not rise by 6 dB.
- Whatever you choose, set the final sub level by measurement in §9 using the same mono signal, because that is what fixes the sub-to-top balance.
- In Arrangement C each JMOD stands beside the cluster, not on it, so each side needs its own top delay on top of the sub-to-top alignment (§9.7).

## 7Gain structure and limiters

### 7.1 Convert ratings into limiter voltages

For each driver or driver group:

1. **RMS limiter voltage** = √(nominal power × impedance).
2. **Peak limiter voltage** = √(program power × impedance), where program power is twice nominal. This is √2 times the RMS voltage.
3. **Amplifier ceiling** = √(amplifier continuous power × load impedance).
4. **Use the lower** of the driver value and the amplifier ceiling, so the limiter acts before the amp clips.
5. **Convert to processor units** (only needed if the processor does not accept speaker volts):
   - Voltage at the processor output = speaker volts ÷ amplifier voltage gain (a ratio, not dB).
   - Level in dBu = 20·log₁₀(V ÷ 0.775).
   - If the processor shows dBFS, add the converter's "0 dBFS = +X dBu" to relate them.
6. **Bridging** an amplifier doubles its output voltage (+6 dB). Do not bridge without recomputing.

### 7.2 Worked examples

The amplifier numbers here are made-up examples. Use your own.

**Example 1 · JMOD woofer pair, with JW's published limits.** Two 12NDL88 at 8 Ω in parallel is 4 Ω. Nominal power per driver is 700 W (B&C), so 1,400 W total. RMS limiter = √(1,400 × 4) = 74.8 V, which matches JW's 75 V. Program power is twice that, 2,800 W, so peak limiter = √(2,800 × 4) = 105.8 V, which matches his 105 V. With an amp of voltage gain 32 dB (×39.8): processor output = 75 V ÷ 39.8 = 1.88 V, which is +7.7 dBu; the peak limiter 105 V gives 2.64 V, +10.6 dBu.

**Example 2 · One SKRAM, 21DS115 at 8 Ω.** Nominal 1,700 W, program 3,400 W. RMS limiter = √(1,700 × 8) = 116.6 V. Peak limiter = √(3,400 × 8) = 164.9 V.

**Example 3 · An amplifier smaller than the driver.** Suppose an example amplifier is rated 700 W continuous into 8 Ω. Its ceiling is √(700 × 8) = 74.8 V, much lower than the driver's 116.6 V. The limiter must be set at about 75 V, not 116.6 V, and the sub will never reach its own power rating. That is fine, and normal: it means the amp, not the driver, sets the maximum, so size the limiters to the amp.

**Example 4 · Two SKRAMs on one channel.** Two 8 Ω drivers in parallel is 4 Ω. The voltage across both is the same as across one, so the voltage limits are unchanged (116.6 V RMS, 164.9 V peak). What changes is the *power the amp must supply*: twice as much at the same voltage.

**Example 5 · The shared coax channel (FB464) with the 16 Ω DCX464.** B&C's ratings are 110 W nominal / 220 W program (mid) and 80 W / 160 W (HF). At 16 Ω the section limits are mid 42.0 V RMS / 59.3 V peak and HF 35.8 V RMS / 50.6 V peak. One voltage feeds both sections, so take the lower RMS figure as the start (35 V) and the HF program figure as the peak start (50 V), and raise toward 42 V and 59 V only after measuring (§6.1). With an amplifier of voltage gain 32 dB (×39.8): processor output for 35 V RMS = 35 ÷ 39.8 = 0.88 V = +1.1 dBu; for 50 V peak = 1.26 V = +4.2 dBu. Power at the start values: 35² ÷ 16 = 77 W and 50² ÷ 16 = 156 W, far below any amplifier ceiling, so here the **driver sets the limit**, not the amp.

### 7.3 Measure the amplifier's real output

Calculated ceilings assume the amplifier delivers what its datasheet says. Verify on the bench. The following follows a method used by a loudspeaker manufacturer for calibrating a processor's limiters against an amplifier.

1. **Disconnect all speakers.** You will drive the amp to its maximum voltage. **Electrical safety:** at clip, an amp channel can put out 70 to 120 V RMS or more at its terminals, which is enough to hurt you. Do not touch the terminals while the amp is on. Connect the meter's insulated probes with the amp off, stand back, then power up.
2. Connect the processor output to the amp input. Clear all processing on that output (or use a flat template). If the amp has clip limiters, turn them on.
3. Connect a true-RMS multimeter across the amp's output terminals.
4. Send a sine wave in the 45 to 70 Hz range from any source. Raise the level slowly until the amp's clip indicator lights, then back off until it just goes out.
5. Read the voltage. This is the amp's maximum clean continuous output on that channel.
6. Compare with the calculated ceilings. Set the RMS limiter at or below the lower of the two.
7. Repeat for every amplifier channel. Record the amp model, gain, clip voltage and the limiter values you set.

Keep a meter on hand during the first loud test with speakers connected. If the voltage ever exceeds the thresholds you calculated, stop and find out why.

### 7.4 Set the amplifier gain

1. With speakers still disconnected, feed a test tone from the source at the highest level you want the system to reach. Use the mixer's nominal "0" level, not its maximum.
2. Raise the processor output until the limiter thresholds are reached or the amp is at its clip point, whichever comes first.
3. Set the amp's input control so that, at that processor output level, the amp is at the limiter threshold voltage. Any more gain only adds noise.
4. Set all channels of the same amp model to the same gain, so that the same processor level gives the same output on each.
5. Write down the final gain setting. Cover or tape the controls afterwards.

### 7.5 Noise-floor check

With the speakers connected, the source muted and the system running, stand about a metre in front of each JMOD and listen. Note any hiss, hum or fan noise on each band. Do this at the end of every setup, not just the first one. If hiss is audible, the usual causes are too much amplifier gain or an amp with a noisy channel. The JMOD guide recommends the 16 Ω DCX464 for a lower noise floor.

## 8Measuring a cabinet

### 8.1 Where and when

Outdoors on a hard, flat surface (concrete or asphalt) with nothing large within 10 m, on a calm, quiet day. Wind ruins high-frequency measurements and rain stops everything. A large, empty hall with a hard floor also works. If you must measure indoors, use a very short time window and accept the loss of low-frequency resolution.

### 8.2 Mic and software setup

- Plug the mic in before launching the measurement software and leave it connected for the whole session.
- Select the mic specifically, not "default device". Set the sample rate to 48 kHz. Turn off any operating-system audio enhancements for the mic.
- Load the mic's calibration file. For a mic lying on the ground, pointing at the cabinet, use the 0° file.
- For a mic that miniDSP's software recognises, such as the UMIK-1, REW needs no separate SPL calibration.
- Run the software's level check with the system muted first, to read the noise floor. Aim for measurement levels at least 20 dB above the noise floor. Check the level at the lowest drive that works. Use a level of about 85 to 95 dB SPL at the mic [Start], and keep a hearing-protection habit.
- Close other programs, turn off Wi-Fi, and keep the laptop on mains power. Interruptions to audio can corrupt a measurement.
- Use single sweeps, not several. Use sweeps no longer than needed. Long sweeps risk overheating compression drivers.

### 8.3 Cabinet and mic placement (the "ground plane")

- **Cabinet on the ground**, facing the mic, not on a stand or a crate.
- **Mic on the ground**, 2 m from the front of the cabinet, capsule pointing at it, lying flat.
- **JMOD.** Place the mic 10° off the cabinet's axis horizontally, as JW did. Aim the cabinet at the mic as best you can (a wedge of wood under the front tilts a cabinet; a phone camera held against the grille helps with alignment outdoors).
- **SKRAM.** Put the mic on the ground 2 m in front of the mouth. Subs do not need aiming.
- Mark the ground with chalk so the placement is repeatable. Measure and record the distance.
- **JMODs are pole-mounted in use.** Do the voicing (§8.4) on the ground plane first, as above. Once the cabinet is on its stand the floor reflection returns and comb-filters the low mids, so do not re-voice the filters from measurements on the stand; use the stand only to check timing, tilt and coverage.

### 8.4 Measure each JMOD band alone

Use the processor's mute or solo function (or physically disconnect the other bands) to measure each band alone, with its normal limiters on.

**What is in JW's REW file.** Nine traces, which I read directly:

| Trace | What it is |
| --- | --- |
| Target LOW / MID / HIGH | The acoustic targets: 80 Hz LR4 high-pass with 500 Hz LR6 low-pass; 500 Hz LR6 high-pass with 4,000 Hz LR4 low-pass; 4,000 Hz LR4 high-pass |
| 12NDL88 LOW RAW, DCX MID RAW, DCX HIGH RAW | Measured 29 Apr 2025; the notes on the mid and high traces say the level was "adjusted by −9 dB" so the plots do not show absolute SPL. Each stores its filter set (§6.2) |
| 12NDL88 XO+EQ, DCX MID XO+EQ, DCX HIGH XO+EQ | Generated 3 Feb 2026 from the raw traces and those filters |

Measurement conditions (guide p. 6): ground plane, 2 m, an EMX-7150 and a Scarlett 2i2 (2nd gen). The release notes describe the raws as **on-axis**, while the guide asks you to measure at **10° off-axis**; expect small differences in the top octaves when you compare, and measure both if the top end disagrees. The EQ window in REW can generate a predicted measurement from a trace plus its filters, which is how the XO+EQ traces were made; I have not driven REW myself, so find the menu on your copy.

1. **Raw check.** Measure the woofer pair, the coax mid, and the coax high with *only* their high-pass and low-pass in place, no PEQ. Overlay your curves with JW's raw traces. Open the REW file in the same software.
2. **With the published filters and EQ.** Apply §6 and measure again. Compare with his "XO+EQ" traces and the "Target" curve for that band.
3. **Differences.** Compare shapes first, not absolute levels. Differences of about 1 to 2 dB are normal. Several dB over a wide band, or deep notches that are not in his curves, usually point to a build or wiring problem: a leak, a reversed driver, a poor seal at the woofer, an incorrectly wired coax.
4. **Absolute level.** Match the level difference between bands using the gain settings, as in the published targets (the mid is 4 dB down, the high 5 dB down).

For the bi-amp route you cannot isolate mid and high. Measure the coax as one band and compare it with the sum of JW's mid and high traces.

### 8.5 Measure the SKRAM

1. Measure with the low-pass and subsonic filter in place and the limiters on.
2. Measure at the lowest level that gives a clean sweep. Do not start loud.
3. **Record all four vent tunings.** Block the vents with the port blocks and measure each configuration: all open, three open, two open, one open. Keep the curves. This is the only way to know what each setting does for our cabinets, and it tells you whether the subsonic filter corner is in the right place.
4. Compare cabinets. Two identical SKRAMs should match within a dB or so across the passband. A cabinet that does not has a leak, a different driver or a wiring problem.

### 8.6 Save and name every measurement

Naming scheme: `cabinet-ID_band_vent-setting_date` (for example `JMOD-L_LF_20251115`). Keep a measurement log (§A).

## 9Aligning subs to tops

Do this with one stack, outdoors, on the ground-plane setup from §8, with the sub and the top at their intended relative positions. If the intended arrangement changes later, repeat the alignment for the new arrangement.

### 9.1 Principles recap

- Measure the sub alone and the top alone, *at the same mic position*, with the crossover already set.
- Decide the crossover region (about 60 to 120 Hz for an 80 Hz crossover).
- Make the phase of the two agree through that region, using delay on the top and, if needed, a polarity flip.
- Check that the sum is flat through the crossover, then set the relative level.

### 9.2 Method A: phase overlay with a timing reference (preferred)

This needs the acoustic timing reference described in §3.8.

1. Place a small powered speaker with a tweeter as the reference, and feed it from the laptop's other output channel. Set the reference level trim so the chirp is clearly picked up at the mic.
2. Measure the **sub alone** with the timing reference on. Then the **top alone**. Do not move the mic between them. Keep the reference speaker and the mic fixed too.
3. Open the software's alignment tool and load the two measurements. Put the sub in the first slot ("A"), which is the reference, and the top in the second ("B"), the one whose delay the tool adjusts. A positive delay on B means the top must be delayed, which is what we expect.
4. Place the cursor at the crossover frequency. Use the tool's phase-alignment function ("align phase at cursor") and look at the phase traces overlaid. They should lie close together through the crossover region. If they are about 180° apart, flip the polarity of one and align again.
5. Check that the delay it reports is plausible. A full-cycle ambiguity exists at any single frequency: at 80 Hz a cycle is 12.5 ms, so a result 12.5 ms away from the right answer looks identical on the phase plot at that frequency. Compare with the physical path difference between the sub's and the top's acoustic centres.
6. Look at the summed response in the tool. It should be smooth through the crossover with no dip. Adjust the delay by tenths of a millisecond and watch the sum.
7. Note the delay and polarity. Create an "aligned sum" measurement for the record.
8. Enter the delay as an *added delay on every JMOD output* (LF and coax, or LF, mid and HF), the same amount on each, so the designer's relative offsets between JMOD bands (0.4 ms, 0.22 ms) stay intact. If the tool wants a *negative* delay on B, the top is already late: put that delay on the sub instead. Then run a fresh measurement with both playing and the mic unmoved to confirm it matches the predicted sum.

**Caveats from the tool's documentation and users.** The tool's delay figures for subs are less precise than for tops, because a sub's impulse response has a broad, delayed peak. Latency differences between the electrical paths of the two sources (for example one path through extra processing) also appear as apparent delay. Re-measure after every change, and do not trust a result you have not confirmed with a new measurement.

### 9.3 Method B: step the delay and read the sum (no timing reference)

Use this if the acoustic timing reference misbehaves. It needs nothing but the mic.

1. Set the top's delay to 0 ms. Play the sub and the top together and measure the response. Keep the mic fixed.
2. Raise the top's delay in steps of 0.5 ms, up to about 12 ms. Measure after each step.
3. Overlay the measurements. At the crossover region, the sum will improve, reach a best value, then worsen as delay continues. Pick the delay with the highest, smoothest sum through the crossover.
4. Repeat with the polarity of the sub flipped. If the flipped version gives a clearly better best case, keep the flip.
5. Refine with 0.1 ms steps around the best delay.

### 9.4 Method C: the null test (field check)

A fast sanity check that works with a sine generator and an SPL meter.

1. Play a sine at the crossover frequency (80 Hz) through both sub and top, at a low level.
2. **Invert the polarity of the sub.** The sound at the mic will drop where the two now oppose each other.
3. Adjust the top's delay until the level at the mic is at its *lowest*. At that setting the two sources are exactly opposite.
4. **Un-invert the polarity.** They are now in phase at that frequency.
5. Confirm with a measurement. This method aligns at a single frequency only; always check the sum across the whole crossover region.

### 9.5 Set the relative level

After alignment, compare the sub's and the top's passband levels, well away from the crossover: the sub around 40 to 70 Hz and the top around 100 to 200 Hz. Trim the sub gain until the two sit at the same level (flat). Then decide, as a separate step, whether to add a low-frequency lift for taste (§12).

### 9.6 Record, repeat for the arrangement, copy to the other stack

Write down: delay on tops, polarity, gains, the arrangement (two-high, side-by-side, centre cluster), the mic position and the temperature. If the physical arrangement changes, the delay changes with it.

### 9.7 Arrangement C: aligning pole-mounted tops to the centre cluster

Our baseline puts the sub cluster in the centre and a JMOD on a pole at each side. The tops are not on top of the subs, so the alignment in §9.2 to §9.4 has to be done with the real geometry, and the delay on each top is not the number you would get with the cabinets side by side.

1. **Set the real layout.** Cluster in position, one JMOD on its stand at its real place and height, the other side muted or off. Mark the mix position and a second check position.
2. **Measure at the mix position**, mic at ear height, sub alone and then top alone without moving the mic, and align as in §9.2 (timing reference) or §9.3 (stepped delay). The delay the tool gives already contains the geometry for this side.
3. **Sanity-check it with geometry.** Delay on the top ≈ the delay a co-located top would need − (path from the top to the mic − path from the cluster to the mic) ÷ c. A top farther from the mic than the cluster arrives later and so needs *less* delay; a nearer top needs *more*. Worked example, with invented numbers to show the arithmetic: the mix position is 12 m from the cluster on the centre line and each JMOD stands 3 m to one side of the cluster centre on the same front line. The top's path is √(12² + 3²) = 12.37 m, 0.37 m longer, which is 1.1 ms later at 343 m/s. If a co-located top would need +4.2 ms, this side needs 4.2 − 1.1 = **3.1 ms**. The measurement wins over the arithmetic.
4. **Repeat for the other side.** With the mix position on the centre line and a symmetrical layout, both sides get the same delay. Otherwise the nearer side gets more delay by the path difference ÷ c (§10.2).
5. **Check off the mix position.** The alignment is exact only where you measured. At 80 Hz, 1 ms is 29° (§3.4), so a few metres sideways costs little; confirm at two off-axis positions (§12).
6. **Cluster layout.** Four SKRAMs in a row are about 2.4 m wide; adjacent centres are 0.61 m apart, well under a quarter wavelength at 80 Hz (1.07 m), so they couple as one source. Use the same delay on every sub and do not offset them. Stage 1 (two SKRAMs side by side) behaves the same, 1.2 m wide.
7. **Record** the layout, stand heights, distances, delays and temperature (§A.3). If a stand or the cluster moves, repeat from step 1.

[Calculated]

## 10Stereo and mono

### 10.1 The default

**Stereo tops, mono subs.** Two stacks with identical settings. Tops receive left and right. The subs receive the sum below about 80 Hz. A DJ mixer's mono switch gives full-band mono, which is one switch away.

Why mono subs: bass in dance music is essentially mono and gives little directional information below about 100 Hz, so a summed low band avoids cancellation from out-of-phase low content. Why stereo tops: width and detail for IDM, techno and house, with 90° horizontal coverage that lets most of the floor hear both sides.

### 10.2 What it adds to the work

1. **Routing.** The input matrix described in §6.4.
2. **Presets.** One preset per stack, mirrored. Tune one stack fully, copy it to the other.
3. **Matching checks.** After copying:
   - Measure the left stack and the right stack at the same distance and compare. They should match within about 1 dB.
   - Play mono pink noise through both subs. The bass should *increase*, not cancel. If it drops or has a deep hole, check polarity and the cable pinout.
   - Listen at the centre, then to the left and right of the mix position.
4. **Delays.** Nothing new if the mix position is equidistant from both stacks. If not, delay the nearer one by the path difference. The sub-to-top delay is the same on both sides.

### 10.3 The layout matters more than the settings

If the two stacks carry subs and are far apart, they act as two separate sources playing the same bass. Listeners off the centre line hear the sides at different moments, which carves notches in the response that EQ cannot fill. This is the "power alley". Feeding both the same mono signal does not prevent it: the spacing causes it.

The remedy is to keep subs together. The plan lists three arrangements, and **C is our baseline**:

- **A.** Two-high stacks left and right. The two sub groups are as far apart as the stacks.
- **B.** Side-by-side pairs left and right with a pole. Same issue.
- **C.** A centre cluster of all the subs with the JMODs on stands or poles left and right. The subs behave as one source. This needs a per-side delay on each top so it lines up with the cluster at the mix position (§9.7).

For arrangement C, the delay on each top comes from the geometry: start from the alignment a co-located top would need and **subtract** the extra path of a top that is farther from the mix position than the cluster, or add the shortfall of one that is nearer, divided by the speed of sound. (An earlier version of this guide said "add" without the sign; the sign depends on which is nearer.) Measure it; do not just calculate it.

If a room is small, or the stacks are only a few metres apart, A or B will sound acceptable. Verify by measuring at the centre and at two or three off-axis positions.

**Growth path: side stacks.** The plan's later step puts SKRAMs, SKHORNs or other bass bins under the JMODs so the tops reach mounting height without poles. That puts bass sources at the sides again, so the power alley returns in proportion to how much bass the side stacks carry. Options to test when you get there, none verified: (a) high-pass the side-stack bass cabinets higher (for example 60 to 80 Hz) so the centre cluster carries the lowest octave and the side stacks carry only the 80 to 160 Hz band where the JMOD is weakest (plan §08); (b) give the side-stack subs their own delay and level and measure the combined response at several positions; (c) accept two sub groups if the stacks stay within a few metres. In every case re-run §9 for the new arrangement, because the delays change.

## 11Verifying limiters

Do this once, carefully, with a hand free to turn the level down.

1. **Speakers disconnected.** Confirm that the limiter engages at the intended output voltage. Send a tone, watch the voltage with the multimeter and the processor's limiter indicator. The limiter's gain reduction should begin at the threshold, and the output voltage should stop rising.
2. **Speakers connected, low level.** Play music at a low level. Confirm no limiter activity and no distortion.
3. **Short bursts.** Raise the level in steps and play a few seconds of pink noise or a loud passage. Watch the gain-reduction meter. The peak limiter should flick on peaks. The RMS limiter should only engage after seconds of sustained loud material.
4. **Listen for distortion** before the limiter engages. If the amp clips first, the limiter threshold is too high for that amp: lower it.
5. **Never test with a sustained loud tone** into a connected speaker. Use short bursts.
6. **Watch the clip lights.** They should stay off at normal levels and light only briefly when the limiter is working hard.

Document the result as part of the preset record (§13).

## 12Tuning in a venue

The aim is to change as little as possible. The cabinets were tuned outdoors on the ground plane. A venue adds its own room, so measure, make small corrections, and stop.

1. **Place** the stacks and set the arrangement. Record the layout. Measure the distance from each stack to the mix position.
2. **Check timing.** If the stacks are at different distances from the mix position, add delay to the nearer one.
3. **Measure at the mix position and at three to five other places** in the audience area, at ear height. Use the same measurement level.
4. **Average them** (the software's vector or RMS average) to see what the common behaviour is. A single spot's quirks are mostly the room, not the system.
5. **Compare with your target.** Do not aim for a ruler-flat line. Many engineers use a gentle tilt: flat through the mids with some extra low end, and the high end gently falling off. Many engineers add a few dB of low-frequency lift, often 3 to 6 dB below about 100 Hz for dance music [Start]. This is taste and venue dependent: there is no single right curve, and sources disagree. Choose one with your ears and with music you know.
6. **Apply gentle, broad EQ** to the whole system (before the splitting, if your processor allows it, so both stacks and the subs benefit). Cut peaks, avoid boosting dips, and never EQ a null. Compare with the EQ bypassed regularly.
7. **Listen** with reference tracks: something with a clean sub-bass sweep, a well-known kick drum, a vocal, hats and percussion, and one or two of your own tracks that you know well. Walk the room.
8. **Set the level cap** (§14) with a calibrated SPL meter at the mix position, and in line with local limits.

## 13Document, back up, lock

- [ ] **Export every preset** to a file, in the processor's native format, and also screenshot or print each page of settings. Store copies off the laptop.
- [ ] Fill in the **preset record** (§A): per output, filters, EQ, gain, delay, polarity, limiter values, the amp model and its gain, the date, who set it, and the measurements that justify it.
- [ ] Keep the measurement files with names matching the preset record.
- [ ] **Lock** the processor (front-panel lock or password) and cover or tape the amplifier gain knobs after calibration.
- [ ] Decide who may change what. A sensible rule: anyone may adjust the master level and the mono/stereo switch; only the named sound lead may change filters, gains, delays or limiters.
- [ ] Keep a **recovery copy** of the factory-default and of the last known good preset on the laptop and on a USB stick in the case.
- [ ] **Two people** should be able to run the whole procedure. The plan lists tuning knowledge concentrated in one person as a risk.

## 14Event day

### 14.1 Setup

1. Place the sub cluster and the JMOD stands to the agreed arrangement; measure and record the distance from the cluster and from each top to the mix position.
   - **Stands:** legs fully open on firm, level ground; ballast bag on the centre column; pole locking screw or ring lock tight; the JMOD's pole flange bolts checked; cable strain-relieved so the cable cannot pull the stand over; the area under and around each stand kept clear of the audience.
   - **Wind:** if gusts exceed about 8 m/s (30 km/h) do not run the JMODs on tripod stands unless they are guyed and ballasted; see the Build Guide §D1 for the estimate behind this. Take them down in a gale.
2. Connect the speaker cables, with the **amps off** and the processor muted.
3. Confirm labelling, polarity and pinouts at every connector. A wrong cable is the most common failure.
4. Power on in this order: **source, processor, amplifiers last**. Amps on last avoids a power-on thump into the speakers.
5. Recall the preset. Confirm the right one is loaded and that nothing is bypassed.
6. Bring the level up from zero with pink noise at a low level.

### 14.2 Quick checks (about ten minutes)

- [ ] **Each channel, one at a time:** pink noise on each output, one cabinet at a time. Confirm it is the right cabinet and right band, and that nothing rattles or buzzes.
- [ ] **Polarity and sum:** mono pink noise on both subs, then the top and sub together: the sum at the crossover should not dip. If it does, a cable has the wrong polarity.
- [ ] **Left and right** are balanced: stand in the centre, check left and right in turn.
- [ ] **Noise floor** with the source muted, near each top. Hiss or hum is a gain or a ground problem.
- [ ] **Limiters** are not engaged at normal level; clip lights are off.
- [ ] **One walk-through** with a reference track.

### 14.3 Operating rules

- **The master level is the only knob most people touch.** Keep the mixer's master near its nominal position and use the processor or amplifier master for overall level.
- **Level cap.** Agree a maximum level before the event. Put an SPL meter at the mix position or the loudest audience position, and watch it. Check local rules: in Germany, audience-exposure limits (DIN 15905-5) apply to many events, and the numbers in the 2007 edition (99 dB(A) average over 30 minutes and 135 dB(C) peak at the loudest audience position) were replaced by a 2022 edition whose limits I could not confirm.
- **If something distorts,** turn down, do not turn up. Look at limiter and clip indicators first.
- **Never** change a filter, delay, limiter or gain during an event unless it is an emergency and the sound lead has agreed.
- **Hearing protection** for the operator and crew at the mix position, and offered to the audience where required.
- **Thermal.** If a cabinet or amplifier gets hot, let it cool. Keep amp vents clear.

### 14.4 Shutdown

1. Mute the source, turn the level down.
2. **Amplifiers off first**, then the processor, then the source.
3. Disconnect cables, label them, and stack them in their cases.
4. Note anything unusual in the event log: failures, limiter activity, complaints, changes. Update the preset record if anything was changed.

## 15Troubleshooting

| Symptom | Likely causes | Checks |
| --- | --- | --- |
| No sound from a band | Muted or soloed output, cable fault, amp channel off, wrong preset | Processor meters, swap cables, amp channel indicators |
| Hollow or thin sum between sub and top | Polarity or delay wrong, or a reversed cable | §9; measure sub and top alone, then together |
| Sub louder than expected on mono content | Sum without a −6 dB trim | §6.4; re-measure level |
| Bass cancels when both sides play | One stack's polarity or cable reversed | Mono pink noise on each sub alone then together |
| Uneven bass across the floor | Sub spacing ("power alley"), room modes | §10.3; consider a centre cluster; measure several positions |
| Hiss | Too much amp gain, a noisy channel, wrong input level | §7.4 and §7.5; lower amp gain, raise the processor level |
| Hum or buzz | Ground loop, unbalanced connection, mains interference | Use balanced cables, a single power distribution, lift grounds only where safe |
| Distortion before the limiter engages | Amp clipping, limiter thresholds too high for the amp | §7.3: measure the amp's clip voltage and lower the limiter |
| Limiter constantly engaged | Level too high, thresholds too low for the programme | Check the level cap; check that thresholds match the amp |
| Delay seems wrong across the room | Wrong path difference, temperature change, wrong preset | Re-measure; confirm preset |
| Compression driver sounds harsh or dull | Clip, a failed driver, or the wrong FB464 impedance | Check clip lights; compare with the measurement; check the FB464 version |
| Measurement is noisy or odd | Wind, traffic, wrong mic file, input level off, clock mismatch | §8.2; use single sweeps; repeat on a calm day |
| Alignment tool gives implausible delay | Cycle ambiguity, polarity flip not accounted, latency differences | §9.2 caveats; confirm with a new measurement |
| Amp too hot or shuts down | Blocked vents, low impedance, cable shorted | Check airflow, loads and cable continuity |

## AWorksheets

Copy these into your own sheet or print them.

### A.1 Channel map

| Output | Name | Amp channel | Cabinet | Speakon pins | Load | Filters | Delay | Gain |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | L-LF | | JMOD-L | 1± | 4 Ω | HPF 80 LR4, LPF 195 LR2 | 0.4 ms (+ top delay, §9.7) | 0 dB |
| 2 | L-COAX | | JMOD-L | 2± (FB464) | 16 Ω | HPF 370 LR4 + PEQs (§6.1) | (+ top delay, §9.7) | −4 dB |
| 3 | SUB-A | | SKRAM-1 (+ 2) in the centre cluster | 1± | 4 Ω | LPF 80 LR4, HPF 27 Hz BW4 (vents open) | 0 ms | |
| 4 | R-LF | | JMOD-R | 1± | 4 Ω | as L-LF | as L-LF | |
| 5 | R-COAX | | JMOD-R | 2± (FB464) | 16 Ω | as L-COAX | as L-COAX | |
| 6 | SUB-B | | SKRAM-3 (+ 4) in the centre cluster | 1± | 4 Ω | as SUB-A | as SUB-A | |

### A.2 Limiter calculation

| Output | Driver and load | Nominal W | Program W | Driver RMS V | Driver peak V | Amp model | Amp gain (dB / ×) | Amp max V | Set RMS V | Set peak V | Processor dBu (RMS / peak) | Attack / release |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| L-LF | 2 × 12NDL88 (4 Ω) | 1,400 | 2,800 | 74.8 | 105.8 | | | | | | | |
| L-COAX | DCX464 (16 Ω) via FB464, shared channel | mid 110 / HF 80 | mid 220 / HF 160 | start 35 (ceiling 42) | start 50 (ceiling 59) | | | | | | | RMS 800 ms / 2,400 ms; peak 2.7 ms / 21 ms |
| SUB-A | 21DS115 (8 Ω, one, or 2 in parallel) | 1,700 | 3,400 | 116.6 | 164.9 | | | | | | | |

### A.3 Alignment log

| Date | Arrangement | Stack | Sub-to-top delay (ms, on tops) | Polarity | Crossover (Hz) | Sub gain (dB) | Mic position | Temperature | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

### A.4 Measurement log

| File name | Date | Cabinet ID | Band / vent setting | Mic position and distance | Processing on | Level | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |

### A.5 Preset record

| Preset name | Date | Who | Purpose | Outputs changed | Reason | Backup file | Verified by measurement |
| --- | --- | --- | --- | --- | --- | --- | --- |

### A.6 Event checklist

One page version of §14. Print and tick off.

## BQuick maths

| Task | Formula | Example |
| --- | --- | --- |
| Watts to volts | V = √(P × R) | 1,400 W into 4 Ω = 74.8 V |
| Volts to dBu | dBu = 20·log₁₀(V / 0.775) | 1.88 V = +7.7 dBu |
| Amp gain, dB to ratio | ratio = 10^(dB / 20) | 32 dB = ×39.8 |
| Speaker volts to processor volts | V_dsp = V_speaker / ratio | 75 V ÷ 39.8 = 1.88 V |
| Delay to distance | d = c × t, c ≈ 343 m/s | 1 ms = 0.343 m |
| Distance to delay | t = d / c | 1 m = 2.91 ms |
| Phase from delay | φ = 360° × f × Δt | 80 Hz, 1 ms = 28.8° |
| Speed of sound | c ≈ 331.3 + 0.606 × T(°C) | 20 °C = 343.4 m/s |
| Sum of two equal signals, phase difference φ | Level vs one signal = 20·log₁₀(2·cos(φ/2)) | 0° = +6 dB, 90° = +3 dB, 120° = 0 dB, 180° = null |
| Cable loss | R = 0.0172 × L × 2 / A (Ω, L in m, A in mm²) | 10 m of 2.5 mm² = 0.14 Ω |
| Level change per doubling of distance | −6 dB in free field | |

## CGlossary

**AES power**: a loudspeaker's nominal power handling under a standard long-term pink noise test. **Alignment**: choosing delay and polarity so two sources add properly. **Amp gain**: the voltage amplification of the amplifier, in dB. **BU (Butterworth)**: a filter type with a flat passband. **Clip**: a signal exceeding what a stage can pass, flattening its peaks. **Crest factor**: the ratio of peak to RMS level. **Crossover**: a filter set that splits a signal into bands. **dBu / dBV / dBFS / dB SPL**: see §3.1. **FIR / IIR**: filter families; IIR changes phase, FIR can correct it at the cost of latency. **Gain structure**: sharing level across stages so none clips early or adds avoidable noise. **Ground plane**: a measurement method with the cabinet and mic on the ground. **Group delay**: how much each frequency is delayed; large near a sub's tuning. **Impulse response**: a speaker's response to a click; the basis of measurement. **Limiter (peak, RMS)**: protection that holds level below a ceiling; the RMS version responds to sustained heat. **LR (Linkwitz–Riley)**: a crossover type that sums flat. **Mono sum**: left plus right combined. **Null**: a deep dip where two signals cancel. **PEQ**: parametric equaliser. **Phase**: timing offset in degrees, varying with frequency. **Polarity**: signal inversion, 180° at all frequencies. **Power alley**: interference between separated subs playing the same bass. **RTA**: real-time spectrum display. **Subsonic filter**: a high-pass that protects a sub below its tuning. **Timing reference**: a signal that lets a measurement system share absolute timing. **Tuning (box)**: the frequency at which a vented or horn cabinet's output peaks and its cone motion is smallest. **Voicing**: setting a cabinet's EQ to the designer's target.

## DSources and open checks

### What this guide is built from

- The JMOD 2.02 design guide (John White, JW Sound): published DSP settings, limiter table, wiring diagrams, ground-plane measurement note, measurement and targets charts, and the REW measurement file.
- The SKRAM information from Josh Ricci's forum thread, and the cut sheet: dimensions, vent tunings.
- B&C's published power-handling definitions.
- Reference documents on gain structure, limiter setting and measurement, listed below.
- **New in v2:** the filter sets and trace notes stored inside JW's REW file, read directly (§6.2, §8.4); B&C's product pages for the DCX464, FB464, 12NDL88 and 21DS115; JW Sound's SKRAM page; owner reports on SKRAM high-pass settings (§6.3).

### Web sources checked, 11 Oct 2026 (added in v2)

- B&C product pages: [DCX464 16 Ω](https://www.bcspeakers.com/en/products/coaxials-hf/1-4/16/DCX464-16) (110 / 220 W mid, 80 / 160 W HF, four M6 on Ø102 mm), [FB464 16 Ω](https://www.bcspeakers.com/en/products/crossovers/0/16/FB464) (3.6 kHz, 18 to 12 dB per octave, bulb protection, no power rating), [12NDL88](https://www.bcspeakers.com/en/products/lf-driver/12/8/12NDL88), [21DS115](https://www.bcspeakers.com/en/products/lf-driver/21/8/21DS115)
- [FB464V2 16 Ω, no bulbs, higher power (Toutlehautparleur)](https://en.toutlehautparleur.com/2-way-fb4648v2-crossover-for-b-c-speakers-dcx464-and-dcx462-16-16-ohm-3600-hz-18-12-db-octave-more-power-handling-without-light-bulb-protection.html)
- [JW Sound: Ricci's SKRAM](https://www.jwsound.live/designs/riccis-skram-subwoofer), [JMOD](https://www.jwsound.live/designs/jmod), [JMOD-M](https://www.jwsound.live/designs/jmodm-medium-format-array)
- [Powersoft M50Q](https://www.powersoft.com/en/products/touring-amps/m-series/m50q/) and [K3](https://www.powersoft.com/en/products/touring-amps/k-series/k3/) pages (clip limiter, long-term limiter, end of life); [M-series DSP summary (ProSoundWeb)](https://www.prosoundweb.com/powersoft-introduces-m-series-dspeth-amplifiers/)
- [Crown XTi 4002 listing (Kirstein)](https://www.kirstein.de/it/Live-Studio/Finali/Crown-XTI-4002.html) and [XTi 6002 listing (zZounds)](https://www.zzounds.com/item--CWNXTI6002) for the Peak X Plus limiter and filter lists (retailer data, not the manual)
- [miniDSP Flex Eight signal flow](https://docs.minidsp.com/product-manuals/flex-eight/signal-flow/index.html) (per-output compressor) and [the "+12 dB is 0 dBFS" forum explanation](https://www.minidsp.com/community/threads/relation-between-gain-setting-and-compression-threshold.20762/latest)
- dbx DriveRack 4800 features via [SVC Online](https://www.svconline.com/?p=92038) and the [4800 manual](https://manualmachine.com/dbx/4800/339100-user-manual/)
- Owner reports on SKRAM high-pass settings: AVS Forum threads ["Ricci's Skram"](https://www.avsforum.com/threads/riccis-skram.3058134/) and ["YES! I finally have end game SKRAM subwoofers"](https://www.avsforum.com/threads/yes-i-finally-have-end-game-skram-subwoofers.3330961/), read only as search-result summaries
- [Neutrik NL8MPR / NL4MP cutout drawing summary](https://www.farnell.com/cad/3475533.pdf)

### Web sources checked, 09 Oct 2026

- [B&C power handling definitions](https://bcspeakers.com/en/products-overview/power-handling)
- [Gain structure basics (ProSoundWeb)](https://www.prosoundweb.com/the-basics-of-audio-system-gain-structure/)
- [Calibrating limiters against an amplifier (Danley Sound Labs, Amp Note 011)](https://www.danleysoundlabs.com/wp-content/uploads/2024/02/Amp-Note-011-Calibrating-the-Limiters-on-the-DNA-SC48-with-an-amplifier-attached.pdf)
- [Ground plane measurements (Pat Brown, Pro Sound Training)](https://www.prosoundtraining.com/?p=16413)
- [REW: making measurements](https://www.roomeqwizard.com/help/help_en-GB/html/makingmeasurements.html), [checking levels](https://www.roomeqwizard.com/help/help_en-GB/html/measurementlevel.html), [soundcard and USB mic setup](https://www.roomeqwizard.com/help/help_en-GB/html/calsoundcard.html), [alignment tool](https://www.roomeqwizard.com/betahelp/help/html/graph_allspl.html)
- [Linkwitz–Riley filter](https://en.wikipedia.org/wiki/Linkwitz%E2%80%93Riley_filter)
- [NIOSH noise exposure](https://www.cdc.gov/niosh/noise/about/noise.html)
- [The "power alley" (Fulcrum Acoustic)](https://fulcrum-acoustic.com/education/the-power-alley-a-k-a-troubling-interactions-of-subwoofers)
- [Speed of sound and temperature (Sengpiel Audio)](https://sengpielaudio.com/TemperatureSound.htm)
- [UMIK-1 file choice (miniDSP)](https://support.minidsp.com/support/solutions/articles/47000681633-which-direction-should-i-point-the-umik-1)

### Not verified, and what would verify it

| Open item | How to close it |
| --- | --- |
| SKRAM subsonic filter corner (now 27 Hz BW4 with all vents open, from owner reports; designer silent) | Ask JW or Ricci; confirm by the three checks in §6.3 on the built cabinets |
| SKRAM limiter values for our actual amps | §7 after the amps are chosen |
| FB464 route limiter values (start RMS 35 V, peak 50 V; derived in §6.1) and the coax's relative level | §8.4 and §11 measurement; compare the coax with the 500 Hz flat target |
| Whether JW's own hardware preset uses the .mdat filters (640 Hz mid boost; 6 kHz +5 dB Q5 and 8 kHz +2.5 dB Q2.5) | Ask JW; measure our build |
| Which side of the FB464 carries 18 dB per octave | The standard FB464 page does not say; the V2 datasheet summary says 18 dB low-pass, 12 dB high-pass, same circuit. Read B&C's PDF datasheet and measure the coax |
| DIN 15905-5 (2022) limits | The standard itself, and the permit conditions for each venue |
| Whether the chosen processor can sum L+R | Its manual, before purchase; not verified for any candidate (§2) |
| Crown XTi: RMS limiter, LR2, filter counts | The Crown manual; the data here is from retailer listings |
| Powersoft K3 DSP and M-series DSP: limiter details, LR2, Armonía support for end-of-life units | Powersoft manuals; the K3 page does not say |
| miniDSP 4x10 HD: any limiter or compressor | The product manual |
| Behaviour of REW's acoustic timing reference with our mic and laptop | Try it in the first session; Method B is the fallback |
| Everything marked [Start] | Measurement on the built cabinets |
