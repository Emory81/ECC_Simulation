#fiber_optic.py
#Last Updated: 12/01/2025
#By: Auto-generated

# Simulates transmission over fiber optic cable.

import sprompt
import mediums.helper as helper

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # Fiber has extremely low random bit errors, occasional micro-bends and splice losses
    noise_prob = [0, 1e-7, 5e-7, 1e-6]

    base_error = noise_prob[noise_level]

    # Attenuation over very long distances (km scale), capped
    length_factor = min(length / 50000.0, 1.0)
    bit_error_rate = base_error * (1 + length_factor) * error_multiplier

    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=helper.apply_noise_default
    )
