import random
import random as rand

from classe import PairNode
from classe.Node import Node


class Graph:

    def __init__(self):

        pass

    """
    Cree un graph avec des pairs de node au hazard dans une litst ou chacune a un taux de 0
    """

    def create_graph(self, node_nbr, node_pair_nbr, screen_w, screen_h, circle_rad, color):
        list_node = list(range(0, node_nbr))
        list_pair = list(range(0, node_nbr * node_pair_nbr))

        for i in range(len(list_node)):
            position = (random.randrange(50, screen_w), random.randrange(50, screen_h))
            list_node[i] = Node(position, circle_rad, color, i)

        for i in range(len(list_pair)):
            for j in range(len(list_node)):
                rand_node = rand.choice(list_node)
                if list_node[j] != rand_node:
                    list_pair[i] = PairNode.PairNode(list_node[j], rand_node, 0)
                else:
                    while list_node[j] == rand_node:
                        rand_node = rand.choice(list_node)

                    list_pair[i] = PairNode.PairNode(list_node[j], rand_node, 0)

        return list_node, list_pair
