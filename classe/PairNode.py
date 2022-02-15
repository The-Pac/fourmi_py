import random

from classe.Node import Node


class PairNode:

    def __init__(self, node1, node2, taux_phero, screen_w, screen_h, circle_rad, color1, color2):
        position = (random.randrange(screen_w), random.randrange(screen_h))
        self.node1 = Node(position, circle_rad, color1, node1)
        self.node2 = Node(position, circle_rad, color2, node2)
        self.taux_phero = taux_phero

