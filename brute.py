import sys

import networkx as nx
from networkx import grid_graph
from networkx.relabel import convert_node_labels_to_integers
import matplotlib.pyplot as plt


def hamiltonians(G, vis = []):
    if not vis:
        for n in G.nodes():
            for p in hamiltonians(G, [n]):
                yield p
    else:
        dests = set(G[vis[-1]]) - set(vis)
        if not dests and len(vis) == len(G.nodes()):
            yield vis
        for n in dests:
            for p in hamiltonians(G, vis + [n]):
                yield p

def lattice_draw(lattice, walk):
    steps = [(walk[i], walk[i+1]) for i in range(0, len(walk)-1)]

    pos = nx.spring_layout(lattice)
    nx.draw_networkx_nodes(lattice, pos)
    nx.draw_networkx_edges(lattice, pos, edgelist=steps)
    plt.show()
    pass
if __name__ == "__main__":
    # n = int(sys.argv[1])
    n = 4
    lattice = grid_graph(dim=(n, n))
    lattice = convert_node_labels_to_integers(lattice)
    ps = list(hamiltonians(lattice))
    print(len(ps))
    for path in ps:
        lattice_draw(lattice, path)
