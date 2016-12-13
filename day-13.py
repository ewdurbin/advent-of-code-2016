#!/usr/bin/env/python

import sys


class Space(object):
    def __init__(self, x, y, fav):
        self.x, self.y, self.fav = x, y, fav
        self.value = sum([int(c) for c in "{0:b}".format(self.score())])
        if (self.value % 2) == 0:
            self.rep = "."
        else:
            self.rep = "#"

    def __repr__(self):
        return "Space ({}, {})".format(self.x, self.y)

    def score(self):
        return self.x*self.x + 3*self.x + 2*self.x*self.y + self.y + self.y*self.y + self.fav

    def distance(self, x, y):
        return (abs(x-self.x) + abs(y-self.y))

    def solved(self, x, y):
        return (self.x, self.y) == (x, y)

    def iterate(self):
        neighbors = [(self.x, self.y-1), (self.x, self.y+1),
                     (self.x-1, self.y), (self.x+1, self.y)]
        neighbors = [n for n in neighbors if all([n[0] >= 0, n[1] >= 0])]
        ses = []
        for x, y in neighbors:
            new_space = Space(x, y, self.fav)
            if new_space.rep == '.':
                ses.append(new_space)
        return ses


def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    fav_number = int(input_data[0])
    start = Space(1, 1, fav_number)
    generation = [start]
    known_places = set([repr(start)])
    moves = 0
    while moves < 50:
        moves += 1
        print('moves: {}'.format(moves))
        print('generation: {}'.format(len(generation)))
        print('known: {}'.format(len(known_places)))
        new_generation = []
        for space in generation:
            new_generation += [s for s in space.iterate() if repr(s) not in known_places]
            known_places |= set([repr(s) for s in new_generation])
        generation = new_generation
    print(len(known_places))

if __name__ == '__main__':
    main()

