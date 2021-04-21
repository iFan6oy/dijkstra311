# CSC311
# HW3 - Dijkstra's Algorithm
# Group #... what group number are we?

from typing import List
import copy


# this is a class to define links between nodes (edges & costs) in the graph
class Link:
    def __init__(self, node1, node2, cost):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost

    def __eq__(self, other):
        # TODO: might want some type checking here for more advanced compares
        if self.node1 == other.node1 and self.node2 == other.node2:
            return True
        elif self.node2 == other.node1 and self.node1 == other.node2:
            return True
        else:
            return False


def get_cost(link: Link) -> int:
    return link.cost


def same_link(link1: Link, link2: Link) -> bool:
    if link1.node1 == link2.node1 and link1.node2 == link2.node2:
        return True
    elif link1.node2 == link2.node1 and link1.node1 == link2.node2:
        return True
    else:
        return False


def is_edge(node1: int, node2: int, graph_list: List) -> bool:
    for g in graph_list:
        if g.node1 == node1 and g.node2 == node2:
            return True
        else:
            return False


def edge_cost(node1: int, node2: int, graph_list: List) -> int:
    for g in graph_list:
        if g.node1 == node1 and g.node2 == node2:
            return g.cost
        else:
            return -1


def dijkstra(start_node, end_node, graph_list):
    # the graph is passed in via a List containing Links
    # a Link contains a start, end, and cost

    # current_cost is our current running cost, current node is start_node
    current_cost = 9999
    current_node = start_node
    total_cost = 0

    # we can remove our own node from the list since looping back can't help
    # also, mark all destinations "infinity" (-1) in unvisited graph
    # we can use -1 here since i don't think dijkstras works with negative values on edges
    # start_link = Link(start_node, start_node, 0)
    # for x in graph_list:
    #     # if same_link(x, x) or same_link(x, homelink):
    #     if x == x or x == start_link:
    #         graph_list.remove(x)
    #     if x.node1 == current_node:
    #         graph_list.remove(x)
    #     if x.node2 == current_node:
    #         graph_list.remove(x)

    # copy reduced graph to new structure named 'unvisited'
    unvisited = copy.deepcopy(graph_list)

    # mark all destinations "infinity" (-1) in unvisited graph
    # we can use -1 here since i don't think dijkstras works with negative
    # cost values on edges
    for u in unvisited:
        u.cost = -1

    # make empty visited list
    visited = []

    # visit nodes
    for u in unvisited:
        # check to see if we've visited this before
        if u not in visited:
            # check for adjacency
            if u.node1 == current_node:
                pass
                # is node 2 end node?
                # TODO: fix this crap

            # loop through graph_list to get cost, assign to unvisited distance
            for g in graph_list:
                # if u.node1 == g.node1 and u.node2 == g.node2:
                # if same_link(u, g):
                if u == g:
                    # compare cost to lowest current?
                    if g.cost < current_cost:
                        current_cost = g.cost
                        u.cost = current_cost
                        total_cost = u.cost + current_cost

                        # append this visit + cost
                        visited.append(u)
                    else:
                        visited.append(u)
            #

        # remove current unvisited(u) (since we visited it)
        # unvisited.remove(u)

    for v in visited:
        print(v.node1, v.node2, v.cost)

        # print(graph_list(x.distance))  #this is broken, need to ref original graph_list for distances

    # debug print
    # for x in unvisited:
    #    print(x.node1, x.node2, x.distance)


def main():
    print('CSC311 - Group Project - Dijkstra\'s Algorithm\n')

    # we need to represent the provided graph
    # we will use the Link class from above to do this and capture them all in a list
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
        Link(2, 8, 2),
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

    # take input for start point, set inputs to invalid points
    starting_node = -1
    ending_node = -1

    # get starting_node from user
    while not (0 <= starting_node <= 8):
        prompt_text = "Please enter a starting node: "
        starting_node = int(input(prompt_text))

    # get ending_node from user
    while not (0 <= ending_node <= 8):
        prompt_text = "Please enter an ending node: "
        ending_node = int(input(prompt_text))

    # debug print to make sure we got them
    print("starting: ", starting_node)
    print("ending: ", ending_node)

    # get result from djik
    result = dijkstra(starting_node, ending_node, graph_list)


# Init main function
if __name__ == '__main__':
    main()
