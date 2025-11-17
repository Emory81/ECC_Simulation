#copper.py
#Last Updated: 11/15/2025
#By: Emory H.

#this code simulates the transmission of data across copper wires.

import time
import random
import sprompt

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # Noise level
    noise_prob = [0, 1e-4, 5e-4, 2e-3]  # none, low, medium, high
    base_error = noise_prob[noise_level]

    # Increase error rate based on wire length
    length_factor = min(length / 1000, 1.0)
    bit_error_rate = base_error * (1 + length_factor) * error_multiplier

    # Track results and time
    results = []
    start_time = time.time()
    last_update = start_time

    for i in range(test_amount):
        data = encoded_data
        for _ in range(hops + 1):
            data = apply_noise(data, bit_error_rate)
        results.append(data)

        # Progress update every 5 seconds
        now = time.time()
        if now - last_update >= 5 or i == test_amount - 1:
            elapsed = now - start_time
            percent_done = ((i + 1) / test_amount) * 100
            tests_done = i + 1

            if percent_done > 0:
                eta_seconds = (elapsed / percent_done) * (100 - percent_done)
            else:
                eta_seconds = 0

            eta_formatted = format_time(eta_seconds)
            print(f"{percent_done:.2f}% | {tests_done}/{test_amount} | ETA: {eta_formatted}")
            last_update = now

    # Return all results as a comma separated string
    return ','.join(results)

def apply_noise(binary_data, bit_error_rate):
    transmitted = []
    data_len = len(binary_data)

    i = 0
    while i < data_len:
        bit = binary_data[i]

        # Burst noise simulation
        if random.random() < 0.005:
            burst_len = random.randint(3, 12)
            for _ in range(min(burst_len, data_len - i)):
                transmitted.append(flip_bit(binary_data[i]))
                i += 1
            continue

        # Random flip at base error rate
        if random.random() < bit_error_rate:
            bit = flip_bit(bit)

        transmitted.append(bit)
        i += 1

    return ''.join(transmitted)

def flip_bit(bit):
    return '1' if bit == '0' else '0'

def format_time(seconds):
    """Format seconds into hh:mm:ss"""
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"