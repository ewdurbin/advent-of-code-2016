#!/usr/bin/env/python

import sys


DIRECTIONS = {
    '1': {'U': '1', 'D': '3', 'R': '1', 'L': '1'},
    '2': {'U': '2', 'D': '6', 'R': '3', 'L': '2'},
    '3': {'U': '1', 'D': '7', 'R': '4', 'L': '2'},
    '4': {'U': '4', 'D': '8', 'R': '4', 'L': '3'},
    '5': {'U': '5', 'D': '5', 'R': '6', 'L': '5'},
    '6': {'U': '2', 'D': 'A', 'R': '7', 'L': '5'},
    '7': {'U': '3', 'D': 'B', 'R': '8', 'L': '6'},
    '8': {'U': '4', 'D': 'C', 'R': '9', 'L': '7'},
    '9': {'U': '9', 'D': '9', 'R': '9', 'L': '8'},
    'A': {'U': '6', 'D': 'A', 'R': 'B', 'L': 'A'},
    'B': {'U': '7', 'D': 'D', 'R': 'C', 'L': 'A'},
    'C': {'U': '8', 'D': 'C', 'R': 'C', 'L': 'B'},
    'D': {'U': 'B', 'D': 'D', 'R': 'D', 'L': 'D'},
}

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    key = '5'
    code = []
    for command in input_data:
        for movement in command:
            key = DIRECTIONS[key][movement]
        code.append(key)
    print(''.join(code))

if __name__ == '__main__':
    main()
