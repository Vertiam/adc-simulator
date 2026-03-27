# ⚡ ADC Resolution & Noise — Signal Processing Lab
### Hackathon Project #19 — Signal Processing & Digital Electronics

> **A full browser-based laboratory for studying Analog-to-Digital Conversion.**  
> Record real signals, run controlled experiments, log data, write observations, and export a complete lab report — no installation required.

<br>

---

## 🌐 Live Website

🔗 **[https://vertiam.github.io/adc-simulator/](https://vertiam.github.io/adc-simulator/)**

| Page | URL | Description |
|---|---|---|
| 🏠 Landing Page | `/` or `/index.html` | Project overview, theory, and experiment guide |
| 🔬 Lab Environment | `/lab.html` | Full 5-step interactive experiment |

---

<br>

## 📋 Table of Contents

- [What This Project Does](#-what-this-project-does)
- [The Problem We're Solving](#-the-problem-were-solving)
- [Technologies Used](#-technologies-used)
- [Website Structure](#-website-structure)
- [Lab Workflow — All 5 Steps](#-lab-workflow--all-5-steps)
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
- [Project File Structure](#-project-file-structure)
- [Key Formulas Reference](#-key-formulas-reference)
- [Team](#-team)

<br>

---

## 🎯 What This Project Does

This is a **complete digital laboratory** for signal processing experiments. It goes far beyond a simple simulator — it is a structured, end-to-end lab experience designed for students to:

- **Record real audio** from a microphone and feed it through a virtual ADC
- **Control ADC parameters** — bit depth (2–16 bit) and oversampling (1× to 64×)
- **Observe the effects live** — staircase waveform, quantization noise, SNR curve
- **Log experimental readings** into a data table with notes
- **Write up a full lab notebook** — aim, theory, observations, conclusion
- **Export a complete lab report** as a printable/CSV document

Everything runs in a web browser. No Python, no MATLAB, no installation.

<br>

---

## 🔍 The Problem We're Solving

**Problem Statement #19:**
> *Analog-to-digital conversion introduces quantization noise. Simulate ADC digitization effects and study how oversampling improves signal quality.*

Every sensor, microphone, camera, and smart device converts real-world signals into digital numbers. This conversion is **never perfect** — it always introduces error. Understanding this error, and knowing how to reduce it through oversampling, is fundamental to electronics and signal processing.

This project makes that abstract concept **visual, interactive, and academically rigorous** — structured exactly like a real lab session.

<br>

---

## 🛠 Technologies Used

| Technology | Purpose | Why We Chose It |
|---|---|---|
| **HTML5** | Page structure for all three files | Universal browser support, zero install |
| **CSS3** | Shared design system (`style.css`) | Dark monochromatic UI, consistent across pages |
| **JavaScript (ES6+)** | All simulation logic, recording, data management | Runs entirely in browser — no server needed |
| **Web Audio API** | Microphone recording and PCM decoding | Native browser API, no libraries needed |
| **MediaRecorder API** | Capturing audio stream to blob | Standard, works on all modern browsers |
| **Chart.js v4** | Three live interactive charts | Lightweight, real-time updates with `update('none')` |
| **localStorage** | Auto-saving student data between sessions | Built into every browser, no database needed |
| **JetBrains Mono** | Monospace font for data values | Technical/engineering aesthetic |
| **DM Sans** | Body font for readable prose | Clean at small sizes |
| **GitHub Pages** | Free static site hosting | HTTPS required for microphone, auto-deploys on push |

 
> The project brief references these as concept tools. We implement the identical mathematics — midtread quantization, oversampling decimation, SNR calculation — in JavaScript so it runs live in the browser without any local setup. The algorithms are the same; the runtime is different.

<br>

---

##  Website Structure

The project is split into **3 files** that work together:

```
adc-simulator/
│
├── index.html     ← Landing page (theory, objectives, experiment overview)
├── lab.html       ← Full 5-step lab environment
├── style.css      ← Shared design system used by both HTML files
│
└── README.md      ← This file
```


> ⚠️ **Microphone recording requires HTTPS.** GitHub Pages provides this automatically. It will NOT work if you open `lab.html` as a local `file://` URL — use the hosted link.

<br>

---

## 🔬 Lab Workflow — All 5 Steps

The lab is structured as a guided 5-step experiment, accessible via the step bar at the top of `lab.html`.

### Step 1 — Student Setup
Students enter their details before beginning:
- Full name, registration number, department
- Date, experiment title, section/batch

This information is stored in `localStorage` and automatically appears in the final report. The form auto-saves every 10 seconds, so students can close the browser and return later.

---

### Step 2 — Signal Source
Three ways to provide the input signal:

**🎤 Microphone Recording**
- Uses `navigator.mediaDevices.getUserMedia()` to capture audio
- `MediaRecorder` records to a WebM blob
- `AudioContext.decodeAudioData()` decodes the blob to raw PCM float samples
- Samples are normalized to `[-1, +1]` and stored in memory
- A live waveform visualiser (`AnalyserNode + Canvas`) shows the recording in real time
- Configurable recording duration (2–10 seconds)

**⚡ Signal Generator**
- Four waveform types: Sine, Square, Sawtooth, Chirp (frequency-swept sine)
- Configurable frequency (1–8 Hz) and amplitude (10–100%)
- A canvas preview updates live as you adjust parameters

**📂 CSV Upload**
- Drag and drop or file picker
- Accepts single-column (values) or two-column (time, value) format
- Tab, comma, or semicolon delimited
- Auto-normalized to `[-1, +1]` regardless of original scale
- Linearly resampled to 250 points for the simulator

---

### Step 3 — Run Experiments
The core simulation environment. Three live charts update in real time:

1. **Waveform chart** — Original (blue, smooth) vs Quantized (orange, stepped). An orange fill shades the gap between them, making the error visible even at high bit depths. Dashed horizontal level-lines appear at ≤7-bit depth, showing exactly which level each sample snaps to.

2. **Quantization Error chart** — The raw difference between original and quantized at every sample. This is the noise signal itself. RMS error is displayed live.

3. **SNR vs Bit Depth chart** — The theoretical SNR curve for the current oversampling rate, with an orange dot marking the student's exact current operating point.

**Recording readings:** A "Record This Reading" button logs the current settings (bits, oversampling, noise floor, levels, SNR, ENOB, RMS error) into a persistent data table. Students can add inline notes to each row, delete individual rows, or export the full table as CSV.

---

### Step 4 — Lab Notebook
A structured notebook with six pre-labelled sections:
- **Aim** — Pre-filled with the standard experiment aim (editable)
- **Apparatus** — Equipment list (editable)
- **Theory** — Pre-filled with key formulas and explanations (editable)
- **Observations** — Student fills this in based on what they saw
- **Analysis & Calculations** — Compare measured vs theoretical SNR
- **Inference & Conclusion** — Final conclusions

All fields auto-save to `localStorage`.

---

### Step 5 — Report
A fully assembled lab report generated from all previous steps:
- Student information header (from Step 1)
- Complete experimental data table (from Step 3)
- All six notebook sections (from Step 4)

Students can print directly (`window.print()` with print-specific CSS that hides navigation) or export a full CSV containing all metadata, data, and notebook text.

<br>

---

##  Core Concepts Explained

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

Bit depth determines how many discrete levels the ADC can produce:

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

---

### 4. Quantization Noise

When the ADC rounds a sample to the nearest level, the difference between the **true value** and the **rounded value** is the quantization error. This IS the noise.

```
True value:         0.732 V
Nearest level:      0.750 V  (at 4-bit resolution)
Quantization error: 0.018 V  ← this IS the noise
```

Mathematically, the error `e` is bounded:
```
-step/2 ≤ e ≤ +step/2     where step = 2 / 2ⁿ
```

---

### 5. Signal-to-Noise Ratio (SNR)

SNR measures how much louder the signal is compared to the noise, in decibels. Higher is better.

```
Theoretical SNR:  SNR ≈ 6.02 × n + 1.76   (dB)
```

| Application | Typical SNR |
|---|---|
| AM Radio | ~40 dB |
| FM Radio | ~60 dB |
| CD Audio | ~96 dB |
| Studio Recording | ~120+ dB |

Every additional bit adds approximately **6 dB of SNR**.

---

### 6. Oversampling

Instead of one sample per interval, take `M` samples and average them. Random quantization errors cancel out statistically while the true signal is preserved.

```
Normal (1×):    [sample] → quantize → output  (error stays)
4× Oversample:  [s1][s2][s3][s4] → quantize each → average → output
                 Random errors partially cancel out
```

```
Golden Rule: Every 4× oversampling = +1 effective bit = +6 dB SNR
Full formula: SNR = 6.02n + 1.76 + 10·log₁₀(osRate)  dB
```

---

### 7. Effective Number of Bits (ENOB)

ENOB is your actual resolution after combining hardware bit depth with oversampling gain:

```
ENOB = n + log₂(osRate) / 2
```

Example: 12-bit ADC + 16× oversampling → ENOB = 12 + 2 = **14 effective bits**

This is the principle behind sigma-delta ADCs used in every smartphone.

<br>

---

##  The Algorithm — How the Code Works

All simulation logic lives in `lab.html` (and the standalone `adc_simulator.html`). Here is the complete breakdown:

### Step 1 — Signal Acquisition

Three paths depending on the source selected in Step 2:

```javascript
// Microphone: MediaRecorder → WebM blob → decodeAudioData → Float32Array PCM
const audioBuffer = await audioCtx.decodeAudioData(arrayBuffer);
const raw = audioBuffer.getChannelData(0);  // mono channel

// Generator: mathematical formula evaluated at N points
sine:     v = sin(2π × freq × t)
square:   v = sign(sin(2π × freq × t)) × 0.9
sawtooth: v = 2 × frac(freq × t) - 1
chirp:    v = sin(2π × (freq + freq×t) × t)  // frequency sweep

// CSV: linear interpolation (lerp) between adjacent user samples
signal[i] = csvData[lo] + (csvData[hi] - csvData[lo]) × (idx - lo)
```

All three sources are normalized to `[-1, +1]` and resampled to exactly N=250 display points using linear interpolation.

---

### Step 2 — Noise Floor Injection

```javascript
noisy[i] = original[i] + (Math.random() - 0.5) × 2 × noiseAmplitude
```

Uniform random noise is added before quantization to simulate real-world interference (thermal noise, EMI, power supply ripple). `noiseAmplitude` scales from 0 to 0.3.

---

### Step 3 — Midtread Uniform Quantization

```
step = 2 / 2ⁿ              ← voltage width of one level
Q[i] = round(x[i] / step) × step
```

This is **midtread uniform quantization** — the algorithm inside every real ADC chip. Each sample is snapped to the nearest multiple of `step`. The rounding error is uniformly distributed in `[-step/2, +step/2]`, which produces the theoretical SNR = `6.02n + 1.76 dB` exactly.

The `Math.max(-1, Math.min(1, v))` clamp prevents clipping artifacts when noise pushes a sample outside the ADC's input range.

---

### Step 4 — Oversampling + Decimation

```javascript
// 1. Generate N × osRate super-samples
// 2. Add independent noise to each
// 3. Quantize each with the same midtread rule
// 4. Average every group of osRate → N output points

for (let i = 0; i < N; i++) {
  let sum = 0;
  for (let j = 0; j < osRate; j++) {
    sum += quantized_super_samples[i * osRate + j];
  }
  output[i] = sum / osRate;   // ← averaging step
}
```

The noise cancellation comes from **statistical independence** of rounding errors. Each super-sample rounds independently, so averaging M of them reduces noise variance by factor M → noise amplitude by √M. Since 4× → √4 = 2 → amplitude halved → +6 dB → +1 bit.

---

### Step 5 — Metrics Calculation

```javascript
errors = original.map((v, i) => quantized[i] - v)
RMS    = sqrt(mean(errors²))
SNR    = 6.02 × bits + 1.76 + 10 × log₁₀(osRate)   // dB
ENOB   = bits + osRateExp / 2
```

---

### Step 6 — Chart Rendering

Three Chart.js instances, all updated via `chart.update('none')` (no animation) for instant slider response:

- **Waveform chart** — 3 datasets: original (blue line), quantized (orange stepped line), fill anchor (invisible copy of quantized that fills between itself and dataset[0] with orange shading). A custom `levelLinesPlugin` draws dashed horizontal lines at each quantization boundary when bits ≤ 7.
- **Error chart** — Single line + fill showing the raw difference signal
- **SNR chart** — Green theoretical curve + orange scatter dot at current operating point

---

### Step 7 — Data Persistence

```javascript
// Auto-save all form fields + readings array to localStorage
localStorage.setItem('adc-lab', JSON.stringify(data));

// Reload on page open
const d = JSON.parse(localStorage.getItem('adc-lab'));
```

`readings` is a JavaScript array of objects. Each call to "Record This Reading" pushes a new object and re-renders the HTML table. The table supports inline note editing, row deletion, and CSV export.

<br>

---

##  Features

### Landing Page (`index.html`)
- Theory cards for all 4 core concepts with formulas
- Visual 5-step experiment workflow diagram
- Objectives and equipment list
- Links to the lab environment

### Lab Environment (`lab.html`)
- ** Microphone Recording** — record real audio, decoded to PCM samples with live visualiser
- ** Signal Generator** — sine, square, sawtooth, chirp with frequency + amplitude control
- ** CSV Upload** — drag-and-drop, auto-normalised, works with sensor data
- ** Bit Depth Slider** — 2-bit to 16-bit with live bit meter
- ** Oversampling Slider** — 1× to 64× in powers of 2
- ** Noise Floor** — 0–30% pre-ADC noise injection
- ** 3 Live Charts** — waveform + fill, error signal, SNR curve
- ** Level Lines** — dashed grid at each quantization boundary (≤7 bit)
- ** Hover Tooltips** — JS-positioned bubbles for every technical term
- ** Quality Meter** — Poor → FM → CD → Studio, colour-coded live
- ** Record Readings** — log every setting to a data table with inline notes
- ** Auto-Save** — all data persists in localStorage between sessions
- ** Lab Notebook** — 6-section notebook (aim, apparatus, theory, observations, analysis, conclusion)
- ** Report Builder** — auto-assembles final report from all steps
- ** Print** — print-optimised CSS hides navigation for clean output
- ** Export CSV** — readings table and full report both exportable

<br>

---

## 🚀 How to Use

### Using the Hosted Site
Visit **[https://vertiam.github.io/adc-simulator/](https://vertiam.github.io/adc-simulator/)** — no setup needed.

### Running Locally
The landing page and simulator work by simply opening the files. However, **microphone recording requires HTTPS** — it will not work from `file://`. For local mic testing, use a local HTTPS server:

```bash
# Python (simplest)
python -m http.server 8000
# then open http://localhost:8000

# Node.js (if installed)
npx serve .
```

### Lab Experiment — Quick Start

```
1. Open /lab.html
2. Step 1: Enter your name and reg number
3. Step 2: Choose signal source
         → Mic: click the red button, speak, stop
         → Generator: pick waveform, adjust frequency
         → CSV: drag your data file onto the drop zone
4. Step 3: Move the Bit Depth slider to 4-bit
         → Observe the staircase in the waveform
         → Click "Record This Reading"
         → Move to 8-bit → Record again
         → Move to 12-bit → Record again
         → Now drag Oversampling to 4×, 16×, 64×
         → Record each setting to build your data table
5. Step 4: Write your observations and conclusion
6. Step 5: Print or export your report
```

### CSV Data Format

```
# Single column (values only)
0.123
-0.456
0.789

# Two columns (time, value) — comma, tab, or semicolon delimited
0.000, 0.123
0.001, -0.456
0.002, 0.789
```

Values are automatically normalized to `[-1, +1]`. Any real sensor data works — ECG readings, temperature logs, accelerometer outputs, etc.

<br>

---

## 🌍 Real-World Applications

| Domain | How ADC Quality Matters |
|---|---|
|  **Music & Audio** | CD uses 16-bit 44.1kHz. Studio uses 24-bit. Noise = audible hiss |
|  **Medical Devices** | ECG, pulse oximeters, MRI scanners — a noisy sample = wrong diagnosis |
|  **Smartphones** | Every mic, touch screen, and camera sensor has an ADC inside |
|  **Communication** | AM/FM radio, 5G — quantization noise limits transmission quality |
|  **IoT Sensors** | Temperature, pressure, humidity sensors all use ADCs |
|  **Scientific Instruments** | Oscilloscopes, spectrum analysers — precision depends on ADC resolution |
|  **Gaming** | Controller analog sticks, audio — 8-bit feels 'lo-fi', 16-bit is clean |

<br>

---

##  Project File Structure

```
adc-simulator/
│
├── index.html              ← Landing page
│   ├── <nav>               Sticky navigation bar
│   ├── .hero               Title, subtitle, stats row
│   ├── #concepts           4 theory cards with formulas
│   ├── .flow-steps         5-step experiment workflow diagram
│   ├── objectives grid     What you'll do + what you need
│   ├── .cta-section        "Start the Lab" call to action
│   └── <footer>            Team info
│
├── lab.html                ← Full lab environment
│   ├── <nav>               Navigation (links back to index)
│   ├── .step-bar           Clickable 5-step progress indicator
│   ├── #step1              Student info form (auto-saves to localStorage)
│   ├── #step2              Signal source
│   │   ├── Microphone      getUserMedia → MediaRecorder → decodeAudioData
│   │   ├── Generator       Sine / Square / Sawtooth / Chirp + canvas preview
│   │   └── CSV Upload      Drag-drop, parse, normalize, lerp resample
│   ├── #step3              Experiment environment
│   │   ├── Left column     Stats, quality bar, ADC sliders, Record button
│   │   └── Right column    Waveform chart, Error chart, SNR chart
│   ├── #readings-table     Logged data with inline notes + CSV export
│   ├── #step4              Lab notebook (6 textarea sections)
│   ├── #step5              Auto-assembled report + print + export
│   ├── .lab-footer         Prev/Next navigation + auto-save indicator
│   └── <script>
│       ├── Tooltip engine  getBoundingClientRect → position:fixed
│       ├── Step nav        goStep(), nextStep(), prevStep()
│       ├── Auto-save       localStorage read/write, setInterval(10s)
│       ├── Signal source   setSignalMode(), startRecording(), updateGen()
│       ├── buildSimData()  Quantization + oversampling algorithm
│       ├── simUpdate()     Reads sliders → buildSimData → updates charts
│       ├── initCharts()    Chart.js setup (wave, error, SNR)
│       ├── levelPlugin     Custom Chart.js plugin for level-line grid
│       ├── recordReading() Push to readings[], re-render table, save
│       ├── exportReadingsCSV() / exportFullReport()
│       └── buildReport()   Assembles Step 5 from all previous data
│
├── style.css               ← Shared design system
│   ├── CSS variables        Colors, fonts, radii, shadows
│   ├── body / nav           Layout, sticky nav, logo
│   ├── Typography           h1–h4, body text, code
│   ├── Buttons              Primary, outline, ghost, danger + sizes
│   ├── Cards                card, card-header, card-body
│   ├── Status dots          Color-coded animated indicators
│   ├── Form elements        Input, select, textarea, range slider
│   ├── Tabs                 .tabs / .tab / .tab-content
│   ├── Data table           .data-table with hover states
│   ├── Badges               Color variants for SNR quality
│   ├── Step bar             .step-item, .step-num, connectors
│   ├── Upload zone          Drag-and-drop with hover states
│   ├── Record button        Idle / recording / done states + pulse
│   └── Print styles         @media print hides nav + controls
│
└── README.md               ← This file
```

<br>

---

##  Key Formulas Reference

```
Quantization Levels    =  2ⁿ
Quantization Step Size =  Full Scale Range / 2ⁿ
Quantization Error     ∈  [-step/2, +step/2]
RMS Quantization Noise =  step / √12

Theoretical SNR        =  6.02n + 1.76                      (dB, no oversampling)
SNR with Oversampling  =  6.02n + 1.76 + 10·log₁₀(osRate)  (dB)
Oversampling SNR Gain  =  10·log₁₀(osRate)                  (dB)

ENOB                   =  n + log₂(osRate) / 2
Golden Rule            :  4× oversampling  ≡  +1 bit  ≡  +6 dB SNR

Nyquist Theorem        :  sample_rate ≥ 2 × f_signal  (minimum to reconstruct)
```

<br>

---

## 👥 Team

**Team Name: Qt π's**  
**Quantumn Hackathon Track 4 PS_#19** — ADC Resolution, Noise & Oversampling Simulator  
**Department:** Mechanical Engineering

| Role | Name | Registration No. |
|---|---|---|
|  **Team Leader** | Swayam Viral Marfatia | RA2511002010080 |
|  **Member** | Narayan Murthy | RA2511002010124 |
|  **Member** | Shirly Oviya | RA2511054010030 |
| **Member** | Mithasha P Sishaj | RA2511053050040 | 
Built to make signal processing concepts accessible through an interactive, academically rigorous lab experience.

---

<br>

> *"The goal is to turn invisible noise into something you can see, drag a slider, and understand."*  
> — **Qt π's**, Quantumn Hackathon Track 4 PS_19

---
