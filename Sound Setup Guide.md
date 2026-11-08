Working guide · 8 November 2026 · For group review

# Sound setup

This guide starts with **one JMOD**, then adds a SKRAM. The [build plan](SKRAM%20%2B%20JMOD%20Build%20Plan.md) covers the cabinets and budget. Use the designer's files and the actual amplifier's manual alongside this guide.

**There is no verified ready-to-use preset for our planned bi-amped JMOD yet.** Before connecting the drivers, an experienced person must check the wiring, filters and protection for the actual amplifier and crossover. Calculated settings or a measurement microphone alone do not prove the drivers are protected.

## How the first JMOD connects

The planned JMOD contains two 8 Ω B&C 12NDL88 drivers, one 16 Ω DCX464 compression driver and a matching 16 Ω FB464 passive crossover.

- **Amp channel 1:** the two 12-inch drivers, wired in parallel, present a nominal 4 Ω load.
- **Amp channel 2:** the compression driver through the FB464, nominally 16 Ω.
- The FB464 divides the compression driver's mid and high sections. It does **not** divide the signal between those sections and the 12-inch drivers; that needs processing in the amplifier or a separate processor. [JMOD designer's explanation](https://www.diyaudio.com/community/threads/jmod-v2-build-thread.429672/page-6)

Use two independently processed channels per JMOD. A stereo pair needs four; a SKRAM needs its own channel. A four-pole speaker cable can carry both JMOD channels, but its pinout and any amp-rack breakout or patch panel must be checked against the actual equipment and designer's wiring diagram. Do not assume every socket is wired the same way.

## Before buying amplification

Choose an amplifier and processor combination that can handle the loads above and provides the required crossover filters, equalisation, delay, polarity control and independently adjustable driver protection. The **CVR DSP-1504 with Dante** is a candidate; the exact unit's limiter behaviour and the finished bi-amp setup remain unverified. A separate processor may be needed. A second JMOD can use the other two channels of a suitable four-channel amp; the SKRAM will eventually need separate amplification.

The Crown XTi's published crossover menu does not offer the JMOD's 12 dB Linkwitz–Riley filter directly, and its documentation does not list a separate RMS limiter. Do not assume its onboard processing alone meets this design. [Crown crossover documentation](https://adn.harmanpro.com/static/archimedia/aa_help/Device_Help_Files/Crown_Modules/XTi_2_Series/XTi2_Crossover_Settings_Overview.htm)

## Before the first sound

1. Check the cabinet is sealed, the FB464 matches the driver's impedance, and cables, connectors and polarity match the designer's diagrams. Label every channel and cable. Make electrical checks with the equipment off.
2. Prepare the processing for each output. The designer publishes an **80 Hz high-pass and 195 Hz low-pass** for the JMOD woofer section; these are starting references, not a complete verified preset for the FB464 version. The planned shared compression-driver channel needs its own filters and protection. [JMOD plans](https://www.jwsound.live/designs/jmod)
3. Have an experienced person set and verify peak and sustained-level protection for the exact drivers and amplifier, including the compression driver behind the passive crossover. The standard FB464 has protective bulbs; the FB464V2 does not. Neither replaces a verified setup.
4. Use a calibrated measurement microphone, its calibration file, a laptop with REW, and a suitable audio output to measure the finished speaker. A USB mic such as the UMIK-1 does not need a separate microphone interface, but the laptop still needs a way to send the test signal to the amplifier. [UMIK and REW setup](https://www.minidsp.com/applications/acoustic-measurements/umik-1-setup-with-rew/)
5. Start at low level after the checks. Measure the JMOD, adjust with the help of the person setting it up, and save the final settings and measurements. The designer notes that results depend on the drivers, amp, processing and build.

The previously inspected JMOD measurement file and printed guide differ on some mid/high EQ details. The original files are not in this checkout; obtain the current designer package and check the source before using those values. The designer does not supply a complete FB464 bi-amp preset in the published guide.

## When we add a SKRAM

The planned SKRAM has one 8 Ω B&C 21DS115. It needs an amp channel, a low-frequency protective filter and a limiter configured for the driver, cabinet and amp. The correct settings for our cabinet and its adjustable vents are **not yet established**; do not treat a general online setting as verified.

Place the sub and top as planned, then measure their combined response and adjust their relative level and timing. With a second JMOD, send left and right to the separate tops; subs can receive a properly levelled mono sum. Save settings for the actual arrangement.

## Using the system

- Check the cabinets, stands, ventilation, cables and saved settings before each use.
- Turn on the source and processor first, amplifiers last; reverse the order when shutting down.
- Keep levels down while checking each channel. If there is distortion, unexpected noise or persistent limiter activity, turn down and investigate.
- Keep a copy of the verified settings and measurement files; agree who may change them.

For the designer's guidance, see [JMOD](https://www.jwsound.live/designs/jmod), [SKRAM](https://www.jwsound.live/designs/riccis-skram-subwoofer) and the [JMOD build thread](https://www.diyaudio.com/community/threads/jmod-v2-build-thread.429672/). The original designer packages are not included in this checkout.
