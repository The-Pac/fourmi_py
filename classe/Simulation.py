import random

import arcade
from classe import Graph
from classe.Fourmi import Fourmi

# --- Constants ---
NODE_NBR = 7
# minim 2 pair
NODE_PAIR_NBR = 2

FOURMI_NBR = 5
FOURMI_SPEED = 1.5

NODE_CIRCLE_RADIUS = 15
FOURMI_CIRCLE_RADIUS = 5

NODE_COlOR = (0, 255, 0)
NODE_SUCRE_COlOR = (0, 0, 255)
FOURMI_COLOR = (255, 0, 0)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class Simulation(arcade.Window):
    """
        -Cree une list de bar && fourmi && node
        -Ajoute une list de node && pair au jeu
        -Ajoute une list de fourmi au jeu
        -Ajoute un sucre a un noeud aleatoire
        -Defini les bar par rapport au paire
    """

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Simulation")

        self.bar = list(range(0, NODE_NBR * NODE_PAIR_NBR))

        self.fourmi_list = arcade.SpriteList()
        self.node_list = arcade.SpriteList()

        graph = Graph.Graph()
        self.list_node, self.list_pair = graph.create_graph(NODE_NBR, NODE_PAIR_NBR, SCREEN_WIDTH - 50,
                                                            SCREEN_HEIGHT - 50,
                                                            NODE_CIRCLE_RADIUS,
                                                            NODE_COlOR)

        for i in range(0, FOURMI_NBR):
            position = (self.list_pair[0].node1.center_x, self.list_pair[0].node1.center_y)
            fourmi = Fourmi(position, self.list_pair[0].node1, FOURMI_SPEED)
            self.fourmi_list.append(fourmi)

        rand_node = self.list_node[random.randint(1, len(self.list_node) - 1)]
        rand_node.set_sucre(rand_node.position, True, NODE_SUCRE_COlOR)

        for node in self.list_node:
            self.node_list.append(node)

        for index, pair in enumerate(self.list_pair):
            self.bar[index] = [pair.node1.center_x, pair.node1.center_y, pair.node2.center_x, pair.node2.center_y]

    """
        update chaque list
    """

    def update(self, delta_time):
        self.fourmi_list.update()

    """
        -Affiche chaque bar
        -Affiche un text sur chaque noeud
        -dessine les list fourmi / node
    """

    def on_draw(self):
        self.clear()
        arcade.start_render()
        self.node_list.draw()
        self.fourmi_list.draw()

        for bar in self.bar:
            color = arcade.color.WHITE
            arcade.draw_line(bar[0], bar[1],
                             bar[2], bar[3], color, 1)

        for node in self.list_node:
            arcade.draw_text(str(node.name), node.center_x - 7, node.center_y - 7, arcade.color.BLACK, bold=True)
