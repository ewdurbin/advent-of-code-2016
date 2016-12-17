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
            if x > 3 or y > 3:
                continue
            new_space = Space(x, y, self.input_data, self.path + [direction])
            ses.append(new_space)
        return ses


def main():
    input_data = sys.stdin.read().rstrip()
    path = []
    digest = hashlib.md5(input_data + ''.join(path)).hexdigest()
    generation = [Space(0, 0, input_data, [])]
    paths = []
    while True:
        new_generation = []
        for space in generation:
            new_generation += [s for s in space.iterate()]
        if any([x.solved(3,3) for x in new_generation]):
            paths += [''.join(x.path) for x in new_generation if x.solved(3,3)]
        if len(new_generation) == 0:
            break
        generation = [x for x in new_generation if x.solved(3,3) == False]
    print max([len(p) for p in paths])


if __name__ == '__main__':
    main()

