import math
import random
import csv

def get_float_input(prompt, default_value):
    """Helper to get a number from the user or use a default."""
    user_input = input(f"{prompt} [Default: {default_value}]: ").strip()
    if not user_input:
        return default_value
    try:
        return float(user_input)
    except ValueError:
        print(f"  -> Invalid number. Using default: {default_value}")
        return default_value

print("--- ADC Oversampling Data Generator ---")
print("Press Enter on any prompt to use the default value.\n")

# 1. Get User Inputs
f_signal = get_float_input("Ideal Signal Frequency (Hz)", 1.0)
fs = get_float_input("Sampling Rate (Hz)", 1000.0)
duration = get_float_input("Simulation Duration (seconds)", 1.0)
noise_std = get_float_input("Noise Level (Amplitude)", 0.5)

filename = input("Output filename [Default: custom_adc_data.csv]: ").strip()
if not filename:
    filename = "custom_adc_data.csv"
if not filename.endswith('.csv'):
    filename += '.csv'

# 2. Setup Variables
num_samples = int(duration * fs)
time_step = 1.0 / fs

data_rows = []
buffer_64 = [] # Buffer to hold recent samples for averaging

print(f"\nGenerating {num_samples} rows of data...")

# 3. Generate the Data
for i in range(num_samples):
    t = i * time_step
    
    # Calculate ideal sine wave (Amplitude 5, Offset 5)
    ideal_val = 5 * math.sin(2 * math.pi * f_signal * t) + 5
    
    # Inject Gaussian-like noise (using Box-Muller transform for standard python)
    u1 = random.random()
    u2 = random.random()
    # Avoid log(0)
    if u1 == 0: u1 = 1e-10 
    z0 = math.sqrt(-2.0 * math.log(u1)) * math.cos(2.0 * math.pi * u2)
    noise_val = z0 * noise_std
    
    noisy_sample = ideal_val + noise_val
    
    # Add to buffer for oversampling calculations
    buffer_64.append(noisy_sample)
    if len(buffer_64) > 64:
        buffer_64.pop(0)
        
    # Calculate Oversampled values (Rolling Averages)
    osr4 = sum(buffer_64[-4:]) / len(buffer_64[-4:])
    osr16 = sum(buffer_64[-16:]) / len(buffer_64[-16:])
    osr64 = sum(buffer_64) / len(buffer_64)
    
    # Store the row (rounding to 4 decimal places for clean CSV)
    data_rows.append([
        round(t, 4), 
        round(ideal_val, 4), 
        round(noisy_sample, 4), 
        round(osr4, 4), 
        round(osr16, 4), 
        round(osr64, 4)
    ])

# 4. Write to CSV
try:
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write headers
        writer.writerow(["Time_s", "Ideal_Signal", "Noisy_ADC_Sample", "Oversampled_OSR4", "Oversampled_OSR16", "Oversampled_OSR64"])
        # Write data
        writer.writerows(data_rows)
    print(f"\nSuccess! File saved as '{filename}'.")
except Exception as e:
    print(f"\nError saving file: {e}")
