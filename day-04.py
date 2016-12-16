#!/usr/bin/env/python

import sys
import string
import operator
from collections import Counter, defaultdict

def caesar(plaintext, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    for row in input_data:
        words = row.split('-')[:-1]
        [sectorid, checksum] = row.split('-')[-1].split('[')
        checksum = checksum.replace(']', '')
        counts = Counter(''.join(words))
        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        chars = defaultdict(list)
        for item in sorted_counts:
           chars[item[1]].append(item[0])
        calculated_checksum = ''
        for winner in sorted(chars, reverse=True):
           calculated_checksum += ''.join(sorted(chars[winner]))
        if calculated_checksum[:5] == checksum:
            decoded = caesar(' '.join(words), int(sectorid) % 26)
            if 'north' in decoded:
                print sectorid, decoded

if __name__ == '__main__':
    main()
