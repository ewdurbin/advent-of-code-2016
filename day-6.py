#!/usr/bin/env/python

import collections
import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    decoded = ''
    for i in range(len(input_data[0])):
        decoded += collections.Counter([x[i] for x in input_data]).most_common(1)[0][0]
    print(decoded)
            
if __name__ == '__main__':
    main()
