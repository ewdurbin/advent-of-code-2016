#!/usr/bin/env/python

import sys


def invert(data):
    ret = ''
    for x in reversed(data):
        if x == '1':
            ret += '0'
        else:
            ret += '1'
    return ret


def checksum(data):
    chk = ''
    for i in range(len(data)/2):
        if data[i*2] == data[i*2 + 1]:
            chk += '1'
        else:
            chk += '0'
    if len(chk) % 2 == 0:
        chk = checksum(chk)
    return chk

def main():
    input_data = sys.stdin.read().rstrip()
    data = input_data
    while len(data) < 272:
        data = data + '0' + invert(data)
    data = data[:272+1]
    print checksum(data)


if __name__ == '__main__':
    main()

