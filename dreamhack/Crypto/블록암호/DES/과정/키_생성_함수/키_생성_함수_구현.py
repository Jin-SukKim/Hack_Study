#!/usr/bin/env python3
# Name: des.py

# Parity Bit Drop Table
PBDT = [57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22,
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4]

# Compression P-Box Table
CPBT = [14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32]

...

def key_scheduling(key: bytearray):
    shift_1 = [0, 1, 8, 15]
    round_keys = []
    
    # Drop parity bit
    parity_erased = permutation(key, PBDT, 56)
    left = parity_erased[:28]
    right = parity_erased[28:]
    
    # Shift
    for i in range(16):
        if i in shift_1:
            left = left[1:] + left[0:1]
            right = right[1:] + right[0:1]
        else:
            left = left[2:] + left[:2]
            right = right[2:] + right[:2]
        
        # Compression
        round_keys.append(permutation(left+right, CPBT, 48))
    
    return round_keys
...

key = "DreamCry"
key_bitarray = plain_to_bits(key)

# Key scheduling
round_keys = key_scheduling(key_bitarray)