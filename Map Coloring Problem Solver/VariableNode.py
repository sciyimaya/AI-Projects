# variable node has name, domain, number of colors, neighbors, and value
class VariableNode:
    def __init__(self, name, num_colors):
        self.name = name
        self.domain = self.construct_domain(num_colors)
        self.neighbors = []
        self.value = -1

    def add_neighbor(self, new_neighbor_node):
        self.neighbors.append(new_neighbor_node)

    def construct_domain(self, num_colors):
        domain = []
        for i in range(0, num_colors):
            domain.append(i)
        return domain
