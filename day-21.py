#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    password = [c for c in 'abcdefgh']
    for instruction in input_data:
        parts = instruction.split()
        if instruction.startswith('swap position'):
            posx, posy = (int(parts[2]), int(parts[5]))
            valx, valy = (password[posx], password[posy])
            password[posx] = valy
            password[posy] = valx
        if instruction.startswith('swap letter'):
            this, becomes = (parts[2], parts[5])
            for i, p in enumerate(password):
                if p == this:
                    password[i] = becomes
                if p == becomes:
                    password[i] = this
        if instruction.startswith('rotate left'):
            amt = int(parts[2])
            password = password[amt:] + password[:amt]
        if instruction.startswith('rotate right'):
            amt = int(parts[2])
            password = password[-amt:] + password[:-amt]
        if instruction.startswith('rotate based on'):
            amt = ''.join(password).find(parts[6]) + 1
            if amt > 4:
                amt += 1
            for i in range(amt):
                password = password[-1:] + password[:-1]
        if instruction.startswith('reverse positions'):
            start, end = (int(parts[2]), int(parts[4]))
            password = password[:start] + list(reversed(password[start:end+1])) + password[end+1:]
        if instruction.startswith('move position'):
            remove, insert = (int(parts[2]), int(parts[5]))
            value = password.pop(remove)
            password = password[:insert] + [value] + password[insert:]
    print ''.join(password)

if __name__ == '__main__':
    main()
