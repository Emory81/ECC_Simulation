#sprompt.py
#Last Updated: 11/14/2025
#By: Emory H.

#prompts before simulation

def ecc_input():
    global ecc_method

    print("Please choose an ECC method:")
    print("1. Parity Bit")
    print("2. Hamming Code")
    print("3. Reed-Solomon Code")
    print("4. Redudancy Code")
    print("5. Checksum Code")
    print("6. No ECC")
    ecc_method = input("Enter the number corresponding to your choice: ")
    if ecc_method == '1' or ecc_method == '2' or ecc_method == '3' or ecc_method == '4' or ecc_method == '5' or ecc_method == '6':
        print(f"You have selected option {ecc_method}.")
    else:
        print("Invalid selection. Please try again.")
        return

    return ecc_method

def medium_input():
    global ecc_medium

    print("Please choose a transmission medium:")
    print("1. Copper Wire")
    print("2. Fiber Optic Cable")
    print("3. Coaxial Cable")
    print("4. Cat6 Ethernet Cable")
    print("5. Satellite Radio")
    print("6. 5th Generation Network")
    print("7. FM Radio")
    print("8. Wifi 7")
    ecc_medium = input("Enter the number corresponding to your choice: ")
    if ecc_medium == '1' or ecc_medium == '2' or ecc_medium == '3' or ecc_medium == '4' or ecc_medium == '5' or ecc_medium == '6' or ecc_medium == '7' or ecc_medium == '8':
        print(f"You have selected option {ecc_medium}.")
    else:
        print("Invalid selection. Please try again.")
        return

    return ecc_medium

def environmental_variables():
    global noise_level, hops, error_rate, medium_length, test_amount, message_length

    print("Please specify the environmental variables for the simulation:")

    # noise level
    noise_level = ""
    while noise_level not in ['0','1', '2', '3']:
        noise_level = input("(1 of 6) Enter the noise level (0: none, 1: low, 2: medium, 3: high): ")
        if noise_level not in ['0','1', '2', '3']:
            print("Invalid selection. Please input 0, 1, 2, or 3.")

    # hops
    hops = ""
    valid_hops = [str(i) for i in range(0, 11)]
    while hops not in valid_hops:
        hops = input("(2 of 6) Enter the number of hops (0-10): ")
        if hops not in valid_hops:
            print("Invalid selection. Please input an integer between 0 and 10.")

    # error rate
    error_rate = ""
    while True:
        error_rate = input("(3 of 6) Enter the error rate exaggerated multiplier (ex. 1.25): ")
        try:
            float(error_rate)
            break
        except ValueError:
            print("Invalid selection. Please input a number (decimals allowed).")

    # medium length
    medium_length = ""
    valid_lengths = [str(i) for i in range(1, 1001)]
    while medium_length not in valid_lengths:
        medium_length = input("(4 of 6) Enter the length of the medium in kilometers (1–1000): ")
        if medium_length not in valid_lengths:
            print("Invalid selection. Please input an integer between 1 and 1000.")
    
    # test amount
    test_amount = ""
    valid_tests = [str(i) for i in range(1, 100001)]
    while test_amount not in valid_tests:
        test_amount = input("(5 of 6) Enter the number of tests to run (1–100000): ")
        if test_amount not in valid_tests:
            print("Invalid selection. Please input an integer between 1 and 100000.")
    
    #message lenth
    message_length = ""
    valid_method_lengths = [str(i) for i in range(1, 100001)]
    while message_length not in valid_method_lengths:
        message_length = input("(6 of 6) Enter the length of the message in bits (1–100000): ")
        if message_length not in valid_method_lengths:
            print("Invalid selection. Please input an integer between 1 and 100000.")

    return noise_level, hops, error_rate, medium_length, test_amount, message_length

def main():
    #while ecc_input() is not selected, keep prompting the user
    while ecc_input() is None:
        ecc_input()
    while medium_input() is None:
        medium_input()
    environmental_variables()