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

    if choice == '1':
        ecc.parity.encode(data_string)
        encoded_data = ecc.parity.encoded_data
    elif choice == '2':
        ecc.hamming.encode(data_string)
        encoded_data = ecc.hamming.encoded_data
    elif choice == '3':
        ecc.reed_solomon.encode(data_string)
        encoded_data = ecc.reed_solomon.encoded_data
    elif choice == '4':
        ecc.redundancy.encode(data_string)
        encoded_data = ecc.redundancy.encoded_data
    elif choice == '5':
        ecc.checksum.encode(data_string)
        encoded_data = ecc.checksum.encoded_data
    elif choice == '6':
        ecc.no_ecc.encode(data_string)
        encoded_data = ecc.no_ecc.encoded_data
    else:
        print(f"ECC method {choice} does not exist. Proceeding with no ECC.")
        ecc.no_ecc.encode(data_string)
        encoded_data = ecc.no_ecc.encoded_data

    last_encoded_data = encoded_data
    return encoded_data

def method_decoder(transmitted_data):
    # Use stored encoded data for decoding metrics when possible.
    choice = sprompt.ecc_method

    # Dispatch to selected ECC decoder
    if choice == '1':
        return ecc.parity.decode(transmitted_data)
    elif choice == '2':
        return ecc.hamming.decode(transmitted_data)
    elif choice == '3':
        return ecc.reed_solomon.decode(transmitted_data)
    elif choice == '4':
        return ecc.redundancy.decode(transmitted_data)
    elif choice == '5':
        return ecc.checksum.decode(transmitted_data)
    elif choice == '6':
        return ecc.no_ecc.decode(transmitted_data)

    # Fallback: use last encoded data and no-ECC decode
    try:
        encoded_data = last_encoded_data
    except NameError:
        print("Error: No encoded data available for decoding. Did you run method_encoder?")
        return None

    def _no_ecc_decode(encoded_data_local, test_results):
        if len(test_results) == 0:
            return ''
        return test_results[0][:len(encoded_data_local)]

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