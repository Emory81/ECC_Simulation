#redudancy.py
#Last Updated: 11/15/2025
#By: Emory H.

#This module implements the Redundancy ECC method.

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
    # Split the transmitted tests and get the original data length
    test_results = transmitted_data.split(',')
    data_len = len(encoded_data) // num_repeats

    metrics = {
        "total_tests": len(test_results),
        "error_free_tests": 0,
        "tests_with_errors": 0,
        "bit_error_counts": [],
        "bit_error_rates": []
    }

    for test in test_results:
        if len(test) != len(encoded_data):
            print("Warning: transmitted data length does not match encoded data length.")
        
        # Count errors by comparing bit by bit
        bit_errors = sum(1 for a, b in zip(encoded_data, test) if a != b)
        
        metrics["bit_error_counts"].append(bit_errors)
        metrics["bit_error_rates"].append(bit_errors / len(encoded_data))

        if bit_errors == 0:
            metrics["error_free_tests"] += 1
        else:
            metrics["tests_with_errors"] += 1

    # Decode using majority vote for each block
    decoded_message = ""
    for i in range(data_len):
        bits = [test[j] for test in test_results for j in range(i * num_repeats, (i + 1) * num_repeats)]
        decoded_message += '1' if bits.count('1') > bits.count('0') else '0'

    metrics["decoded_message"] = decoded_message
    return metrics