#wifi7.py
#Last Updated: 12/01/2025
#By: Auto-generated

# Simulates transmission over Wifi 7 (next-gen WiFi) as a relatively reliable wireless medium.

import sprompt
import mediums.helper as helper
import random

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # Wifi7 expected to be low-error in good conditions
    noise_prob = [0, 2e-5, 1e-4, 5e-4]

    base_error = noise_prob[noise_level]

    # Obstacle/attenuation factor
    obstacle_factor = min(length / 1000.0, 2.0)
    bit_error_rate = base_error * (1 + 0.7 * obstacle_factor) * error_multiplier

    # Bursty interference from other devices
    def wifi_noise(data, ber):
        if random.random() < 0.03:
            return helper.apply_noise_default(data, min(ber * 15, 0.3), burst_chance=0.06, burst_min=4, burst_max=40)
        return helper.apply_noise_default(data, ber)

    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=wifi_noise
    )
