#cat6.py
#Last Updated: 12/01/2025
#By: Auto-generated

# Simulates transmission over Cat6 Ethernet cable.

import sprompt
import mediums.helper as helper

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # Cat6 has better shielding and performance than generic copper
    noise_prob = [0, 5e-5, 2e-4, 5e-4]

    base_error = noise_prob[noise_level]

    length_factor = min(length / 1000.0, 1.0)
    bit_error_rate = base_error * (1 + length_factor) * error_multiplier

    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=helper.apply_noise_default
    )
