#helper.py
#Last Updated: 11/20/2025
#By: Emory H.

#This module provides helper functions for ECC methods.

def compute_metrics(encoded_data, transmitted_data, decode_func):

    test_results = transmitted_data.split(',')
    encoded_len = len(encoded_data)

    metrics = {
        "total_tests": len(test_results),
        "error_free_tests": 0,
        "tests_with_errors": 0,
        "bit_error_counts": [],
        "bit_error_rates": []
    }

    for test in test_results:
        if len(test) != encoded_len:
            print("Warning: transmitted data length mismatch. Skipping length validation.")

        # Bit errors
        bit_errors = sum(1 for a, b in zip(encoded_data, test) if a != b)
        metrics["bit_error_counts"].append(bit_errors)
        metrics["bit_error_rates"].append(bit_errors / encoded_len)

        if bit_errors == 0:
            metrics["error_free_tests"] += 1
        else:
            metrics["tests_with_errors"] += 1

    # Use ECC-specific decode function
    metrics["decoded_message"] = decode_func(encoded_data, test_results)

    return metrics