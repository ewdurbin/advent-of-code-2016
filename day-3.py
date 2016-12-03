#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    input_data = [x.split() for x in input_data]
    valid = 0
    for triangle in input_data:
        sides = [int(x) for x in triangle]
        sides = sides + sides
        valid_triangle = True
        for i in range(len(triangle)):
            if sides[i] >= sides[i+1] + sides[i+2]:
                valid_triangle = False
        if valid_triangle:
            valid += 1
    print(valid)

if __name__ == '__main__':
    main()
