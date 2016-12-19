#!/usr/bin/env/python

import sys

def main():
    input_data = int(sys.stdin.read().rstrip())
    # used slow solution to look for a pattern in first 1000 or so results
    # - find largest multiple of 3 which is less than target
    # - from here "solutions" increment by 1 up to the first power of three's steps
    # - through to the next power of three, solutions increment by 2
    i = 1
    while i * 3 < input_data:
        i = i * 3
    if i == input_data:
        print input_data
    else:
        modifier = max(input_data - (2 * i), 0)
        print input_data - i + modifier

if __name__ == '__main__':
    main()

