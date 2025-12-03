#hamming.py
#Last Updated: 12/03/2025
#By: Auto-generated

import ecc_methods.helper as helper

def _int_to_bits(n, width):
    return [(n >> i) & 1 for i in range(width)][::-1]

def _bits_to_int(bits):
    n = 0
    for b in bits:
        n = (n << 1) | int(b)
    return n

def _encode_block_4bits(block):
    # block: string of 4 bits
    d = [int(b) for b in block]
    # positions: [p1,p2,d1,p3,d2,d3,d4] (1-indexed)
    p1 = d[0] ^ d[1] ^ d[3]
    p2 = d[0] ^ d[2] ^ d[3]
    p3 = d[1] ^ d[2] ^ d[3]
    out = [p1, p2, d[0], p3, d[1], d[2], d[3]]
    return ''.join(str(x) for x in out)

def _decode_block_7bits(block):
    b = [int(x) for x in block]
    p1, p2, d1, p3, d2, d3, d4 = b
    s1 = p1 ^ d1 ^ d2 ^ d4
    s2 = p2 ^ d1 ^ d3 ^ d4
    s3 = p3 ^ d2 ^ d3 ^ d4
    syndrome = (s1 << 2) | (s2 << 1) | s3
    # correct if syndrome != 0
    if syndrome != 0 and 1 <= syndrome <= 7:
        idx = syndrome - 1
        b[idx] = 1 - b[idx]
    # extract data bits
    d_bits = [b[2], b[4], b[5], b[6]]
    return ''.join(str(x) for x in d_bits)

def encode(data):
    global encoded_data
    # pad data to multiple of 4
    pad_len = (4 - (len(data) % 4)) % 4
    data_padded = data + ('0' * pad_len)
    encoded_parts = []
    for i in range(0, len(data_padded), 4):
        encoded_parts.append(_encode_block_4bits(data_padded[i:i+4]))
    encoded_data = ''.join(encoded_parts)
    return encoded_data

def decode(transmitted_data):
    return helper.compute_metrics(
        encoded_data=encoded_data,
        transmitted_data=transmitted_data,
        decode_func=decode_hamming
    )

def decode_hamming(encoded_data_local, test_results):
    # encoded_data_local consists of 7-bit blocks
    decoded = ''
    nblocks = len(encoded_data_local) // 7
    for blk in range(nblocks):
        bits = []
        for test in test_results:
            start = blk * 7
            seg = test[start:start+7]
            if len(seg) == 7:
                # correct single-bit errors per test and extract data
                bits.append(_decode_block_7bits(seg))
        # majority vote per data bit across tests
        for j in range(4):
            bit_choices = [b[j] for b in bits]
            decoded += '1' if bit_choices.count('1') > bit_choices.count('0') else '0'

    return decoded
