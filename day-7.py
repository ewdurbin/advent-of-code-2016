#!/usr/bin/env/python

import re
import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    tls_support = 0
    for line in input_data:
        bracketed = re.findall(r"\[([A-Za-z0-9_]+)\]", line)
        supports = None
        for i in range(len(line)-3):
            if supports == False:
                break
            if line[i:i+2] == line[i+2:i+4][::-1] and line[i] != line[i+1]:
                supports = True
                for b in bracketed:
                    if line[i:i+4] in b:
                        supports = False
        if supports:
            tls_support += 1
    print(tls_support)
        

if __name__ == '__main__':
    main()
