import random

import arcade

from classe import Graph
from classe.Fourmi import Fourmi

# --- Constants ---
NODE_NBR = 10
NODE_PAIR_NBR = 2

FOURMI_NBR = 100
SPEED = 2

NODE_CIRCLE_RADIUS = 10
FOURMI_CIRCLE_RADIUS = 5

NODE_COlOR = (0, 255, 0)
NODE_SUCRE_COlOR = (0, 0, 255)
FOURMI_COLOR = (255, 0, 0)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Simulation(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Simulation")

        self.bar = list(range(0, (NODE_NBR - 1) * NODE_PAIR_NBR))

        self.fourmi_list = arcade.SpriteList()
        self.node_list = arcade.SpriteList()

        graph = Graph.Graph()
        self.list_node, self.list_pair = graph.create_graph(NODE_NBR - 1, NODE_PAIR_NBR, SCREEN_WIDTH - 50,
                                                            SCREEN_HEIGHT - 50,
                                                            NODE_CIRCLE_RADIUS,
                                                            NODE_COlOR)

        rand_node = random.choice(self.list_node)
        rand_node.set_sucre(rand_node.position, True, NODE_SUCRE_COlOR)

        for node in self.list_node:
            self.node_list.append(node)

        for index, pair in enumerate(self.list_pair):
            self.bar[index] = [pair.node1.center_x, pair.node1.center_y, pair.node2.center_x, pair.node2.center_y]

        for i in range(0, FOURMI_NBR):
            position = (self.list_pair[0].node1.center_x, self.list_pair[0].node1.center_y)
            fourmi = Fourmi(position, FOURMI_CIRCLE_RADIUS, FOURMI_COLOR)
            self.fourmi_list.append(fourmi)

    def update(self, delta_time):
        self.node_list.update()
        self.fourmi_list.update()

    def on_draw(self):
        arcade.start_render()
        self.node_list.draw()
        self.fourmi_list.draw()

        for bar in self.bar:
            color = arcade.color.WHITE
            arcade.draw_line(bar[0], bar[1],
                             bar[2], bar[3], color, 1)

        for node in self.list_node:
            arcade.draw_text(str(node.name), node.center_x - 5, node.center_y - 5, arcade.color.BLACK, bold=True)
