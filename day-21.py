#!/usr/bin/env/python

from itertools import permutations
import sys

def scramble(in_pass, input_data):
    password = [c for c in in_pass]
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
            amt = ''.join(password).find(parts[6]) + 1  # WELL SHIT
            if amt > 4:  # I HAD amt >= 4 HERE FOR SO LONG. COMPLETELY BLEW LEADERBOARD ONE LINE UP
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
    return ''.join(password)


def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    for test_pass in permutations('fbgdceah'):
        if scramble(''.join(test_pass), input_data) == 'fbgdceah':
            print(''.join(test_pass))
            break

if __name__ == '__main__':
    main()
