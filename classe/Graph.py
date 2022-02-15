import random
import random as rand
from math import pi, cos, sin

from classe import PairNode
from classe.Node import Node


class Graph:

    def __init__(self):

        pass

    """
        Cree des pairs de node au hazard dans une list ou chaque paire a un taux de 0
        return la list de noeud , la list de paire
    """

    def point(self, h, k, r):
        theta = random.random() * 2 * pi
        return h + cos(theta) * r, k + sin(theta) * r

    def create_graph(self, node_nbr, node_pair_nbr, screen_w, screen_h, circle_rad, color):
        list_node = list(range(0, node_nbr))
        list_pair = list()

        for i in range(len(list_node)):
            random_point = self.point((screen_w / 2), (screen_h / 2), (screen_h / 2) - 50)
            position = (random_point[0], random_point[1])
            # position = (random.randrange(50, screen_w), random.randrange(50, screen_h))
            list_node[i] = Node(position, circle_rad, color, i)

        for j in range(len(list_node)):
            for i in range(node_pair_nbr):
                rand_node = rand.choice(list_node)
                if list_node[j] != rand_node:
                    list_node[j].set_pair(rand_node)
                    list_pair.append(PairNode.PairNode(list_node[j], rand_node, 0))
                else:
                    while list_node[j] == rand_node:
                        rand_node = rand.choice(list_node)
                    list_node[j].set_pair(rand_node)
                    list_pair.append(PairNode.PairNode(list_node[j], rand_node, 0))

        return list_node, list_pair
