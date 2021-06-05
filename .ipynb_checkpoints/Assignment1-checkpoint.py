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

        # Enter the values
        print("Enter the row:")
        row = int(input())
        print("Enter the column:")
        column = int(input())

        G = nx.grid_2d_graph(column, row)

        print("How many quarantine places do you want?")
        Qnumber = int(input())
        for i in range(Qnumber):
            print("Enter the coordinate row:")
            Qrow = int(input())
            while not Qrow <= row:
                print("index out of bound")
                print("Enter the coordinate row:")
                Qrow = int(input())
            print("Enter the coordinate column:")
            Qcolumn = int(input())
            while not Qcolumn <= column:
                print("index out of bound")
                print("Enter the coordinate column:")
                Qcolumn = int(input())
            Qpoint = [Qrow, Qcolumn]
            while Quarantine.__contains__(Qpoint):
                print("The place has been defined, please choose another place:")
                print("Enter the coordinate row:")
                Qrow = int(input())
                print("Enter the coordinate column:")
                Qcolumn = int(input())
                Qpoint = [Qrow, Qcolumn]
            Quarantine.append(Qpoint)
            i += 1
        print(Quarantine)

        print("How many vaccine places do you want?")
        Vnumber = int(input())
        for i in range(Vnumber):
            print("Enter the coordinate row:")
            Vrow = int(input())
            while Vrow > row:
                print("index out of bound")
                print("Enter the coordinate row:")
                Vrow = int(input())
            print("Enter the coordinate column:")
            Vcolumn = int(input())
            while Vcolumn > column:
                print("index out of bound")
                print("Enter the coordinate column:")
                Vcolumn = int(input())
            Vpoint = [Vrow, Vcolumn]
            while Quarantine.__contains__(Vpoint) or Vaccine.__contains__(Vpoint):
                print("The place has been defined, please choose another place:")
                print("Enter the coordinate row:")
                Vrow = int(input())
                print("Enter the coordinate column:")
                Vcolumn = int(input())
                Vpoint = [Vrow, Vcolumn]
            Vaccine.append(Vpoint)
            i += 1
        print(Vaccine)

        print("How many playgrounds do you want?")
        Pnumber = int(input())
        for i in range(Pnumber):
            print("Enter the coordinate row:")
            Prow = int(input())
            while Prow > row:
                print("index out of bound")
                print("Enter the coordinate row:")
                Prow = int(input())
            print("Enter the coordinate column:")
            Pcolumn = int(input())
            while Pcolumn > column:
                print("index out of bound")
                print("Enter the coordinate column:")
                Pcolumn = int(input())
            Ppoint = [Prow, Pcolumn]
            while Quarantine.__contains__(Ppoint) or Vaccine.__contains__(Ppoint) or Playground.__contains__(Ppoint):
                print("The place has been defined, please choose another place:")
                print("Enter the coordinate row:")
                Prow = int(input())
                print("Enter the coordinate column:")
                Pcolumn = int(input())
                Ppoint = [Prow, Pcolumn]
            Playground.append(Ppoint)
            i += 1
        print(Playground)

        G.add_nodes_from(Vaccine)




        pos = {(x, y): (y, -x) for x, y in G.nodes()}
        nx.draw(G, pos=pos,
                node_color="black",
                with_labels=True,
                node_size=700,
                font_color="white",
                )

        for i in range(len(Vaccine)):
            nx.draw(G, node_list=Vaccine, node_color="r")
        plt.show()
