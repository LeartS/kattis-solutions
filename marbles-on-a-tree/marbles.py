#!/usr/bin/env python3
from sys import stdin

nodes = {}

def visit(i):
    if not nodes[i][1]:
        descendant_marbles, descendant_nodes = 0, 0
    else:
        descendant_marbles, descendant_nodes = [sum(x) for x in zip(*[visit(c) for c in nodes[i][1]])]
    nodes[i][2] = nodes[i][0] + descendant_marbles
    nodes[i][3] = 1 + descendant_nodes
    return nodes[i][2], nodes[i][3]

while True:
    nodes.clear()
    N = int(stdin.readline())
    if N == 0:
        break
    for _ in range(N):
       i, marbles, _, *children = [int(x) for x in stdin.readline().split()]
       nodes[i] = [marbles, children, 0, 0]
    root = (set(range(1, N+1)) - set(c for n in nodes for c in nodes[n][1])).pop()
    visit(root)
    # print(nodes)
    total = 0
    for marbles, _, subtree_marbles, subtree_nodes in nodes.values():
        total += abs(subtree_marbles - subtree_nodes)
    print(total)