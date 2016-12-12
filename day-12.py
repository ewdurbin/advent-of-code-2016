#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    i = 0
    while i < len(input_data):
        instr = input_data[i].split()
        if instr[0] == 'cpy':
            if instr[1] in 'abcd':
                value = registers[instr[1]]
            else:
                value = int(instr[1])
            registers[instr[2]] = value
        if instr[0] == 'inc':
            registers[instr[1]] += 1
        if instr[0] == 'dec':
            registers[instr[1]] -= 1
        if instr[0] == 'jnz':
            x, y = instr[1:3]
            if x in 'abcd':
                value = registers[x]
            else:
                value = int(x)
            if value != 0:
                i += int(y)
                continue
        i+=1

    print(registers['a'])

if __name__ == '__main__':
    main()
