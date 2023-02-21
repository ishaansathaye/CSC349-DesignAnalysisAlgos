import sys


class node:
    def __init__(self, name, out_edges, in_edges, previsit,
                 postvisit, component):
        self.name = name
        self.out_edges = out_edges
        self.in_edges = in_edges
        self.previsit = previsit
        self.postvisit = postvisit
        self.component = component
        self.firstVisit = False
        self.secVisit = False


def visit(G, v, stack):
    v.firstVisit = True
    for w in v.out_edges:
        if not G[w].firstVisit:
            visit(G, G[w], stack)
    stack.append(v)


def assign(G, v, components):
    v.secVisit = True
    components.append(v.name)
    for w in v.in_edges:
        if not G[w].secVisit:
            assign(G, G[w], components)
    return components


def strong_connectivity(G):
    stack = []
    for v in G:
        if not v.firstVisit:
            visit(G, v, stack)

    components = []

    while stack:
        v = stack.pop()
        if not v.secVisit:
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
    G = read_file(filename)
    components = strong_connectivity(G)
    print(components)


if __name__ == '__main__':
    main()
