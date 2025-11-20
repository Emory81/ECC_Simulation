#redudancy.py
#Last Updated: 11/20/2025
#By: Emory H.

#This module implements the Redundancy ECC method.

import ecc_methods.helper as helper

def encode(data):
    global encoded_data, num_repeats

    num_repeats = input("(ECC Prompt) How many times would you like to repeat each message for redundancy? (1-100): ")
    try:
        num_repeats = int(num_repeats)
        if num_repeats < 1 or num_repeats > 100:
            raise ValueError
    except ValueError:
        print("Invalid input. Please enter an integer between 1 and 100.")
        return None
    # just makes data string repeated num_repeats times
    encoded_data = data * num_repeats
    #print(encoded_data)
    return encoded_data, num_repeats

def decode(transmitted_data):
    return helper.compute_metrics(
        encoded_data=encoded_data,
        transmitted_data=transmitted_data,
        decode_func=decode_redundancy
    )

def decode_redundancy(encoded_data, test_results):
    global num_repeats

    data_len = len(encoded_data) // num_repeats
    decoded_message = ""

    # Majority vote decoding
    for i in range(data_len):
        block = []
        for test in test_results:
            for j in range(i * num_repeats, (i + 1) * num_repeats):
                block.append(test[j])
        decoded_message += '1' if block.count('1') > block.count('0') else '0'

    return decoded_message