import math
import random

import arcade


class Fourmi(arcade.Sprite):
    """
        -definir la position init
        -cree une list des noeud parcouru
        -defini le noeud actuel
        -ajoute le noeud actuel a la road
    """

    def __init__(self, position, node, speed):
        super().__init__(filename="C:/Users/pac/PycharmProjects/fourmi_py/img/ant.png", center_x=position[0],
                         center_y=position[1], scale=0.2)
        self.center_x = position[0]
        self.center_y = position[1]
        self.frame_count = 0
        self.road = list()
        self.road.append(node)
        self.actual_node = node
        self.speed = speed
        self.sucre_found = False

    """
        Update chaque 60 frame la position de la fourmi
    """

    def update(self):
        self.frame_count += 1
        # chaque 60 frame update la pos
        if self.frame_count >= 60:
            self.frame_count = 0
            # si le noeud actuel a du sucre alors retourner au depart et placer des phero sur les pair
            if self.actual_node.sucre:
                self.sucre_found = True
                if len(self.road) > 0:
                    self.road.pop()
                    last_node = self.road.pop()
                    self.center_x = last_node.center_x
                    self.center_y = last_node.center_y
                    self.actual_node = last_node
                else:
                    self.road = self.actual_node
            else:
                # si le sucre est trouver chercher parmis toutes les noeuds la paire avec
                # le plus de phero tout en faisant un aletoire entre ce noeuds et les autres
                if self.sucre_found:
                    pair_H_taux_phero = 0
                    for pair in self.actual_node.list_pair:
                        if pair_H_taux_phero == 0:
                            pair_H_taux_phero = pair
                        else:
                            if pair.taux_phero >= pair_H_taux_phero.taux_phero:
                                pair_H_taux_phero = pair.taux_phero

                    self.center_x = pair_H_taux_phero.node2.center_x + self.speed
                    self.center_y = pair_H_taux_phero.node2.center_y + self.speed

                    self.actual_node = pair_H_taux_phero.node2
                    self.road.append(pair_H_taux_phero.node2)

                else:
                    # si la le noeud actuel n'a pas qu'une paire
                    if len(self.actual_node.list_pair) > 1:
                        # recuperer un noeud random qui n'est pas egal au dernier noeuds explorer
                        rand_node = random.choice(self.actual_node.list_pair)
                        if len(self.road) > 1:
                            while self.road[len(self.road) - 2] == rand_node:
                                rand_node = random.choice(self.actual_node.list_pair)
                    # si le noeud n'a qu'une paire alors la prendre
                    else:
                        rand_node = self.actual_node.list_pair[0]

                    self.center_x = rand_node.center_x + self.speed
                    self.center_y = rand_node.center_y + self.speed

                    self.actual_node = rand_node
                    self.road.append(rand_node)

    """
        Ajouter un noeud a la list de noeud pour retrouver son chemin
    """

    def add_road(self, road):
        self.road.append(road)

    """
        defini le noeud actuel
    """

    def set_actual_node(self, node):
        self.road.append(node)
        self.actual_node = node
