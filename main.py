#main.py
#Last Updated: 11/20/2025
#By: Emory H.

#This program will simulate how Error Correction Codes (ECC) work in data transmission.

import time
import sprompt
import helper

def main():
    sprompt.main()
    start_time = time.time()
    data_string = helper.data_creator()
    encoded_data = helper.method_encoder(data_string)
    transmitted_data = helper.medium_runner(encoded_data)
    print("\nCompiling metrics...")
    metrics = helper.method_decoder(transmitted_data)
    end_time = time.time()
    helper.print_metrics(metrics)
    print(f"Time elapsed for simulation: {(end_time - start_time):.4f} seconds")

if __name__ == "__main__":
    main()