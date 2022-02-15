import random

import arcade

from classe import Graph
from classe.Fourmi import Fourmi

# --- Constants ---
NODE_NBR = 10
FOURMI_NBR = 100
SPEED = 2

NODE_CIRCLE_RADIUS = 10
FOURMI_CIRCLE_RADIUS = 5

NODE_COlOR = (0, 255, 0)
NODE_SUCRE_COlOR = (0, 255, 0)
FOURMI_COLOR = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Simulation(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Simulation")

        self.bar_n1 = list(range(0, NODE_NBR - 1))
        self.bar_n2 = list(range(0, NODE_NBR - 1))

        self.fourmi_list = arcade.SpriteList()
        self.node_list = arcade.SpriteList()

        graph = Graph.Graph()
        self.real_graph = graph.create_graph(NODE_NBR - 1, SCREEN_WIDTH + 20, SCREEN_HEIGHT - 20, NODE_CIRCLE_RADIUS,
                                             NODE_COlOR)
        self.real_graph[random.randint(0, len(self.real_graph) - 1)].node1.set_sucre(True, NODE_SUCRE_COlOR)

        for index, pair_node in enumerate(self.real_graph):
            self.node_list.append(pair_node.node1)
            self.node_list.append(pair_node.node2)

            bar_node1 = [pair_node.node1.center_x, pair_node.node1.center_y]
            bar_node2 = [pair_node.node2.center_x, pair_node.node2.center_y]

            self.bar_n1[index] = bar_node1
            self.bar_n2[index] = bar_node2

        for i in range(0, FOURMI_NBR):
            position = (self.real_graph[0].node1.center_x, self.real_graph[0].node1.center_y)
            fourmi = Fourmi(position, FOURMI_CIRCLE_RADIUS, FOURMI_COLOR)
            self.fourmi_list.append(fourmi)

    def update(self, delta_time):
        self.node_list.update()

    def on_draw(self):
        arcade.start_render()
        self.node_list.draw()
        self.fourmi_list.draw()

        for bar_1 in self.bar_n1:
            for bar_2 in self.bar_n2:
                color = arcade.color.WHITE
                arcade.draw_line(bar_1[0], bar_1[1],
                                 bar_2[0], bar_2[1], color, 1)
