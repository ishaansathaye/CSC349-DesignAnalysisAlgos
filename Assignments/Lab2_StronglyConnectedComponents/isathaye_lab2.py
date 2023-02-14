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
        self.visited = False


def dfs_1(G, v, clock):
    if v.previsit == -1:
        v.previsit = clock
        clock += 1
        for w in v.out_edges:
            clock = dfs_1(G, G[w], clock)
        v.postvisit = clock
        clock += 1
    return clock


def assign(G, v, components):
    v.visited = True
    components.append(v.name)
    for w in v.in_edges:
        if G[w].visited == False:
            assign(G, G[w], components)
    return components


def strong_connectivity(G):
    for v in G:
        if v.previsit == -1:
            dfs_1(G, v, 0)

    sorted_list = []
    for v in G:
        sorted_list.append(v)
    sorted_list.sort(key=lambda x: x.postvisit, reverse=True)

    components = []
    for v in sorted_list:
        if v.visited == False:
            components.append(assign(G, v, []))
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
    filename = sys.argv[1]
    # filename = "Assignments/Lab2_StronglyConnectedComponents/lab2_example1"
    G = read_file(filename)
    components = strong_connectivity(G)
    print(components)


if __name__ == '__main__':
    main()
