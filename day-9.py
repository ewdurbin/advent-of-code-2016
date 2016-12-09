#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip()
    decompressed = ''
    sentinel = None
    for i, character in enumerate(input_data):
        if sentinel is not None and i <= sentinel:
            continue
        else:
            sentinel = None
        if character == '(':
            while True:
                for j, character in enumerate(input_data[i:]):
                    if character == ')':
                        break
                break
            length, repeats = input_data[i+1:i+j].split('x')
            sentinel = i + j +  int(length)
            decompressed += int(repeats) * input_data[i+j+1:i+j+1+int(length)]
        else:
            decompressed += character
    print(len(decompressed))

if __name__ == '__main__':
    main()
