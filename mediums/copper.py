#copper.py
#Last Updated: 11/20/2025
#By: Emory H.

#this code simulates the transmission of data across copper wires.

import sprompt
import mediums.helper as helper

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # Copper-specific noise profile
    noise_prob = [0, 1e-4, 5e-4, 2e-3]  # none, low, medium, high

    base_error = noise_prob[noise_level]

    # Increase error rate based on wire length
    length_factor = min(length / 1000, 1.0)
    bit_error_rate = base_error * (1 + length_factor) * error_multiplier

    # Call the helper module's simulate_medium function
    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=helper.apply_noise_default
    )