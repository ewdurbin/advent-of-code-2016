#!/usr/bin/env/python

import itertools
import copy
import string
import sys
import Queue

class State(object):
    def __init__(self, floors, elevator, moves):
        self.floors = floors
        self.elevator = elevator
        self.moves = moves

    def __repr__(self):
        output = []
        for i, floor in enumerate(self.floors):
            if i == self.elevator:
                e = 'E'
            else:
                e = '_'
            output.append('{} {}'.format(e, floor))
        return '\n'.join(output)

    def valid(self):
        for floor in self.floors:
            chips = [x for x in floor if x.startswith('chip-')]
            gens = [x for x in floor if x.startswith('gen-')]
            shielded = [x for x in chips if 'gen-' + x.split('-')[1] in gens]
            chips = [x for x in chips if x not in shielded]
            if len(gens) > 0 and len(chips) > 0:
                return False
        return True

    def apply(self, dest_floor, items):
        floors = copy.deepcopy(self.floors)
        for item in items:
            floors[self.elevator].remove(item)
            floors[dest_floor] += [item]
        return State(floors, dest_floor, self.moves + 1)

    @property
    def score(self):
        score = 0
        for i, floor in enumerate(self.floors):
            score += -i * len(floor)
        return score

    def iterate(self):
        if self.elevator == 0:
            dest_floors = [self.elevator + 1]
        elif self.elevator == len(self.floors) - 1:
            dest_floors = [self.elevator - 1]
        else:
            dest_floors = [self.elevator - 1, self.elevator + 1]

        items = list(itertools.combinations(self.floors[self.elevator], 2))
        items += list(itertools.combinations(self.floors[self.elevator], 1))

        moves = [move for move in itertools.product(dest_floors, items) if self.apply(*move).valid()]
        if any([len(y) == 2 for x, y in moves if x > self.elevator]):
            moves = [(x, y) for x, y in moves if not (len(y) == 1 and x > self.elevator)]
        if any([len(y) == 1 for x, y in moves if x < self.elevator]):
            moves = [(x, y) for x, y in moves if not (len(y) == 2 and x < self.elevator)]

        new_states = []
        for move in moves:
            new_state = self.apply(*move)
            if new_state.valid():
                new_states.append(new_state)
        return new_states

    def solved(self):
        for i in range(len(self.floors) - 1):
            if len(self.floors[i]) != 0:
                return False
        return True

    def generalize(self):
        identifiers = list(string.ascii_lowercase)
        new_floors = [[] for x in range(len(self.floors))]
        seen_elements = {}
        for i, floor in enumerate(self.floors):
            for item in sorted(floor):
                parts = item.split('-')
                element = parts[1]
                if element not in seen_elements:
                    seen_elements[element] = identifiers.pop(0)
                parts[1] = seen_elements[element]
                new_floors[i].append('-'.join(parts))
        return State(new_floors, self.elevator, self.moves).__repr__()

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    max_floor = len(input_data)
    state = [[] for x in range(max_floor)]
    for i, floor in enumerate(input_data):
        for j, word in enumerate(floor.split()):
            if word in ('generator', 'generator.', 'generator,'):
                state[i].append('gen-' + floor.split()[j-1])
            if word in ('microchip', 'microchip.', 'microchip,'):
                state[i].append('chip-' + floor.split()[j-1].split('-')[0])
    generation = Queue.PriorityQueue()
    generation.put((State(state, 0, 0).score, State(state, 0, 0)))
    known_states = set(State(state, 0, 0).generalize())
    i = 0
    while True:
        state = generation.get()[1]
        new_generations = [x for x in state.iterate() if x.generalize() not in known_states]
        for s in new_generations:
            generation.put((s.score, s))
        known_states |= set([x.generalize() for x in new_generations])
        if any([x.solved() for x in new_generations]):
            solved = [x for x in new_generations if x.solved()]
            print('solved in {} moves'.format(solved[0].moves))
            print('solved in {} iterations'.format(i))
            break
        if i % 1000 == 0:
            print generation.qsize()
        i += 1

if __name__ == '__main__':
    main()
