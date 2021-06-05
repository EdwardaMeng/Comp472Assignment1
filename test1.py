import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pylab
import pylab as pb

if __name__ == '__main__':
    x = int(input())
    row = x
    y = int(input())
    column = y
    # a = float(input())
    # b = float(input())
    # point = (a , b)
    G = nx.grid_2d_graph(x, y)
    H = nx.Graph()
    # H.add_node(point)
    # Hpos = dict((n,n) for n in H.nodes)
    Gpos = dict((n, n) for n in G.nodes())
    labels = dict((((i, j), (i + 1 + x * j)) for i, j in G.nodes()))
    color_map = []
    Quarantine = [(1, 1)]
    Vaccine = [(3, 1)]
    for node in G:
        if node == (1, 1):
            color_map.append('blue')
        elif node == (3, 1):
            color_map.append('black')
        else:
            color_map.append('green')

    Horiziontal = {}
    Vertical = {}
    for i in range(row - 1):
        for j in range(column):
            Horiziontal[(i, j), (i + 1, j)] = 1

    for i in range(row - 1):
        for j in range(column):
            node = (i, j)
            uppernode = (i, j + 1)
            if j == 0 or j == column - 1 or i == 0 or i == row:
                Horiziontal[(i, j), (i + 1, j)] = 1
            elif Vaccine.__contains__(node):
                if Vaccine.__contains__(uppernode):
                    Horiziontal[(i, j), (i + 1, j)] = 2
                elif Quarantine.__contains__(uppernode):
                    Horiziontal[(i, j), (i + 1, j)] = 1
                else:
                    Horiziontal[(i, j), (i + 1, j)] = 1.5
            elif Quarantine.__contains__(node):
                if Vaccine.__contains__(uppernode):
                    Horiziontal[(i, j), (i + 1, j)] = 1
                elif Quarantine.__contains__(uppernode):
                    Horiziontal[(i, j), (i + 1, j)] = 0
                else:
                    Horiziontal[(i, j), (i + 1, j)] = 0.5


    for i in range(row):
        for j in range(column - 1):
            Vertical[(i, j), (i, j + 1)] = 1

    G.add_edge((0, 0), (0, 1))
    nx.draw_networkx_nodes(G, pos=Gpos, node_color=color_map)
    nx.draw_networkx_labels(G, pos=Gpos, labels=labels, font_color="white")
    nx.draw_networkx_edges(G, pos=Gpos)
    nx.draw_networkx_edge_labels(G, edge_labels=Horiziontal, pos=Gpos)
    nx.draw_networkx_edge_labels(G, edge_labels=Vertical, pos=Gpos)

    # nx.draw_networkx_nodes(H, pos=Hpos, node_color='black', node_shape='*')
    plt.show()
