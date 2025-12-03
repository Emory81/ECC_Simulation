#reed_solomon.py
#Last Updated: 12/03/2025
#By: Auto-generated

# NOTE: This is a simplified Reed-Solomon-like implementation for the
# purposes of the simulation. It treats the message as bytes (8-bit symbols)
# and appends a single parity symbol computed as XOR of all symbols.
# This is NOT a full RS implementation but provides block-level parity.

import ecc_methods.helper as helper

def _to_symbols(bitstr):
    # pad to multiple of 8
    pad = (8 - (len(bitstr) % 8)) % 8
    bitstr_p = bitstr + ('0' * pad)
    symbols = [int(bitstr_p[i:i+8], 2) for i in range(0, len(bitstr_p), 8)]
    return symbols, pad

def _from_symbols(symbols, pad):
    bits = ''.join(f"{s:08b}" for s in symbols)
    if pad:
        bits = bits[:-pad]
    return bits

def encode(data):
    global encoded_data, _rs_pad
    symbols, pad = _to_symbols(data)
    parity = 0
    for s in symbols:
        parity ^= s
    symbols.append(parity)
    _rs_pad = pad
    encoded_data = _from_symbols(symbols, 0)  # include parity full
    return encoded_data

def decode(transmitted_data):
    return helper.compute_metrics(
        encoded_data=encoded_data,
        transmitted_data=transmitted_data,
        decode_func=decode_rs
    )

def decode_rs(encoded_data_local, test_results):
    # Split into 8-bit symbols, last symbol is parity; perform simple correction by
    # dropping last symbol and returning majority-voted original symbols across tests.
    decoded_bits = ''
    nbits = len(encoded_data_local)
    nsymbols = nbits // 8
    # remove parity symbol from count
    data_symbols_count = nsymbols - 1

    for sym_idx in range(data_symbols_count):
        choices = []
        for test in test_results:
            start = sym_idx * 8
            seg = test[start:start+8]
            if len(seg) == 8:
                choices.append(seg)
        if not choices:
            decoded_bits += '00000000'
            continue
        # majority vote per bit within symbol
        for bpos in range(8):
            bits = [c[bpos] for c in choices]
            decoded_bits += '1' if bits.count('1') > bits.count('0') else '0'

    # strip pad if present
    try:
        pad = _rs_pad
        if pad:
            decoded_bits = decoded_bits[:-pad]
    except NameError:
        pass

    return decoded_bits
