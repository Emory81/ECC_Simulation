#copper.py
#Last Updated: 11/15/2025
#By: Emory H.

#this code simulates the transmission of data across copper wires.

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

    # Track results for multiple test cycles
    results = []

    for _ in range(test_amount):
        data = encoded_data
        for _ in range(hops + 1):
            data = apply_noise(data, bit_error_rate)
        results.append(data)

    # Return all results as a comma separated string
    return ','.join(results)

def apply_noise(binary_data, bit_error_rate):
    # Applies bit flips based on error rate.
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
    # helper for flipping a bit
    return '1' if bit == '0' else '0'