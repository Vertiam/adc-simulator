# ADC Resolution & Noise Simulator
### Hackathon Project #19 — Signal Processing & Digital Electronics

> **Visualize how analog signals become digital data — and how oversampling recovers lost quality.**  
> An interactive, browser-based simulator that makes the invisible world of Analog-to-Digital Conversion tangible.

<br>

---

## 🌐 Live Demo

🔗 **[https://vertiam.github.io/adc-simulator/](https://vertiam.github.io/adc-simulator/)**

---

<br>

## 📋 Table of Contents

- [What This Project Does](#-what-this-project-does)
- [The Problem We're Solving](#-the-problem-were-solving)
- [Technologies Used](#-technologies-used)
- [Core Concepts Explained](#-core-concepts-explained)
  - [Analog vs Digital](#1-analog-vs-digital)
  - [ADC — How It Works](#2-adc--how-it-works)
  - [Bit Depth & Quantization Levels](#3-bit-depth--quantization-levels)
  - [Quantization Noise](#4-quantization-noise)
  - [Signal-to-Noise Ratio (SNR)](#5-signal-to-noise-ratio-snr)
  - [Oversampling](#6-oversampling)
  - [Effective Number of Bits (ENOB)](#7-effective-number-of-bits-enob)
- [The Algorithm — How the Code Works](#-the-algorithm--how-the-code-works)
- [Features](#-features)
- [How to Use](#-how-to-use)
- [Real-World Applications](#-real-world-applications)
- [Project Structure](#-project-structure)
- [Team](#-team)

<br>

---

## What This Project Does

This simulator lets you **see** what happens inside an ADC chip in real time. You control:

- How many **bits** the ADC uses to encode each sample
- How much **oversampling** is applied
- What **type of signal** is being converted (sine, square, sawtooth, or your own CSV data)
- How much **background noise** is present before conversion

The simulator then shows you three live charts:
1. The **original vs quantized waveform** — see the staircase effect
2. The **quantization error** — see the actual noise introduced
3. The **SNR vs bit depth curve** — see where you sit on the theoretical limit

<br>

---

## The Problem We're Solving

**Problem Statement #19:**
> *Analog-to-digital conversion introduces quantization noise. Simulate ADC digitization effects and study how oversampling improves signal quality.*

Every sensor, microphone, camera, and smart device converts real-world signals into digital numbers. This conversion is **never perfect** — it always introduces error. Understanding this error, and knowing how to reduce it (through techniques like oversampling), is fundamental to electronics and signal processing.

This project makes that abstract concept **visual, interactive, and intuitive**.

<br>

---

## Technologies Used

| Technology | Purpose | Why We Chose It |
|---|---|---|
| **HTML5** | Structure of the web app | Universal browser support, no install needed |
| **CSS3** | Styling, layout, animations | Full control over the dark monochromatic UI design |
| **JavaScript (ES6+)** | All simulation logic and interactivity | Runs entirely in the browser — no server needed |
| **Chart.js** | Drawing the three live charts | Lightweight, fast, easy to update in real time |
| **JetBrains Mono** | Monospace font for data values | Conveys technical/engineering aesthetic |
| **DM Sans** | Body font for labels and prose | Clean readability at small sizes |
| **GitHub Pages** | Free static site hosting | Zero cost, auto-deploys on every commit |

> **Note:** This project intentionally uses no Python, no backend server, and no build tools. Everything runs as a single `.html` file in the browser. This makes it instantly shareable — just open the file or visit the URL.
>
> *The mention of Python/Matplotlib in the project brief refers to the algorithmic concepts (which we implement in JavaScript) — the same mathematics applies regardless of language.*

<br>

---

## Core Concepts Explained

### 1. Analog vs Digital

The real world is **analog** — signals like sound, temperature, and voltage are smooth and continuous. They can take literally any value at any instant.

Computers are **digital** — they can only store a finite set of discrete numbers. They cannot store `3.14159265...` forever; they must round it.

```
Analog:   ~~~smooth wave, infinite precision~~~
Digital:  [  1  |  2  |  4  |  3  |  5  |  4  ]  ← rounded steps
```

The **ADC (Analog-to-Digital Converter)** is the chip that bridges this gap.

---

### 2. ADC — How It Works

An ADC performs two operations on every signal sample:

**Sampling** — It takes a snapshot of the voltage at regular time intervals. How often it does this is the **sample rate** (measured in Hz or samples per second).

```
Sample rate examples:
  CD Audio     → 44,100 samples/sec
  Phone call   →  8,000 samples/sec
  Medical ECG  →    500 samples/sec
```

**Quantization** — It rounds each snapshot to the nearest available digital level. This rounding is where the imperfection enters.

---

### 3. Bit Depth & Quantization Levels

Bit depth (also called resolution) determines how many discrete levels the ADC can produce. The formula is:

```
Number of levels = 2ⁿ    (where n = number of bits)
```

| Bit Depth | Levels | Typical Use Case |
|---|---|---|
| 4-bit | 16 | Old video game audio |
| 8-bit | 256 | Telephony, basic microcontrollers |
| 12-bit | 4,096 | Sensors, IoT devices |
| 16-bit | 65,536 | CD audio, professional audio |
| 24-bit | 16,777,216 | Studio recording |

More levels = smaller rounding error = cleaner signal.

---

### 4. Quantization Noise

When the ADC rounds a sample to the nearest level, the difference between the **true value** and the **rounded value** is called the **quantization error**. This error manifests as noise in the output.

```
True value:       0.732 V
Nearest level:    0.750 V  (at 4-bit resolution)
Quantization error: 0.018 V  ← this IS the noise
```

The noise is spread across all samples and you hear it as **hiss**, **crackle**, or **distortion** in audio, or as **inaccuracy** in sensor readings.

Mathematically, the quantization error `e` is bounded:
```
-step/2 ≤ e ≤ +step/2     where step = 2 / 2ⁿ
```

---

### 5. Signal-to-Noise Ratio (SNR)

SNR measures how much louder the signal is compared to the noise, in decibels (dB). Higher is better.

```
Theoretical SNR formula:
  SNR ≈ 6.02 × n + 1.76   (dB)
  where n = number of bits
```

| Application | Typical SNR |
|---|---|
| AM Radio | ~40 dB |
| FM Radio | ~60 dB |
| CD Audio | ~96 dB |
| Studio Recording | ~120+ dB |

Every additional bit adds approximately **6 dB of SNR** — doubling the number of levels halves the noise.

---

### 6. Oversampling

Oversampling is a clever technique to get better quality from cheaper hardware. Instead of taking one sample at the required rate, the ADC takes **many samples faster than needed**, then **averages them together**.

```
Normal (1×):    [sample] → quantize → output
                 Error stays

4× Oversample:  [s1][s2][s3][s4] → quantize each → average → output
                 Random errors partially cancel out
```

**Why does averaging reduce noise?**

The quantization errors on each super-sample are statistically independent and randomly distributed. When you average `M` independent random values, the variance drops by factor `M` and the amplitude (standard deviation) drops by `√M`.

Since `M = osRate`, and we need 4× to gain one bit (because `√4 = 2`, and halving noise amplitude ≈ +6 dB ≈ +1 bit):

```
Golden Rule: Every 4× oversampling = +1 effective bit of resolution
```

With oversampling, the full SNR formula becomes:
```
SNR = 6.02 × n + 1.76 + 10 × log₁₀(osRate)   (dB)
```

---

### 7. Effective Number of Bits (ENOB)

ENOB combines your hardware bit depth with the oversampling gain into one number:

```
ENOB = n + (log₂(osRate) / 2)
```

Example: A 12-bit ADC with 16× oversampling achieves:
```
ENOB = 12 + (log₂(16) / 2) = 12 + 2 = 14 effective bits
```

This is the principle behind **sigma-delta ADCs** used in smartphones and streaming audio — cheap 1-bit hardware with extreme oversampling achieves 24-bit quality.

<br>

---

## The Algorithm — How the Code Works

The entire simulation runs in JavaScript. Here is the step-by-step breakdown:

### Step 1 — Signal Generation (`genSignal`)

```
Inputs:  N (number of points), waveform type, frequency
Output:  Array of N values in the range [-1, +1]
```

Four waveform modes are supported:

```javascript
Sine:     signal[i] = sin(2π × freq × i/N)
Square:   signal[i] = sign(sin(2π × freq × i/N)) × 0.9
Sawtooth: signal[i] = 2 × frac(freq × i/N) - 1
CSV:      signal[i] = lerp(csvData, i/N)   ← linear interpolation
```

**Why these waveforms?**
- Sine = single frequency, easy to analyse
- Square = hard transitions, worst case for ADCs
- Sawtooth = rich harmonics, exercises full dynamic range
- CSV = real sensor data (ECG, audio, temperature readings)

---

### Step 2 — Noise Floor Injection

```javascript
noisy[i] = original[i] + (random() - 0.5) × 2 × noiseAmplitude
```

Uniform random noise is added before quantization to simulate real-world interference (thermal noise, EMI, power supply ripple). This gets quantized along with the signal.

---

### Step 3 — Midtread Uniform Quantization

```
step = 2 / 2ⁿ              ← size of one level in [-1, +1]
Q[i] = round(x[i] / step) × step
```

This is **midtread uniform quantization** — the standard algorithm inside every real ADC chip. Each sample is snapped to the nearest multiple of `step`. The rounding error is uniformly distributed in `[-step/2, +step/2]`, which matches the theoretical SNR formula exactly.

---

### Step 4 — Oversampling + Decimation (when osRate > 1)

```
1. Generate N × osRate super-samples of the same signal
2. Add independent noise to each super-sample
3. Quantize every super-sample with the same midtread rule
4. Average every group of osRate consecutive quantized values
   back down to N output points
```

```javascript
for (let i = 0; i < N; i++) {
  let sum = 0;
  for (let j = 0; j < osRate; j++) {
    sum += quantized_super_samples[i × osRate + j];
  }
  output[i] = sum / osRate;   // ← the averaging step
}
```

The noise cancellation comes from **statistical independence** of rounding errors. Each super-sample is quantized at a slightly different point in time, so its rounding direction is independent. Averaging independent random variables reduces their combined variance.

---

### Step 5 — Error & Metrics Calculation

```javascript
error[i]  = quantized[i] - original[i]     // quantization noise at each point
RMS       = sqrt( mean( error[i]² ) )       // root mean square error
SNR       = 6.02×bits + 1.76 + 10×log₁₀(osRate)   // theoretical dB
ENOB      = bits + osRateExp / 2            // effective resolution
```

### Step 6 — Live Chart Updates

All three Chart.js charts update on every slider move with `chart.update('none')` (no animation) to keep the response instant and smooth.

<br>

---

## Features

- **Adjustable Bit Depth** — drag from 2-bit (16 levels) to 16-bit (65,536 levels)
- **Oversampling Control** — 1× up to 64× in powers of 2
- **4 Signal Modes** — Sine, Square, Sawtooth, and your own CSV data
- **CSV Upload** — drag and drop any `.csv` file with real sensor data
- **Noise Floor Slider** — simulate real-world interference before the ADC
- **3 Live Charts** — waveform, error signal, and SNR curve
- **Hover Tooltips** — every technical term has a plain-English explanation
- **Signal Quality Meter** — real-time quality indicator (Poor → Studio)
- **Live Metrics** — quantization levels, SNR (dB), and ENOB update instantly
- **Single File** — the entire app is one `.html` file, no install needed

<br>

---

## How to Use

### Running Locally

No setup required. Just download the file and open it:

```bash
# Option 1: double-click index.html in your file manager

# Option 2: from terminal
open index.html         # macOS
start index.html        # Windows
xdg-open index.html    # Linux
```

### Using the Simulator

```
1. Choose a waveform type (Sine / Square / Sawtooth / CSV)
2. Drag the Bit Depth slider left to reduce quality, right to improve
3. Watch the staircase appear in the waveform chart
4. Drag Oversampling up and see the noise reduce
5. Observe the orange dot move along the SNR curve
6. Try uploading a CSV of real data (one number per line)
```

### CSV Format

The CSV upload accepts:

```
# Single column (value only)
0.123
-0.456
0.789

# Two columns (time, value)
0.0, 0.123
0.001, -0.456
0.002, 0.789
```

Data is automatically normalized to the `[-1, +1] ` range regardless of your original scale.

<br>

---

## Real-World Applications

| Domain | How ADC Quality Matters |
|---|---|
| **Music & Audio** | CD uses 16-bit 44.1kHz. Studio uses 24-bit. Noise = audible hiss |
| **Medical Devices** | ECG, pulse oximeters, MRI scanners — a noisy sample = wrong diagnosis |
| **Smartphones** | Every mic, touch screen, and camera sensor has an ADC inside |
| **Communication** | AM/FM radio, 5G — quantization noise limits transmission quality |
| **IoT Sensors** | Temperature, pressure, humidity sensors all use ADCs |
| **Scientific Instruments** | Oscilloscopes, spectrum analysers — precision depends on ADC resolution |
| **Gaming** | Controller analog sticks, audio — 8-bit feels 'lo-fi', 16-bit is clean |

<br>

---

## 📁 Project Structure

```
adc-simulator/
│
├── index.html          ← The entire application (HTML + CSS + JS)
│
└── README.md           ← This file
```

The project is intentionally a **single self-contained file**. Every function, style, and chart is inside `index.html`:

```
index.html
├── <style>             CSS variables, layout, controls, tooltip system
├── #g-tip              Global JS-positioned tooltip (bypasses overflow clipping)
├── <header>            Title + hover-explainer terms
├── .grid-main          Two-column layout (controls | charts)
│   ├── Left column
│   │   ├── Stats row   (Levels, SNR, ENOB cards)
│   │   ├── Quality bar (Poor → Studio gradient)
│   │   ├── Signal source panel  (Sine/Square/Sawtooth/CSV tabs)
│   │   └── ADC settings panel   (Bit depth, Oversampling, Noise floor)
│   └── Right column
│       ├── Waveform chart   (Original vs Quantized)
│       ├── Error chart      (Quantization noise signal)
│       └── SNR chart        (Theory curve + current dot)
└── <script>
    ├── Tooltip engine   (getBoundingClientRect + fixed positioning)
    ├── genSignal()      Signal generation (sine/square/sawtooth/CSV)
    ├── buildData()      Quantization + oversampling algorithm
    ├── update()         Reads sliders → calls buildData → updates charts
    └── initCharts()     Chart.js setup for all three graphs
```

<br>

---

## Key Formulas Reference

```
Quantization Levels    =  2ⁿ
Quantization Step Size =  Full Scale Range / 2ⁿ
Quantization Error     ∈  [-step/2, +step/2]

Theoretical SNR        =  6.02n + 1.76                      (dB, no oversampling)
SNR with Oversampling  =  6.02n + 1.76 + 10·log₁₀(osRate)  (dB)
Oversampling Gain      =  10·log₁₀(osRate)                  (dB)

ENOB                   =  n + log₂(osRate)/2
Golden Rule            :  4× oversampling  ≡  +1 bit  ≡  +6 dB SNR

RMS Noise              =  step / √12    (for uniform quantization)
```

<br>

---

## 👥 Team

**Team Name: Qt π's**
**Hackathon Project Track #4 PS_19** — ADC Resolution, Noise & Oversampling Simulator
**Department:** Mechanical Engineering

| Role | Name | Registration No. |
|---|---|---|
| **Team Leader** | Swayam Viral Marfatia | RA2511002010080 |
| **Member** | Narayan Murthy | RA2511002010124 |
| **Member** | Shirly Oviya | RA2511054010030 |

Built to make signal processing concepts accessible through interactive visualisation.

---

<br>

> *"The goal is to turn invisible noise into something you can see, drag a slider, and understand."*
> — **Qt π's**

---
