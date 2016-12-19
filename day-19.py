#!/usr/bin/env/python

import sys

def main():
    input_data = int(sys.stdin.read().rstrip())
    elves = range(input_data)
    while len(elves) > 1:
        if len(elves) % 2 == 0:
            elves = elves[::2]
        else:
            elves = elves[2::2]
    print elves[0] + 1

if __name__ == '__main__':
    main()

