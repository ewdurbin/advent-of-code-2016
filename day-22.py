#!/usr/bin/env/python

import sys

def main():
    input_data = sys.stdin.read().rstrip().split('\n')
    """
root@ebhq-gridcenter# df -h
Filesystem              Size  Used  Avail  Use%
/dev/grid/node-x0-y0     85T   64T    21T   75%
    """
    nodes = {}
    for node in input_data:
        fs, size, used, avail, _ = node.split()
        size = int(size[:-1])
        used = int(used[:-1])
        avail = int(avail[:-1])
        nodes[fs] = {'size': size, 'used': used, 'avail': avail}
    viable_pairs = []
    for node, data in nodes.iteritems():
        for n, d in nodes.iteritems():
            if node == n:
                continue
            if data['used'] > 0 and data['used'] <= d['avail']:
                viable_pairs.append('&'.join(sorted([node, n])))
    print len(set(viable_pairs))
if __name__ == '__main__':
    main()
