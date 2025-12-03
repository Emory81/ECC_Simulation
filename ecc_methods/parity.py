#parity.py
#Last Updated: 12/03/2025
#By: Auto-generated

import ecc_methods.helper as helper

def encode(data):
    global encoded_data
    # Even parity for the whole message
    parity_bit = str(data.count('1') % 2)
    encoded_data = data + parity_bit
    return encoded_data

def decode(transmitted_data):
    return helper.compute_metrics(
        encoded_data=encoded_data,
        transmitted_data=transmitted_data,
        decode_func=decode_parity
    )

def decode_parity(encoded_data_local, test_results):
    # encoded_data_local = original_data + parity bit
    data_len = len(encoded_data_local) - 1
    decoded_message = ''

    # Majority vote across tests for each data bit
    for i in range(data_len):
        bits = [test[i] for test in test_results if len(test) > i]
        if not bits:
            decoded_message += '0'
            continue
        decoded_message += '1' if bits.count('1') > bits.count('0') else '0'

    return decoded_message
