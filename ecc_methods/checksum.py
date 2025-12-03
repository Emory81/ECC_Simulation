#checksum.py
#Last Updated: 12/03/2025
#By: Auto-generated

import ecc_methods.helper as helper

def _to_bytes(bitstr):
    pad = (8 - (len(bitstr) % 8)) % 8
    bitstr_p = bitstr + ('0' * pad)
    bytes_list = [int(bitstr_p[i:i+8], 2) for i in range(0, len(bitstr_p), 8)]
    return bytes_list, pad

def _from_bytes(bytes_list, pad):
    bits = ''.join(f"{b:08b}" for b in bytes_list)
    if pad:
        bits = bits[:-pad]
    return bits

def encode(data):
    global encoded_data, _chk_pad
    bytes_list, pad = _to_bytes(data)
    checksum = sum(bytes_list) & 0xFF
    bytes_list.append(checksum)
    _chk_pad = pad
    encoded_data = _from_bytes(bytes_list, 0)
    return encoded_data

def decode(transmitted_data):
    return helper.compute_metrics(
        encoded_data=encoded_data,
        transmitted_data=transmitted_data,
        decode_func=decode_checksum
    )

def decode_checksum(encoded_data_local, test_results):
    # Reconstruct message by majority vote per bit across tests, then strip checksum
    if not test_results:
        return ''

    bitlen = len(encoded_data_local)
    # majority vote per bit
    reconstructed = ''
    for i in range(bitlen):
        bits = [t[i] for t in test_results if len(t) > i]
        if not bits:
            reconstructed += '0'
        else:
            reconstructed += '1' if bits.count('1') > bits.count('0') else '0'

    # remove checksum (last 8 bits)
    if len(reconstructed) <= 8:
        return ''
    data_bits = reconstructed[:-8]
    try:
        pad = _chk_pad
        if pad:
            data_bits = data_bits[:-pad]
    except NameError:
        pass

    return data_bits
