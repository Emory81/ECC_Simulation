#main.py
#Last Updated: 11/15/2025
#By: Emory H.

#This program will simulate how Error Correction Codes (ECC) work in data transmission.

import random
import time
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
    if sprompt.ecc_method == '4':
        ecc.redundancy.encode(data_string)
        encoded_data = ecc.redundancy.encoded_data
    
    return encoded_data

def method_decoder(transmitted_data):
    if sprompt.ecc_method == '4':
        metrics = ecc.redundancy.decode(transmitted_data)

    return metrics

def medium_runner(encoded_data):
    if sprompt.ecc_medium == '1':
        transmitted_data = mediums.copper.medium(encoded_data)

    return transmitted_data

def print_metrics(metrics):
    print("\nSimulation Results:")
    print("-------------------")
    print(f"Total Tests: {metrics['total_tests']}")
    print(f"Error-Free Tests: {metrics['error_free_tests']}")
    print(f"Tests with Errors: {metrics['tests_with_errors']}\n")

    print("Bit Error Counts per Test:")
    print(f"{metrics['bit_error_counts']}\n")

    print("Bit Error Rates per Test:")
    print(f"{[round(rate, 3) for rate in metrics['bit_error_rates']]}\n")

    print("Waiting 5 seconds before displaying final decoded message...\n")
    time.sleep(5)
    print("Final Decoded Message:")
    print(f"{metrics['decoded_message']}\n")

def main():
    sprompt.main()
    start_time = time.time()
    data_string = data_creator()
    encoded_data = method_encoder(data_string)
    transmitted_data = medium_runner(encoded_data)
    print("\nCompiling metrics...")
    metrics = method_decoder(transmitted_data)
    end_time = time.time()
    print_metrics(metrics)
    print(f"Time elapsed for simulation: {(end_time - start_time):.4f} seconds")

if __name__ == "__main__":
    main()