#!/usr/bin/env/python

import sys

class Node(object):

    def __init__(self, x, y, size, avail, used, maxx, maxy):
        self.x = x
        self.y = y
        self.size = size
        self.avail = avail
        self.used = used
        self.maxx = maxx
        self.maxy = maxy

    def __repr__(self):
        return 'Node[(%s, %s) %sT/%sT]' % (self.x, self.y, self.used, self.size)

    def adjacent(self, grid):
        neighbors = [(self.x-1, self.y), (self.x+1,self.y), (self.x,self.y-1), (self.x, self.y+1)]
        return [(x,y) for (x,y) in neighbors if x >= 0 and x <= self.maxx and y>= 0 and y <= self.maxy]

    def check_move(self, grid, x, y):
        if grid[x][y].avail < self.used:
            return False
        if (x, y) not in self.adjacent(grid):
            return False
        return True

    def viable_pairs(self, grid):
        viable = []
        for line in grid:
            for node in line:
                if self.used > 0 and self.used < node.avail and (self.x, self.y) != (node.x, node.y):
                    viable.append((node.x, node.y))
        return viable

    def moves(self, grid):
        return [(x, y) for (x, y) in self.adjacent(grid) if self.check_move(grid, x, y)]

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    nodes = {}
    maxy = 0
    maxx = 0
    for node in input_data:
        fs, size, used, avail, _ = node.split()
        _, x, y = fs.split('-')
        x = int(x[1:])
        y = int(y[1:])
        maxx = max(maxx, x)
        maxy = max(maxy, y)
        size = int(size[:-1])
        used = int(used[:-1])
        avail = int(avail[:-1])
        nodes[fs] = {'x': x, 'y': y, 'size': size, 'used': used, 'avail': avail}
    grid = [[None for _ in range(maxy+1)] for _ in range(maxx+1)]
    for node, data in nodes.items():
        grid[data['x']][data['y']] = Node(data['x'], data['y'], data['size'], data['avail'], data['used'], maxx, maxy)
    goal_data = (maxx, 0)
    print grid[maxx][0].viable_pairs(grid)


if __name__ == '__main__':
    main()
