import arcade


class Node(arcade.SpriteCircle):
    """
    Chaque noeud contient un nombre random de de pairs
    un seul noeud contient un sucre
    """

    def __init__(self, position, circle_rad, node_color, name):
        super().__init__(circle_rad, node_color)

        self.center_x = position[0]
        self.center_y = position[1]
        self.name = name
        self.sucre = False
        self.list_pair = list()

    def set_sucre(self, position, sucre, node_color):
        super().__init__(15, node_color)
        self.center_x = position[0]
        self.center_y = position[1]
        self.sucre = sucre

    def set_pair(self, pair):
        self.list_pair.append(pair)
