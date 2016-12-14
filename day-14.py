#!/usr/bin/env/python

import sys
import hashlib


def main():
    input_data = sys.stdin.read().rstrip().split('\n')[0]
    i = 0
    candidates = []
    keys = []
    while True:
        key = hashlib.md5("%s%s" % (input_data, i)).hexdigest()
        for _ in range(2016):
             key = hashlib.md5(key).hexdigest()
        for j in range(len(key)-2):
            if key[j] == key[j+1] and key[j] == key[j+2]:
                candidates.append((i, key[j], key))
                break
        for j in range(len(key)-4):
            if key[j] == key[j+1] and key[j] == key[j+2] and key[j] == key[j+3] and key[j] == key[j+4]:
                matches = [x for x in candidates if x[1] == key[j] and key != x[2]]
                for m in matches:
                    if i - m[0] < 1000:
                        keys.append(m[2])
                        candidates.remove(m)
                        print m[0]
                    if len(keys) == 64:
                        break
        if len(keys) == 64:
            break
        i += 1

if __name__ == '__main__':
    main()
