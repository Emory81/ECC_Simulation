#main.py
#Last Updated: 11/14/2025
#By: Emory H.

#This program will simulate how Error Correction Codes (ECC) work in data transmission.

import random
import sprompt
import ecc_methods as ecc

def data_creator():
    data_string = ""
    for i in range(int(sprompt.message_length)):
        data = random.choice(['0', '1'])
        data_string += data

    return data_string

def method_runner(data_string):
    if sprompt.ecc_method == '4':
        ecc.redundancy.encode(data_string)

def main():
    sprompt.main()
    data_string = data_creator()
    method_runner(data_string)

if __name__ == "__main__":
    main()