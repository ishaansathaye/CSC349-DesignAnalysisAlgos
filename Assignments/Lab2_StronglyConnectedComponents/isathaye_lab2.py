# A template for lab 2 - strong connectivity in graphs - for CSC 349 at Cal Poly
# Reads a file with a list of edges and outputs it to the screen
# Credit: Rodrigo Canaan

import sys
import math


class node:
    def __init__(self, name, out_edges, in_edges, previsit, postvisit, component):
        self.name = name
        self.out_edges = out_edges
        self.in_edges = in_edges
        self.previsit = previsit
        self.postvisit = postvisit
        self.component = component


def dfs(G, node, components):
    # Implement depth first search
    # Input: G, a list of nodes
    # Input: node, a node in G
    # Input: components, a list of lists of nodes, where each list of nodes is a strongly connected component
    # Output: None
    # Side effect: node.previsit, node.postvisit, and node.component are updated
    # Side effect: components is updated
    node.previsit = 0
    node.component = node
    components.append([node.name])
    for out_edge in node.out_edges:
        if G[out_edge].previsit == -1:
            dfs(G, G[out_edge], components)
    node.postvisit = 0


def strong_connectivity(G):
    # Implement Kosaraju's algorithm for finding strongly connected components in a graph
    # Input: G, a list of nodes
    # Output: a list of lists of nodes, where each list of nodes is a strongly connected component
    components = []
    for node in G:
        if node.previsit == -1:
            dfs(G, node, components)
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
        G = list(node(name=i, in_edges=[], out_edges=[], previsit=-1,
                      postvisit=-1, component=None) for i in range(v))
        for l in lines[1:]:
            tokens = l.split(",")
            fromVertex, toVertex = (int(tokens[0]), int(tokens[1]))
            G[fromVertex].out_edges.append(toVertex)
            G[toVertex].in_edges.append(fromVertex)
    return G


def main():
    # filename = sys.argv[1]
    filename = "Assignments/Lab2_StronglyConnectedComponents/lab2_example1"
    G = read_file(filename)
    components = strong_connectivity(G)
    print(components)


if __name__ == '__main__':
    main()
