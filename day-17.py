#!/usr/bin/env/python

import hashlib
import sys

class Space(object):
    def __init__(self, x, y, input_data, path):
        self.x, self.y, self.input_data, self.path = x, y, input_data, path
        self.digest = hashlib.md5(input_data + ''.join(path)).hexdigest()

    def __repr__(self):
        return "Space ({}, {})".format(self.x, self.y)

    def distance(self, x, y):
        return (abs(x-self.x) + abs(y-self.y))

    def solved(self, x, y):
        return (self.x, self.y) == (x, y)

    def iterate(self):
        neighbors = {'U': (self.x, self.y-1), 'D': (self.x, self.y+1),
                     'L': (self.x-1, self.y), 'R': (self.x+1, self.y)}
        if self.digest[0] not in 'bcdef':
            del(neighbors['U'])
        if self.digest[1] not in 'bcdef':
            del(neighbors['D'])
        if self.digest[2] not in 'bcdef':
            del(neighbors['L'])
        if self.digest[3] not in 'bcdef':
            del(neighbors['R'])
        ses = []
        for direction, (x, y) in neighbors.items():
            if x < 0 or y < 0:
                continue
            print(direction, (x, y))
            new_space = Space(x, y, self.input_data, self.path + [direction])
            ses.append(new_space)
        return ses


def main():
    input_data = sys.stdin.read().rstrip()
    path = []
    digest = hashlib.md5(input_data + ''.join(path)).hexdigest()
    generation = [Space(0, 0, input_data, [])]
    while True:
        new_generation = []
        for space in generation:
            new_generation += [s for s in space.iterate()]
        if any([x.solved(3,3) for x in new_generation]):
            print('solved')
            print[''.join(x.path) for x in new_generation if x.solved(3,3)]
            break
        if len(new_generation) == 0:
            print('failed')
            break
        generation = new_generation


if __name__ == '__main__':
    main()

