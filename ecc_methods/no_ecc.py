#no_ecc.py
#Last Updated: 12/03/2025
#By: Auto-generated

import ecc_methods.helper as helper

def encode(data):
    global encoded_data
    encoded_data = data
    return encoded_data

def decode(transmitted_data):
    # For no ECC, simply return metrics using first test as decoded
    return helper.compute_metrics(
        encoded_data=encoded_data,
        transmitted_data=transmitted_data,
        decode_func=_decode_no_ecc
    )

def _decode_no_ecc(encoded_data_local, test_results):
    if not test_results:
        return ''
    return test_results[0][:len(encoded_data_local)]
