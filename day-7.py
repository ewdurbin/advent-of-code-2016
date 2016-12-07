#!/usr/bin/env/python

import re
import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    ssl_support = 0
    for line in input_data:
        bracketed = re.findall(r"\[([A-Za-z0-9_]+)\]", line)
        for b in bracketed:
            line = line.replace('[%s]' % (b,), '')
        supports = False
        for i in range(len(line)-2):
            if supports:
                break
            if line[i] == line[i+2] and line[i] != line[i+1]:
                for b in bracketed:
                    if '%s%s%s' % (line[i+1], line[i], line[i+1]) in b:
                        supports = True
        if supports:
            ssl_support += 1
    print(ssl_support)
        

if __name__ == '__main__':
    main()
