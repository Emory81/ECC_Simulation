#redudancy.py
#Last Updated: 11/15/2025
#By: Emory H.

#This module implements the Redundancy ECC method.

def encode(data):
    num_repeats = input("How many times would you like to repeat each message for redundancy? (1-100): ")
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