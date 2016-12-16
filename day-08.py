#!/usr/bin/env/python

import sys

def rotate(l, n):
    n = n % len(l)
    return l[n:] + l[:n]

display = [['.' for x in range(50)] for y in range(6)]

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    for instruction in input_data:
        if instruction.startswith('rect'):
            y_size, x_size = instruction.split()[1].split('x')
            for x in range(int(x_size)):
                for y in range(int(y_size)):
                    display[x][y] = '#'
        if instruction.startswith('rotate'):
            amt = instruction.split()[4]
            axis, index = instruction.split()[2].split('=')
            if axis == 'x':
                column = [row[int(index)] for row in display]
                column = rotate(column, -int(amt))
                for y, row in enumerate(display):
                    row[int(index)] = column[y]
                    display[y] = row
            if axis == 'y':
                row = display[int(index)]
                row = rotate(row, -int(amt))
                display[int(index)] = row
    lit_pixels = 0
    for row in display:
        for column in row:
            if column == '#':
                lit_pixels += 1
    print(lit_pixels)
    for row in display:
        print(''.join(row))

if __name__ == '__main__':
    main()
