#!/usr/bin/env/python

from collections import deque
import sys

def main():
    input_data = int(sys.stdin.read().rstrip())
    elves = deque(range(1,input_data+1))
    while len(elves) > 1:
        n = int(len(elves)/2)
        elves.rotate(-n)
        elves.popleft()
        elves.rotate(n)
        elves.rotate(-1)
    print elves[0]

if __name__ == '__main__':
    main()

