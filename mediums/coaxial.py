#coaxial.py
#Last Updated: 12/01/2025
#By: Auto-generated

# Simulates transmission over coaxial cable.

import sprompt
import mediums.helper as helper

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # Coaxial is generally worse than copper for long runs in terms of noise
    noise_prob = [0, 5e-4, 2e-3, 1e-2]

    base_error = noise_prob[noise_level]

    length_factor = min(length / 2000.0, 1.0)
    bit_error_rate = base_error * (1 + length_factor) * error_multiplier

    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=helper.apply_noise_default
    )
