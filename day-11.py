#!/usr/bin/env/python

import itertools
import collections
import copy
import string
import sys

class State(object):
    def __init__(self, floors, elevator):
        self.floors = floors
        self.elevator = elevator

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
        return State(floors, dest_floor)

    def iterate(self):
        if self.elevator == 0:
            dest_floors = [self.elevator + 1]
        elif self.elevator == len(self.floors) - 1:
            dest_floors = [self.elevator - 1]
        else:
            dest_floors = [self.elevator - 1, self.elevator + 1]

        items = list(itertools.combinations(self.floors[self.elevator], 2))
        items += list(itertools.combinations(self.floors[self.elevator], 1))

        new_states = []
        for move in [move for move in itertools.product(dest_floors, items)]:
            new_state = self.apply(*move)
            if new_state.valid():
                new_states.append(new_state)
        return new_states

    def solved(self):
        for i in range(len(self.floors) - 1):
            if len(self.floors[i]) != 0:
                return False
        return True

def generalize_state(state):
    new_state = collections.defaultdict(list)
    identifiers = list(string.ascii_lowercase)
    seen_elements = {}
    for floor, items in state.iteritems():
        if floor == 'E':
            new_state['E'] = items
            continue
        for item in sorted(items):
            parts = item.split('-')
            element = parts[1]
            if element not in seen_elements:
                seen_elements[element] = identifiers.pop(0)
            parts[1] = seen_elements[element]
            new_state[floor].append('-'.join(parts))
    return new_state

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
    generation = [State(state, 0)]
    moves = 0
    known_states = [x.__repr__() for x in generation]
    while True:
        moves += 1
        print('moves: {}'.format(moves))
        print('generation: {}'.format(len(generation)))
        print('known: {}'.format(len(known_states)))
        new_generation = []
        for state in generation:
            new_generation += state.iterate()
        if any([x.solved() for x in new_generation]):
            print('solved in {} moves'.format(moves))
            break
        generation = [x for x in new_generation if x.__repr__() not in known_states]
        known_states += [x.__repr__() for x in new_generation if x.__repr__() not in known_states]

if __name__ == '__main__':
    main()
