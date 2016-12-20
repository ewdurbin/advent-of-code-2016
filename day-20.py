#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    ranges = []
    for interval in sorted(input_data, key=lambda x: int(x.split('-')[0])):
        ranges.append(tuple((int(x) for x in interval.split('-'))))
    ip, index = 0, 0
    total = 0
    while ip <= 4294967295:
        if ip >= ranges[index][0]:
            if ip <= ranges[index][1]:
                ip = ranges[index][1] + 1
                continue
            index += 1
        else:
            ip += 1
            total += 1
    print(total)

if __name__ == '__main__':
    main()
