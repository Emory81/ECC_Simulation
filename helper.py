#main.py
#Last Updated: 11/20/2025
#By: Emory H.

#Helper functions for the main.py file.

import random
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