class PairNode:

    def __init__(self, node1, node2, taux_phero):
        self.node1 = node1
        self.node2 = node2
        self.taux_phero = taux_phero

    def set_taux_phero(self, taux):
        self.taux_phero = taux
