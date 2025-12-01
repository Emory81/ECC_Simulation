#mobile_5g.py
#Last Updated: 12/01/2025
#By: Auto-generated

# Simulates transmission over 5th Generation cellular network (5G).

import sprompt
import mediums.helper as helper
import random

def medium(encoded_data):
    length = int(sprompt.medium_length)
    noise_level = int(sprompt.noise_level)
    error_multiplier = float(sprompt.error_rate)
    hops = int(sprompt.hops)
    test_amount = int(sprompt.test_amount)

    # 5G is generally reliable but subject to interference and mobility
    noise_prob = [0, 5e-5, 2e-4, 1e-3]

    base_error = noise_prob[noise_level]

    # Mobility factor (higher for larger "length" representing distance/movement)
    mobility_factor = min(length / 2000.0, 2.0)
    bit_error_rate = base_error * (1 + 0.5 * mobility_factor) * error_multiplier

    # Introduce short interference bursts for wireless
    def cellular_noise(data, ber):
        interference_chance = 0.02
        if random.random() < interference_chance:
            return helper.apply_noise_default(data, min(ber * 20, 0.25), burst_chance=0.08, burst_min=5, burst_max=30)
        return helper.apply_noise_default(data, ber)

    return helper.simulate_medium(
        encoded_data=encoded_data,
        test_amount=test_amount,
        hops=hops,
        bit_error_rate=bit_error_rate,
        noise_function=cellular_noise
    )
