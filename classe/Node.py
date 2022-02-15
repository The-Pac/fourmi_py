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
        self.sucre = False
        self.name = name

    def set_sucre(self, sucre,node_color):
        super().__init__(10, node_color)
        self.sucre = sucre