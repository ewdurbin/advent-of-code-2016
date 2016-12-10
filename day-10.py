#!/usr/bin/env/python

import collections
import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    bots = {}
    state = collections.defaultdict(list)
    for line in input_data:
        if line.startswith('value'):
            value = line.split()[1]
            bot = line.split()[5]
            state['bot-{}'.format(bot)].append(int(value))
        if line.startswith('bot'):
            bot = line.split()[1]
            low_target, low_index = line.split()[5:7]
            high_target, high_index = line.split()[10:12]
            bots['bot-{}'.format(bot)] = {'low': '{}-{}'.format(low_target, low_index),
                                          'high': '{}-{}'.format(high_target, high_index)}

    while True:
        double_bots = [(k, v) for k, v in state.items() if k.startswith('bot-') and len(v) > 1]
        if len(double_bots) == 0:
            break
        bot, chips = double_bots[-1]
        (low, high) = (min(chips), max(chips))
        if (low, high) == (17, 61):
            print('Part 1: {}'.format(bot))
        state[bots[bot]['low']].append(low)
        state[bots[bot]['high']].append(high)
        del state[bot]

    print('Part 2: {}'.format(state['output-0'][0] * state['output-1'][0] * state['output-2'][0]))

if __name__ == '__main__':
    main()
