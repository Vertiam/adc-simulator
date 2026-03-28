# ⚡ ADC Resolution, Noise & Oversampling — Signal Processing Lab
### Quatumn Hackathon · Track #4 · Problem Statement #19

> **A complete, browser-based digital laboratory** for studying Analog-to-Digital Conversion, quantization noise, and oversampling.  
> Record real signals, run controlled experiments, visualise the physics, and export a full lab report — no installation required.

---

## 🌐 Live Website

🔗 **[https://vertiam.github.io/adc-simulator/](https://vertiam.github.io/adc-simulator/)**

---

## 📽️ Video Demo

🔗 **[Click This Link to Watch the video demo!!](https://www.youtube.com/watch?v=S8LdKh43M4Y)**

---

| Page | URL | Description |
|---|---|---|
| 🏠 Landing Page | `/index.html` | Project overview, theory cards, experiment guide |
| 🔬 Lab Environment | `/lab.html` | Full 5-step guided experiment |

---

## 📋 Table of Contents

- [Evaluation Criteria Alignment](#-evaluation-criteria-alignment)
- [What This Project Does](#-what-this-project-does)
- [Problem Statement](#-problem-statement)
- [Technologies Used](#-technologies-used)
- [Lab Workflow — All 5 Steps](#-lab-workflow--all-5-steps)
- [Core Concepts](#-core-concepts)
- [The Algorithm](#-the-algorithm)
- [Visualization Features](#-visualization-features)
- [Chart Interaction Tools](#-chart-interaction-tools)
- [How to Use](#-how-to-use)
- [Real-World Applications](#-real-world-applications)
- [Project File Structure](#-project-file-structure)
- [Key Formulas Reference](#-key-formulas-reference)
- [Team](#-team)

---

## 🎯 Evaluation Criteria Alignment

| Criterion | How This Project Meets It |
|---|---|
| **Physical / System Correctness** | Midtread uniform quantization matches the IEEE standard ADC model. SNR formula `6.02n + 1.76 dB` is the exact closed-form theoretical result. Oversampling gain `10·log₁₀(M)` is derived from noise power spectral density. FFT uses Cooley-Tukey radix-2 DIT with Hanning windowing — standard DSP practice. All formulas are textbook-accurate. |
| **Visualization Quality** | 4 live interactive charts: waveform, error signal, SNR curve, FFT spectrum. Staircase fill shows error area even at high bit depths. Quantization level grid lines visible at ≤7 bits. Zoom, pan, markers, comparison snapshots, and text annotations on every chart. Dark/light mode. PNG export. |
| **Conceptual Clarity** | Every technical term has a plain-English hover tooltip. Step-by-step guided lab workflow. Pre-filled theory notebook with derivations. Real-world application examples. Designed so a student with zero prior knowledge can complete the full experiment and understand ADC principles end-to-end. |

---

## 🎯 What This Project Does

This project models every stage of the ADC pipeline:

```
Real Signal → Sampling → Quantization → Error Measurement → Oversampling → SNR & FFT Analysis
```

Students interact with this pipeline through a guided 5-step lab session, recording readings, writing observations, and generating a complete exportable report.

**Core deliverables from the problem statement:**

| Required Outcome | Implementation |
|---|---|
| Model ADCs with different bit resolutions | 2-bit to 16-bit slider, live waveform update |
| Visualize quantization noise | Error chart + orange fill + FFT spectrum |
| Demonstrate noise reduction via oversampling | 1× to 64× slider, live SNR update |
| Quantized signal plots | Waveform chart with stepped quantized line |
| SNR vs ADC resolution graphs | SNR curve chart with operating point dot |

---

## 🔍 Problem Statement

**Problem Statement #19:**
> *Analog-to-digital conversion introduces quantization noise. Simulate ADC digitization effects and study how oversampling improves signal quality.*

- ✅ Model ADCs with different bit resolutions (2–16 bit)
- ✅ Visualize quantization noise (error chart + FFT)
- ✅ Demonstrate noise reduction using oversampling (1× to 64×)
- ✅ Quantization, ADC resolution, oversampling, noise averaging — all implemented and visualized

---

## 🛠 Technologies Used

| Technology | Role | Why Chosen |
|---|---|---|
| **HTML5** | Page structure | No framework overhead, works offline |
| **CSS3 + Variables** | Shared design system | Single `style.css`; dark/light via class toggle |
| **JavaScript ES6+** | All simulation logic | In-browser, zero-latency slider response |
| **Web Audio API** | Microphone recording | Native PCM capture, no libraries |
| **MediaRecorder API** | Audio stream capture | Standard across all modern browsers |
| **Chart.js v4.4.1** | 4 live interactive charts | Fastest JS charting library for real-time data |
| **chartjs-plugin-zoom** | Zoom & pan | Built on Hammer.js touch gestures |
| **Custom FFT (JS)** | Frequency spectrum | Cooley-Tukey radix-2 DIT, O(N log N) |
| **localStorage** | Auto-save student data | No backend required |
| **GitHub Pages** | Free HTTPS hosting | `getUserMedia` requires HTTPS |

---

## 🔬 Lab Workflow — All 5 Steps

### Step 1 — Student Setup
Required fields (name, reg number, dept, date) with shake-animation validation and live green/red border feedback. Auto-saves to `localStorage` every 10 seconds. All fields populate the final report.

### Step 2 — Signal Source

**🎤 Microphone** — `getUserMedia()` → `MediaRecorder` → WebM blob → `decodeAudioData()` → Float32Array PCM → normalized to `[-1, +1]`. Live waveform via `AnalyserNode`.

**⚡ Generator** — Sine, Square, Sawtooth, Chirp. Configurable frequency and amplitude.

**📂 CSV Upload** — Drag-and-drop, single-column or time,value format, linear interpolation resample to 250 points.

### Step 3 — Run Experiments

Four live charts, all interactive:

1. **Waveform** — Original vs Quantized with staircase fill and level grid lines
2. **Quantization Error** — The noise signal; RMS error shown live
3. **SNR vs Bit Depth** — Theoretical curve + orange dot at current settings
4. **FFT Spectrum** — Cooley-Tukey FFT of the error signal; shows noise spectral distribution

Controls: Bit Depth (2–16 bit) · Oversampling (1×–64×) · Noise Floor (0–30%).

**Record This Reading** logs current settings (bits, OS rate, SNR, ENOB, RMS) to a data table.

### Step 4 — Lab Notebook
Aim, Apparatus, Theory, Observations, Analysis, Conclusion — all editable, auto-saved.

### Step 5 — Report
Auto-assembled from all previous steps. Print with `@media print` CSS, or export full CSV.

---

## 📚 Core Concepts

### 1. Analog vs Digital
Real-world signals are continuous. Computers store only discrete numbers. The ADC bridges this gap.

### 2. Bit Depth & Quantization Levels
```
Levels = 2ⁿ          Step = 2 / 2ⁿ    (in [-1, +1] range)
```

| Bits | Levels | Typical Use |
|---|---|---|
| 4 | 16 | Illustration |
| 8 | 256 | Telephony |
| 12 | 4,096 | Sensors, IoT |
| 16 | 65,536 | CD audio |
| 24 | 16,777,216 | Studio recording |

### 3. Quantization Noise
```
Q[i]    = round(x[i] / step) × step
error   = Q[i] - x[i]   ∈ [-step/2, +step/2]
RMS     = step / √12
```

### 4. Signal-to-Noise Ratio
```
SNR = 6.02n + 1.76 + 10·log₁₀(osRate)   dB
```
Every bit adds ~6 dB. Every 4× oversampling adds another ~6 dB.

### 5. Oversampling
Sample M times faster, average groups of M. Noise variance drops by M, amplitude by √M.
```
Golden Rule:  4× oversampling = +1 bit = +6 dB SNR
ENOB = n + log₂(M) / 2
```

### 6. FFT Spectral Analysis
Quantization noise is ideally white (flat spectrum). The FFT chart shows this. Oversampling lowers the noise floor uniformly across all frequency bins.

---

## 🧮 The Algorithm

### Midtread Uniform Quantization
```javascript
step  = 2 / Math.pow(2, bits)          // one level's width
Q[i]  = Math.round(x[i] / step) * step // snap to nearest level
```
This is the IEEE-standard ADC model. Rounding error is uniformly distributed in `[-step/2, +step/2]`.

### Oversampling + Decimation
```javascript
// Generate N × osRate super-samples → quantize each → average groups
for (let i = 0; i < N; i++) {
  let sum = 0;
  for (let j = 0; j < osRate; j++) sum += Q_super[i * osRate + j];
  output[i] = sum / osRate;
}
```
Statistical independence of rounding errors means averaging M values reduces noise variance by M.

### Cooley-Tukey FFT
```
Algorithm:   Radix-2 DIT with bit-reversal permutation
Complexity:  O(N log N) vs O(N²) naive DFT
Window:      Hanning  w[i] = 0.5 × (1 - cos(2πi/N))
Input:       Quantization error signal
Output:      Power spectrum, first N/2 bins
```

---

## 📊 Visualization Features

| Chart | What It Shows | Evaluation Criterion Met |
|---|---|---|
| **Waveform** | Smooth blue original vs stepped orange quantized + fill + level grid | Physical correctness + Visualization quality |
| **Error Signal** | Raw quantization noise at each sample point | Visualization quality + Conceptual clarity |
| **SNR Curve** | Theoretical `6.02n + 1.76 dB` plotted against current operating point | Physical correctness |
| **FFT Spectrum** | Noise power distribution across frequency bins (Hanning-windowed) | Physical correctness + Visualization quality |

---

## 🔧 Chart Interaction Tools

| Button | Function |
|---|---|
| `+` / `−` | Zoom in/out (also mouse wheel, pinch) |
| `⊙` | Reset zoom |
| `📍` | Place marker — wave markers sync automatically to error chart |
| `✏️` | Add text annotation — click chart, type label |
| `⊞` | Snapshot comparison — freeze current state as purple overlay |
| `↓` | Download PNG (respects dark/light mode) |
| Theme toggle | Dark ↔ Light mode, saved to localStorage |

---

## 🚀 How to Use

```bash
# Hosted: just visit the URL
https://vertiam.github.io/adc-simulator/

# Local (mic needs HTTPS or localhost):
python -m http.server 8000
# open http://localhost:8000
```

**Suggested experiment sequence:**
```
1. Set Bit Depth = 4-bit → Record
2. Set Bit Depth = 8-bit → Record
3. Set Bit Depth = 12-bit → Record  (observe SNR jump)
4. Set Oversampling = 4× → Record   (observe noise floor in FFT)
5. Set Oversampling = 16× → Record
6. Use ⊞ to snapshot 4-bit, switch to 12-bit → direct visual comparison
7. Place marker at a peak → observe it synced to error chart
8. Export lab report
```

---

## 🌍 Real-World Applications

| Domain | ADC Impact |
|---|---|
| 🎵 **Music** | CD = 16-bit 44.1 kHz · Studio = 24-bit 96 kHz |
| 🏥 **Medical** | ECG, MRI, pulse oximeters — noisy ADC = wrong diagnosis |
| 📱 **Smartphones** | Every mic, camera sensor, and touchscreen uses an ADC |
| 🛰 **Telecom** | 5G radio front-ends — ADC limits channel capacity |
| 🌡 **IoT** | Temperature, pressure sensors — bit depth = precision |
| 🔬 **Science** | Oscilloscopes — limited by ADC resolution |

---

## 📁 Project File Structure

```
adc-simulator/
├── index.html              ← Landing page
├── lab.html                ← Full lab (2083 lines)
│   ├── 4 chart system      waveform, error, SNR, FFT
│   ├── Marker system       wave→error sync
│   ├── Comparison mode     snapshot overlay
│   ├── Text annotations    click-to-place labels
│   ├── FFT engine          Cooley-Tukey + Hanning
│   └── Theme toggle        dark/light + localStorage
├── style.css               ← Shared design system
├── csv_data_generator.py   ← Python test data generator
└── README.md               ← This file
```

---

## 🔑 Key Formulas

```
Levels     = 2ⁿ
Step       = 2 / 2ⁿ
RMS noise  = step / √12
SNR (ideal)= 6.02n + 1.76  dB
SNR (OS)   = 6.02n + 1.76 + 10·log₁₀(M)  dB
ENOB       = n + log₂(M) / 2
Nyquist    : f_s ≥ 2 × f_max
FFT        : O(N log N),  Hanning window
```

---

## 👥 Team

**Team Name: Qt π's** · Quatumn Hackathon · Problem Statement #19 · Mechanical Engineering

| Role | Name | Reg. No. |
|---|---|---|
|  **Team Leader** | Swayam Viral Marfatia | RA2511002010080 |
|  **Member** | Narayan Murthy | RA2511002010124 |
|  **Member** | Shirly Oviya | RA2511054010030 |
|  **Member** | Mithasha P Sishaj | RA2511053050040 |

> *"The goal is to turn invisible noise into something you can see, drag a slider, and understand."* — Qt π's
