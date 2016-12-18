#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip()
    board = [input_data]
    for i in range(1,400000):
        previous_row = '.' + board[i-1] + '.'
        row = ''
        for i in range(len(previous_row)-2):
            if previous_row[i:i+3] in ('^^.', '.^^', '^..', '..^'):
                row += '^'
            else:
                row += '.'
        board.append(row)
    safe = 0
    for row in board:
        for spot in row:
            if spot == '.':
                safe += 1
    print safe

if __name__ == '__main__':
    main()

