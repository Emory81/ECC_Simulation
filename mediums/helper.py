#helper.py
#Last Updated: 11/20/2025
#By: Emory H.

#This module contains helper functions for the mediums.

import time
import random

def format_time(seconds):
    """Format seconds into hh:mm:ss"""
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"

def flip_bit(bit):
    return '1' if bit == '0' else '0'

def apply_noise_default(binary_data, bit_error_rate, burst_chance=0.005, burst_min=3, burst_max=12):
    transmitted = []
    data_len = len(binary_data)
    i = 0

    while i < data_len:
        bit = binary_data[i]

        # Burst noise
        if random.random() < burst_chance:
            burst_len = random.randint(burst_min, burst_max)
            for _ in range(min(burst_len, data_len - i)):
                transmitted.append(flip_bit(binary_data[i]))
                i += 1
            continue

        # Random flip
        if random.random() < bit_error_rate:
            bit = flip_bit(bit)

        transmitted.append(bit)
        i += 1

    return ''.join(transmitted)

def simulate_medium(encoded_data, test_amount, hops, bit_error_rate,
                    noise_function=apply_noise_default):
    results = []
    start_time = time.time()
    last_update = start_time

    for i in range(test_amount):
        data = encoded_data

        for _ in range(hops + 1):
            data = noise_function(data, bit_error_rate)

        results.append(data)

        # Progress update every 5 seconds
        now = time.time()
        if now - last_update >= 5 or i == test_amount - 1:
            elapsed = now - start_time
            percent_done = ((i + 1) / test_amount) * 100
            tests_done = i + 1

            eta_seconds = 0
            if percent_done > 0:
                eta_seconds = (elapsed / percent_done) * (100 - percent_done)

            print(f"{percent_done:.2f}% | {tests_done}/{test_amount} | ETA: {format_time(eta_seconds)}")
            last_update = now

    return ','.join(results)