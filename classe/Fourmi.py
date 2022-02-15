import arcade


class Fourmi(arcade.SpriteCircle):
    """
        -chaque fourmi a un etat
        -chaque fourmi a une list de noeud ou elle est passer
    """

    def __init__(self, position, circle_rad, node_color):
        super().__init__(circle_rad, node_color)

        self.center_x = position[0]
        self.center_y = position[1]
