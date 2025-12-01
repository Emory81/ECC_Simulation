#main.py
#Last Updated: 11/20/2025
#By: Emory H.

#Helper functions for the main.py file.

import random
import sprompt
import ecc_methods as ecc
import mediums

def data_creator():
    data_string = ""
    for i in range(int(sprompt.message_length)):
        data = random.choice(['0', '1'])
        data_string += data

    return data_string

def method_encoder(data_string):
    global last_encoded_data

    # Handle ECC method selection. If a method is not implemented, fall back to no ECC (pass-through).
    choice = sprompt.ecc_method

    if choice == '4':
        # Redundancy ECC (implemented)
        ecc.redundancy.encode(data_string)
        encoded_data = ecc.redundancy.encoded_data
    elif choice == '6':
        # No ECC
        encoded_data = data_string
    else:
        # Other ECC methods not implemented yet; use no ECC but inform the user.
        print(f"ECC method {choice} is not implemented. Proceeding with no ECC.")
        encoded_data = data_string

    last_encoded_data = encoded_data
    return encoded_data

def method_decoder(transmitted_data):
    # Use stored encoded data for decoding metrics when possible.
    choice = sprompt.ecc_method

    if choice == '4':
        metrics = ecc.redundancy.decode(transmitted_data)
        return metrics

    # For no ECC or unimplemented methods, compute basic metrics using the last encoded data.
    try:
        encoded_data = last_encoded_data
    except NameError:
        print("Error: No encoded data available for decoding. Did you run method_encoder?")
        return None

    # Simple decode function for no ECC: take the first test result as the decoded message
    def _no_ecc_decode(encoded_data_local, test_results):
        if len(test_results) == 0:
            return ''
        return test_results[0][:len(encoded_data_local)]

    # Compute metrics using ECC helper
    metrics = ecc.helper.compute_metrics(
        encoded_data=encoded_data,
        transmitted_data=transmitted_data,
        decode_func=_no_ecc_decode
    )

    return metrics

def medium_runner(encoded_data):
    choice = sprompt.ecc_medium

    if choice == '1':
        transmitted_data = mediums.copper.medium(encoded_data)
    elif choice == '2':
        transmitted_data = mediums.fiber_optic.medium(encoded_data)
    elif choice == '3':
        transmitted_data = mediums.coaxial.medium(encoded_data)
    elif choice == '4':
        transmitted_data = mediums.cat6.medium(encoded_data)
    elif choice == '5':
        transmitted_data = mediums.satellite_radio.medium(encoded_data)
    elif choice == '6':
        transmitted_data = mediums.mobile_5g.medium(encoded_data)
    elif choice == '7':
        transmitted_data = mediums.fm_radio.medium(encoded_data)
    elif choice == '8':
        transmitted_data = mediums.wifi7.medium(encoded_data)
    else:
        print(f"Unknown medium choice '{choice}'. Defaulting to copper.")
        transmitted_data = mediums.copper.medium(encoded_data)

    return transmitted_data