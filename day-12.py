#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
    i = 0
    while True:
        if i >= len(input_data):
            break
        instr = input_data[i]
        if instr.startswith('cpy'):
            if instr.split()[1] in 'abcd':
                value = registers[instr.split()[1]]
            else:
                value = int(instr.split()[1])
            registers[instr.split()[2]] = value
        if instr.startswith('inc'):
            registers[instr.split()[1]] += 1
        if instr.startswith('dec'):
            registers[instr.split()[1]] -= 1
        if instr.startswith('jnz'):
            x, y = instr.split()[1:3]
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
