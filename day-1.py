#!/usr/bin/env/python

import sys


DIRECTIONS = {'N': {'R': 'E', 'L': 'W'},
              'E': {'R': 'S', 'L': 'N'},
              'S': {'R': 'W', 'L': 'E'},
              'W': {'R': 'N', 'L': 'S'}}


def main():
    input_data = sys.stdin.read().rstrip().split(', ')
    totals = {'N': 0, 'E': 0, 'W': 0, 'S': 0}
    orientation = 'N'
    for movement in input_data:
        direction = movement[0]
        distance = int(movement[1:])
        totals[DIRECTIONS[orientation][direction]] += distance
        orientation = DIRECTIONS[orientation][direction]
    distance = abs(totals['N'] - totals['S']) + abs(totals['E'] - totals['W'])
    print distance

if __name__ == '__main__':
    main()
