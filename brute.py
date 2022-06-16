import sys

import networkx as nx
from networkx import grid_graph
import matplotlib.pyplot as plt


def hamiltonians(G, vis = []):
    if not vis:
        for n in G.nodes():
            for p in hamiltonians(G, [n]):
                yield p
    else:
        dests = set(G[vis[-1]]) - set(vis)
        if not dests and len(vis) == len(G):
            yield vis
        for n in dests:
            for p in hamiltonians(G, vis + [n]):
                yield p

if __name__ == "__main__":
    n = int(sys.argv[1])
    lattice = grid_graph(dim=(n, n))
    paths = list(hamiltonians(lattice))
