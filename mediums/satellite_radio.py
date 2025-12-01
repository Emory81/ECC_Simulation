#satellite_radio.py
#Last Updated: 12/01/2025
#By: Auto-generated

# Simulates transmission via satellite radio (large delays, higher error rates).

import sprompt
import mediums.helper as helper
import random

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # Satellite links are prone to weather and link budget issues
    noise_prob = [0, 1e-3, 5e-3, 2e-2]

    base_error = noise_prob[noise_level]

    # Slightly increase errors with link distance (proxy)
    length_factor = min(length / 40000.0, 1.0)
    bit_error_rate = base_error * (1 + length_factor) * error_multiplier

    # Occasional deep fades cause short high-error bursts
    def satellite_noise(data, ber):
        # Introduce occasional deep-fade bursts
        fade_chance = 0.01
        if random.random() < fade_chance:
            return helper.apply_noise_default(data, min(ber * 50, 0.5), burst_chance=0.1, burst_min=10, burst_max=100)
        return helper.apply_noise_default(data, ber)

    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=satellite_noise
    )
