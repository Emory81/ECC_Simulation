#fm_radio.py
#Last Updated: 12/01/2025
#By: Auto-generated

# Simulates FM radio broadcast (analog), modeled here as a noisy digital channel.

import sprompt
import mediums.helper as helper
import random

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # FM analog link translated to bit-errors for the simulation
    noise_prob = [0, 1e-3, 5e-3, 1e-2]

    base_error = noise_prob[noise_level]

    # Range & fading
    range_factor = min(length / 20000.0, 1.0)
    bit_error_rate = base_error * (1 + range_factor) * error_multiplier

    # Occasional multipath fades
    def fm_noise(data, ber):
        if random.random() < 0.015:
            return helper.apply_noise_default(data, min(ber * 30, 0.4), burst_chance=0.12, burst_min=8, burst_max=60)
        return helper.apply_noise_default(data, ber)

    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=fm_noise
    )
