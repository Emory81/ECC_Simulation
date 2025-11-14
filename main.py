#main.py
#Last Updated: 11/14/2025
#By: Emory H.

#This program will simulate how Error Correction Codes (ECC) work in data transmission.

def ecc_input():
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
    print("Please choose a transmission medium:")
    print("1. Copper Wire")
    print("2. Fiber Optic Cable")
    print("3. Coaxial Cable")
    print("4. Cat6 Ethernet Cable")
    print("5. Satellite Radio")
    print("6. 5 Generation Network")
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
    print("Please specify the envirmonmental variables for the simulation:")
    while noise_level not in ['1', '2', '3']:
        noise_level = input("(1 of 3) Enter the noise level (1: low, 2: medium, 3: high): ")
        if noise_level not in ['1', '2', '3']:
            print("Invalid selection. Please input 1, 2, or 3.")
    while hops not in [str(i) for i in range(1, 11)]:
        hops = input("(2 of 3) Enter the number of hops (1-10): ")
        if hops not in [str(i) for i in range(1, 11)]:
            print("Invalid selection. Please input an integer between 1 and 10.")
    while error_rate not in [str(i) for i in range(0, 6)]:
        error_rate = input("(3 of 3) Enter the error rate exagerated multiplier (integers only, ex. 1.25): ")
        if error_rate not in [str(i) for i in range(0, 6)]:
            print("Invalid selection. Please input an integer between 0 and 5.")
    while medium_length not in [str(i) for i in range(1, 1001)]:
        medium_length = input("Enter the length of the medium in kilometers: ")
        if medium_length not in [str(i) for i in range(1, 1001)]:
            print("Invalid selection. Please input an integer between 1 and 1000.")
    
    return noise_level, hops, error_rate, medium_length
def main():
    #while ecc_input() is not selected, keep prompting the user
    while ecc_input() is None:
        ecc_input()
    while medium_input() is None:
        medium_input()
    environmental_variables()

if __name__ == "__main__":
    main()