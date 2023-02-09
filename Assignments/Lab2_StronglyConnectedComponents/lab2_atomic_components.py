# A template for lab 2 - strong connectivity in graphs - for CSC 349 at Cal Poly
# Reads a file with a list of edges, then creates one component for each node and outputs it to the screen
# Credit: Rodrigo Canaan

import sys
import math


class node:

    def __init__(self, name, out_edges=[], in_edges=[], previsit=-1, postvisit=-1, component=None):
        self.name = name
        self.out_edges = out_edges
        self.in_edges = in_edges
        self.previsit = previsit
        self.postvisit = postvisit
        self.component = component


def strong_connectivity(G):
    components = [[n.name] for n in G]
    sort_component_list(components)
    return components


def sort_component_list(components):
    for c in components:
        c.sort()
    components.sort(key=lambda x: x[0])


def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        v = int(lines[0])
        if v == 0:
            raise ValueError("Graph must have one or more vertices")
        G = list(node(i) for i in range(v))
        for l in lines[1:]:
            tokens = l.split(",")
            fromVertex, toVertex = (int(tokens[0]), int(tokens[1]))
            G[fromVertex].out_edges.append(toVertex)
            G[toVertex].in_edges.append(fromVertex)
        return G


def main():
    filename = sys.argv[1]
    G = read_file(filename)
    components = strong_connectivity(G)
    print(components)


if __name__ == '__main__':
    main()
