import random as rand

from classe import PairNode


class Graph:

    def __init__(self):

        pass
    """
    Cree un graph avec des pairs de node au hazard dans une litst ou chacune a un taux de 0
    """

    def create_graph(self, node_nbr, screen_w, screen_h, circle_rad, color):
        abc = list(range(0, node_nbr))
        graph = list(range(0, node_nbr))
        start = False

        for index in range(0, len(graph)):
            # create random node1 number
            node1 = rand.randint(0, len(abc) - 1)
            node2 = rand.randint(0, len(abc) - 1)

            # check et faire tant que les deux nodes sont egal (eviter les doublons)
            while node1 == node2:
                node1 = rand.randint(0, len(abc) - 1)
                node2 = rand.randint(0, len(abc) - 1)

            # si le graph viens d'etre init et qu'il contient attr node1 || node2
            if start:
                graph[index] = PairNode.PairNode(abc[node1], abc[node2], 0, screen_w, screen_h, circle_rad,
                                                 color, color)
            else:
                graph[index] = PairNode.PairNode(abc[node1], abc[node2], 0, screen_w, screen_h, circle_rad,
                                                 color, color)
                start = True

        return graph
