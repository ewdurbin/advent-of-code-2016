#!/usr/bin/env/python

import sys


def compute(input_data, registers):
    i = 0
    while i < len(input_data):
        instr = input_data[i].split()
        if instr[0] == 'tgl':
            if instr[1] in 'abcd':
                instr[1] = registers[instr[1]]
            if instr[1] < 0 or instr[1] > len(input_data):
                i+=1
                continue
            if i+instr[1] < 0 or i+instr[1] >= len(input_data):
                i += 1
                continue
            prev_instr = input_data[i+instr[1]].split()
            if prev_instr[0] == 'inc':
                new_instr = 'dec'
            if prev_instr[0] == 'dec':
                new_instr = 'inc'
            if prev_instr[0] == 'jnz':
                new_instr = 'cpy'
            if prev_instr[0] == 'cpy':
                new_instr = 'jnz'
            if prev_instr[0] == 'tgl':
                new_instr = 'inc'
            input_data[i+instr[1]] = ' '.join([new_instr] + prev_instr[1:])
            if i+instr[1] == i:
                i += 1
                continue
        if instr[0] == 'inc':
            registers[instr[1]] += 1
        if instr[0] == 'dec':
            registers[instr[1]] -= 1
        if instr[0] == 'cpy':
            if instr[1] in 'abcd':
                value = registers[instr[1]]
            else:
                value = int(instr[1])
            if instr[2] not in 'abcd':
                i+=1
                continue
            registers[instr[2]] = value
        if instr[0] == 'jnz':
            x, y = instr[1:3]
            if x in 'abcd':
                valuex = registers[x]
            else:
                valuex = int(x)
            if y in 'abcd':
                valuey = registers[y]
            else:
                valuey = int(y)
            if valuex != 0:
                i += int(valuey)
                continue
        i+=1
    print(i, registers['a'])

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    compute(input_data, registers)


if __name__ == '__main__':
    main()
