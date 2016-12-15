#!/usr/bin/env/python

import sys


def main():
    discs = []
    input_data = sys.stdin.read().rstrip().split('\n')
    for disc in input_data:
        parts = disc.split()
        positions = int(parts[3])
        position = int(parts[11].rstrip('.'))
        discs.append((position, positions))
    i = 0
    j = 0
    while True:
        clear = []
        for disc in discs:
            clear.append((disc[0] + i + j) % disc[1] == 0)
            j += 1
        if all(clear):
            break
        i += 1
        j = 0
    print i - 1

if __name__ == '__main__':
    main()

