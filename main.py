#main.py
#Last Updated: 11/20/2025
#By: Emory H.

#This program will simulate how Error Correction Codes (ECC) work in data transmission.

import time
import sprompt
import helper

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
    data_string = helper.data_creator()
    encoded_data = helper.method_encoder(data_string)
    transmitted_data = helper.medium_runner(encoded_data)
    print("\nCompiling metrics...")
    metrics = helper.method_decoder(transmitted_data)
    end_time = time.time()
    print_metrics(metrics)
    print(f"Time elapsed for simulation: {(end_time - start_time):.4f} seconds")

if __name__ == "__main__":
    main()