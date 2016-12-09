#!/usr/bin/env/python

import sys

def decompress(input_str):
    sentinel = None
    decompressed = ''
    for i, character in enumerate(input_str):
        if sentinel is not None and i <= sentinel:
            continue
        else:
            sentinel = None
        if character == '(':
            while True:
                for j, character in enumerate(input_str[i:]):
                    if character == ')':
                        break
                break
            length, repeats = input_str[i+1:i+j].split('x')
            sentinel = i + j +  int(length)
            decompressed += int(repeats) * decompress(input_str[i+j+1:i+j+1+int(length)])
        else:
            decompressed += character
    return decompressed

def main():
    input_data = sys.stdin.read().rstrip()
    decompressed = decompress(input_data)
    print len(decompressed)

if __name__ == '__main__':
    main()
