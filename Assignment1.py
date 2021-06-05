import random
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
import pylab
import pylab as pb


# Map class
class Map:
    def __init__(self):
        pass

    def build_map(self):
        # Define list of special areas
        Vaccine = []
        Quarantine = []
        Playground = []
        EdgeVaccine = []
        EdgeQuarantine = []
        EdgePlayground = []
        sp = ()
        ep = ()

        # Enter the values
        print("Enter the row:")
        row = int(input())
        print("Enter the column:")
        column = int(input())

        print("How many quarantine places do you want?")
        Qnumber = int(input())
        for i in range(Qnumber):
            print("Enter the coordinate row:")
            Qrow = int(input())
            while Qrow > row or Qrow == 0:
                print("index out of bound")
                print("Enter the coordinate row:")
                Qrow = int(input())
            print("Enter the coordinate column:")
            Qcolumn = int(input())
            while Qcolumn > column or Qcolumn == 0:
                print("index out of bound")
                print("Enter the coordinate column:")
                Qcolumn = int(input())
            Qpoint = (Qrow - 1, Qcolumn - 1)
            while Quarantine.__contains__(Qpoint):
                print("The place has been defined, please choose another place:")
                print("Enter the coordinate row:")
                Qrow = int(input())
                while Qrow > row or Qrow == 0:
                    print("index out of bound")
                    print("Enter the coordinate row:")
                    Qrow = int(input())
                print("Enter the coordinate column:")
                Qcolumn = int(input())
                while Qcolumn > column or Qcolumn == 0:
                    print("index out of bound")
                    print("Enter the coordinate column:")
                    Qcolumn = int(input())
                Qpoint = (Qrow - 1, Qcolumn - 1)
            Quarantine.append(Qpoint)
            EdgeQuarantine.append((Qrow, Qcolumn))
            i += 1
        print(Quarantine)

        print("How many vaccine places do you want?")
        Vnumber = int(input())
        for i in range(Vnumber):
            print("Enter the coordinate row:")
            Vrow = int(input())
            while Vrow > row or Vrow == 0:
                print("index out of bound")
                print("Enter the coordinate row:")
                Vrow = int(input())
            print("Enter the coordinate column:")
            Vcolumn = int(input())
            while Vcolumn > column or Vcolumn == 0:
                print("index out of bound")
                print("Enter the coordinate column:")
                Vcolumn = int(input())
            Vpoint = (Vrow - 1, Vcolumn - 1)
            while Quarantine.__contains__(Vpoint) or Vaccine.__contains__(Vpoint):
                print("The place has been defined, please choose another place:")
                print("Enter the coordinate row:")
                Vrow = int(input())
                while Vrow > row or Vrow == 0:
                    print("index out of bound")
                    print("Enter the coordinate row:")
                    Vrow = int(input())
                print("Enter the coordinate column:")
                Vcolumn = int(input())
                while Vcolumn > column or Vcolumn == 0:
                    print("index out of bound")
                    print("Enter the coordinate column:")
                    Vcolumn = int(input())
                Vpoint = (Vrow - 1, Vcolumn - 1)
            Vaccine.append(Vpoint)
            EdgeVaccine.append((Vrow, Vcolumn))
            i += 1
        print(Vaccine)

        print("How many playgrounds do you want?")
        Pnumber = int(input())
        for i in range(Pnumber):
            print("Enter the coordinate row:")
            Prow = int(input())
            while Prow >= row or Prow == 0:
                print("index out of bound")
                print("Enter the coordinate row:")
                Prow = int(input())
            print("Enter the coordinate column:")
            Pcolumn = int(input())
            while Pcolumn > column or Pcolumn == 0:
                print("index out of bound")
                print("Enter the coordinate column:")
                Pcolumn = int(input())
            Ppoint = (Prow - 1, Pcolumn - 1)
            while Quarantine.__contains__(Ppoint) or Vaccine.__contains__(Ppoint) or Playground.__contains__(Ppoint):
                print("The place has been defined, please choose another place:")
                print("Enter the coordinate row:")
                Prow = int(input())
                while Prow > row or Prow == 0:
                    print("index out of bound")
                    print("Enter the coordinate row:")
                    Prow = int(input())
                print("Enter the coordinate column:")
                Pcolumn = int(input())
                while Pcolumn > column or Pcolumn == 0:
                    print("index out of bound")
                    print("Enter the coordinate column:")
                    Pcolumn = int(input())
                Ppoint = (Prow - 1, Pcolumn - 1)
            Playground.append(Ppoint)
            EdgePlayground.append((Prow, Pcolumn))
            i += 1
        print(Playground)

        print("Enter the start point row:")
        sprow = float(input())
        while sprow >= row:
            print("index out of bound")
            print("Enter the start point row:")
            sprow = float(input())
        print("Enter the start point column:")
        spcolumn = float(input())
        while spcolumn >= column:
            print("index out of bound")
            print("Enter the start point column:")
            spcolumn = float(input())
        start_point = (sprow, spcolumn)
        sp = start_point
        print(sp)

        print("Enter the end point row:")
        eprow = float(input())
        while eprow >= row:
            print("index out of bound")
            print("Enter the end point row:")
            eprow = float(input())
        print("Enter the start point column:")
        epcolumn = float(input())
        while epcolumn >= column:
            print("index out of bound")
            print("Enter the end point column:")
            epcolumn = float(input())
        end_point = (eprow, epcolumn)
        ep = end_point
        print(ep)

        H = nx.grid_2d_graph(row, column)
        G = nx.grid_2d_graph(row + 1, column + 1)
        S = nx.Graph()
        E = nx.Graph()
        E.add_node(ep)
        S.add_node(sp)

        Spos = {}
        Epos = {}
        Gpos = {}
        Elabel = {}
        Slabel = {}

        for node in E:
            Elabel[node] = "EP"
            if sp == node:
                Elabel[node] = "EP/SP"

        for node in S:
            Slabel[node] = "SP"
            if ep == node:
                Slabel[node] = "EP/SP"

        for node in G:
            newrow = 0
            newcolumn = 0
            x = node[0]
            y = node[1]
            if not x == 0:
                newrow = x * 2
            if not y == 0:
                newcolumn = y * 2
            Gpos[node] = (newrow, newcolumn)
            # print(x, y)

        for node in S:
            newrow = 0
            newcolumn = 0
            x = node[0]
            y = node[1]
            if not x == 0:
                newrow = x * 2
            if not y == 0:
                newcolumn = y * 2
            Spos[node] = (newrow, newcolumn)

        for node in E:
            newrow = 0
            newcolumn = 0
            x = node[0]
            y = node[1]
            if not x == 0:
                newrow = x * 2
            if not y == 0:
                newcolumn = y * 2
            Epos[node] = (newrow, newcolumn)

        Hpos = {}

        for node in H:
            Hpos[node] = (node[0] * 2 + 1, node[1] * 2 + 1)

        Hlabels = {}

        Glabels = dict((((i, j), (i + 1 + (column + 1) * j)) for i, j in G.nodes()))

        color_map = []

        for node in H:
            if Quarantine.__contains__(node):
                color_map.append('lightblue')
                Hlabels[node] = "Q"
            elif Vaccine.__contains__(node):
                color_map.append('yellow')
                Hlabels[node] = "V"
            elif Playground.__contains__(node):
                color_map.append('red')
                Hlabels[node] = "P"
            else:
                color_map.append('pink')
                Hlabels[node] = ""

        # Edge
        Horiziontal = {}
        Vertical = {}

        #Horiziontal edge
        for i in range(row+1):
            for j in range(column+1):
                node = (i, j)
                rightnode = (i + 1, j)
                diognalnode = (i + 1, j + 1)
                if i == row:
                    break

                # if floor edges
                elif j == 0:
                    if EdgeVaccine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 0
                    elif EdgePlayground.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 3
                    else:
                        Horiziontal[(i, j), (i + 1, j)] = 1
                elif j == column:
                    if EdgeVaccine.__contains__(rightnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2
                    elif EdgeQuarantine.__contains__(rightnode):
                        Horiziontal[(i, j), (i + 1, j)] = 0
                    elif EdgePlayground.__contains__(rightnode):
                        Horiziontal[(i, j), (i + 1, j)] = 3
                    else:
                        Horiziontal[(i, j), (i + 1, j)] = 1
                # normal edges
                elif EdgeVaccine.__contains__(rightnode):
                    if EdgeVaccine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 1
                    elif EdgePlayground.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2.5
                    else:
                        Horiziontal[(i, j), (i + 1, j)] = 1.5
                elif EdgeQuarantine.__contains__(rightnode):
                    if EdgeVaccine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 1
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 0
                    elif EdgePlayground.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2
                    else:
                        Horiziontal[(i, j), (i + 1, j)] = 0.5
                elif EdgePlayground.__contains__(rightnode):
                    if EdgeVaccine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2.5
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2
                    elif EdgePlayground.__contains__(diognalnode):
                        Horiziontal[(i, j), (i + 1, j)] = 3
                    else:
                        Horiziontal[(i, j), (i + 1, j)] = 2

                elif EdgeQuarantine.__contains__(diognalnode):
                    Horiziontal[(i, j), (i + 1, j)] = 0.5
                elif EdgePlayground.__contains__(diognalnode):
                    Horiziontal[(i, j), (i + 1, j)] = 2
                elif EdgeVaccine.__contains__(diognalnode):
                    Horiziontal[(i, j), (i + 1, j)] = 1.5

                # if ceilling edges
                elif j == column:
                    if EdgeVaccine.__contains__(rightnode):
                        Horiziontal[(i, j), (i + 1, j)] = 2
                    elif EdgeQuarantine.__contains__(rightnode):
                        Horiziontal[(i, j), (i + 1, j)] = 0
                    elif EdgePlayground.__contains__(rightnode):
                        Horiziontal[(i, j), (i + 1, j)] = 3
                    else:
                        Horiziontal[(i, j), (i + 1, j)] = 1

                else:
                    Horiziontal[(i, j), (i + 1, j)] = 1

        # Vertical edge
        for i in range(row + 1):
            for j in range(column + 1):
                node = (i, j)
                upnode = (i, j + 1)
                diognalnode = (i + 1, j + 1)
                if j == column:
                    break

                # if left edges
                elif i == 0:
                    if EdgeVaccine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 2
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 0
                    elif EdgePlayground.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 3
                    else:
                        Vertical[(i, j), (i, j + 1)] = 1

                # if right edges
                elif i == row:
                    if EdgeVaccine.__contains__(upnode):
                        Vertical[(i, j), (i, j + 1)] = 2
                    elif EdgeQuarantine.__contains__(upnode):
                        Vertical[(i, j), (i, j + 1)] = 0
                    elif EdgePlayground.__contains__(upnode):
                        Vertical[(i, j), (i, j + 1)] = 3
                    else:
                        Vertical[(i, j), (i, j + 1)] = 1

                # normal edges
                elif EdgeVaccine.__contains__(upnode):
                    if EdgeVaccine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 2
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 1
                    elif EdgePlayground.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 2.5
                    else:
                        Vertical[(i, j), (i, j + 1)] = 1.5
                elif EdgeQuarantine.__contains__(upnode):
                    if EdgeVaccine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 1
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 0
                    elif EdgePlayground.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 2
                    else:
                        Vertical[(i, j), (i, j + 1)] = 0.5
                elif EdgePlayground.__contains__(upnode):
                    if EdgeVaccine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 2.5
                    elif EdgeQuarantine.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 2
                    elif EdgePlayground.__contains__(diognalnode):
                        Vertical[(i, j), (i, j + 1)] = 3
                    else:
                        Vertical[(i, j), (i, j + 1)] = 2

                elif EdgeQuarantine.__contains__(diognalnode):
                    Vertical[(i, j), (i, j + 1)] = 0.5
                elif EdgePlayground.__contains__(diognalnode):
                    Vertical[(i, j), (i, j + 1)] = 2
                elif EdgeVaccine.__contains__(diognalnode):
                    Vertical[(i, j), (i, j + 1)] = 1.5

                else:
                    Vertical[(i, j), (i, j + 1)] = 1

        plt.figure(figsize=[10, 10])
        nx.draw_networkx_nodes(H, pos=Hpos, node_size=800, node_shape='s', node_color=color_map)
        nx.draw_networkx_labels(H, pos=Hpos, labels=Hlabels, font_color="black")
        nx.draw_networkx_nodes(G, pos=Gpos, node_size=600, node_color='green')
        nx.draw_networkx_labels(G, pos=Gpos, labels=Glabels, font_color="black")
        nx.draw_networkx_edges(G, pos=Gpos)
        nx.draw_networkx_nodes(S, pos=Spos, node_size=1300, node_shape='*', node_color='black')
        nx.draw_networkx_labels(S, pos=Spos, labels=Slabel, font_color='white')
        nx.draw_networkx_nodes(E, pos=Epos, node_size=1300, node_shape='*', node_color='black')
        nx.draw_networkx_labels(E, pos=Epos, labels=Elabel, font_color='white')
        nx.draw_networkx_edge_labels(G, edge_labels=Horiziontal, pos=Gpos)
        nx.draw_networkx_edge_labels(G, edge_labels=Vertical, pos=Gpos)
        plt.show()
