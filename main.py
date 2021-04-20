# CSC311
# HW3 - Dijkstra's Algorithm
# Group #... what group number are we?

# this is a class to define nodes in the graph
class Link:
    def __init__(self, start_node, end_node, edge_cost):
        self.node1 = start_node
        self.node2 = end_node
        self.distance = edge_cost


def main():
    print('CSC311 - Group Project - Dijkstra\'s Algorithm\n')

    # we need to represent the provided graph
    # we will use the Link class from above to do this
    # and capture them all in a list
    # (start_node, end_node, edge_cost)
    graph_list = [
        Link(0, 1, 4),
        Link(0, 7, 8),
        Link(1, 0, 4),
        Link(1, 2, 8),
        Link(1, 7, 11),
        Link(2, 1, 8),
        Link(2, 3, 7),
        Link(2, 5, 7),
        Link(3, 2, 7),
        Link(3, 4, 9),
        Link(3, 5, 14),
        Link(4, 3, 9),
        Link(4, 5, 10),
        Link(5, 2, 4),
        Link(5, 3, 14),
        Link(5, 4, 10),
        Link(5, 6, 2),
        Link(6, 5, 2),
        Link(6, 7, 1),
        Link(6, 8, 6),
        Link(7, 0, 8),
        Link(7, 1, 11),
        Link(7, 6, 1),
        Link(7, 8, 7),
        Link(8, 2, 2),
        Link(8, 6, 6),
        Link(8, 7, 7),
        ]


# Init main
if __name__ == '__main__':
    main()
