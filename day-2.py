#!/usr/bin/env/python

import sys


DIRECTIONS = {
    1: {'U': 1, 'D': 4, 'R': 2, 'L': 1},
    2: {'U': 2, 'D': 5, 'R': 3, 'L': 1},
    3: {'U': 3, 'D': 6, 'R': 3, 'L': 2},
    4: {'U': 1, 'D': 7, 'R': 5, 'L': 4},
    5: {'U': 2, 'D': 8, 'R': 6, 'L': 4},
    6: {'U': 3, 'D': 9, 'R': 6, 'L': 5},
    7: {'U': 4, 'D': 7, 'R': 8, 'L': 7},
    8: {'U': 5, 'D': 8, 'R': 9, 'L': 7},
    9: {'U': 6, 'D': 9, 'R': 9, 'L': 8},
}

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    key = 5
    code = []
    for command in input_data:
        for movement in command:
            key = DIRECTIONS[key][movement]
        code.append(key)
    print(''.join([str(x) for x in code]))

if __name__ == '__main__':
    main()
