#!/usr/bin/env/python

import collections
import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    decoded = ''
    for i in range(len(input_data[0])):
        frequencies = collections.Counter([x[i] for x in input_data])
        decoded += sorted(frequencies.items(), key=lambda x: x[1])[0][0]
    print(decoded)
            
if __name__ == '__main__':
    main()
