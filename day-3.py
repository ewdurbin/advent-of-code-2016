#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    input_data = [x.split() for x in input_data]
    actual_triangles = []
    for i in range(len(input_data)/3):
        block = input_data[(i*3):(i*3)+3]
        for i in range(3):
            actual_triangles.append([block[0][i], block[1][i], block[2][i]])
    valid = 0
    for triangle in actual_triangles:
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
