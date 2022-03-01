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
        super().__init__(filename="C:/Users/Pac/PycharmProjects/fourmi_py/img/ant.png", center_x=position[0],
                         center_y=position[1], scale=0.2)
        self.center_x = position[0]
        self.center_y = position[1]

        self.frame_count = 0
        self.road = list()
        self.road.append(node)
        self.actual_node = node

        self.speed = speed

        self.direction_x = None
        self.direction_y = None

        self.on_move = False
        self.direction_node = None
        self.searching = True

    def update(self):
        self.frame_count += 1
        if not self.on_move:
            # si le noeud actuel a du sucre alors retourner au depart et placer des phero sur les pair
            if self.actual_node.sucre:
                self.searching = False
                self.road.pop()
                last_node = self.road.pop()
                self.move(last_node)
            else:
                # si le sucre est trouver chercher parmis toutes les noeuds la paire avec
                # le plus de phero tout en faisant un aletoire entre ce noeuds et les autres
                if self.searching:
                    # si le noeud actuel n'a pas qu'une paire
                    if len(self.actual_node.list_pair) > 1:
                        # recuperer un noeud random qui n'est pas egal au dernier noeuds explorer
                        list_pair_taux = list()
                        for pair in self.actual_node.list_pair:
                            list_pair_taux.append(pair.taux_phero)

                        rand_pair = random.choices(self.actual_node.list_pair, list_pair_taux)
                        rand_node = rand_pair[0].node2

                    # si le noeud n'a qu'une paire alors la prendre
                    else:
                        rand_node = self.actual_node.list_pair.node1

                    self.move(rand_node)
                else:
                    if len(self.road) != 0:
                        last_node = self.road.pop()
                        for pair in last_node.list_pair:
                            if pair.node1 == last_node or pair.node2 == last_node:
                                pair.set_taux_phero(40)
                                break
                        self.move(last_node)
                    else:
                        self.road.append(self.actual_node)
                        self.searching = True

        else:

            if math.sqrt((int(self.center_x) - int(self.direction_x)) ** 2 + (
                    int(self.center_y) - int(self.direction_y)) ** 2) <= 1:
                self.on_move = False
                self.change_x = 0
                self.change_y = 0
                self.actual_node = self.direction_node
                if self.searching:
                    self.road.append(self.direction_node)
            else:
                self.center_x += self.change_x
                self.center_y += self.change_y

    def move(self, node):
        self.on_move = True
        self.direction_node = node
        self.direction_x = int(node.center_x)
        self.direction_y = int(node.center_y)

        diff_x = self.direction_x - self.center_x
        diff_y = self.direction_y - self.center_y

        angle = math.atan2(diff_y, diff_x)

        self.angle = math.degrees(angle) - 18

        self.change_x = math.cos(angle) * self.speed
        self.change_y = math.sin(angle) * self.speed

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
