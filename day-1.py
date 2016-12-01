#!/usr/bin/env/python

import sys


DIRECTIONS = {'N': {'R': 'E', 'L': 'W'},
              'E': {'R': 'S', 'L': 'N'},
              'S': {'R': 'W', 'L': 'E'},
              'W': {'R': 'N', 'L': 'S'}}


def main():
    input_data = sys.stdin.read().rstrip().split(', ')
    location = {'N': 0, 'E': 0, 'W': 0, 'S': 0}
    orientation = 'N'
    history = []
    for movement in input_data:
        direction = movement[0]
        distance = int(movement[1:])
        for block in range(1,distance+1):
            location[DIRECTIONS[orientation][direction]] += 1
            coordinate = (location['N'] - location['S'], location['E'] - location['W'])
            history.append(coordinate)
        orientation = DIRECTIONS[orientation][direction]
    for i, coordinate in enumerate(history):
        if coordinate in history[:i]:
            break
    distance = abs(coordinate[0]) + abs(coordinate[1])
    print(distance)

if __name__ == '__main__':
    main()
