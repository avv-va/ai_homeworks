from ..question1.models import Graph, Node
import sys
from operator import attrgetter


def if __name__ == "__main__":
    pass


def find_second_best_shortest_path(graph, source, all_nodes, shortest_path):
    min_cost = sys.maxsize
    second_shortest_path = []
    for node in shortest_path:
        for node_adj in node.adj:
            node.adj.remove(node_adj)
            cost, shortest_path = dijkstra(source, all_nodes)
            if cost < min_cost:
                min_cost = cost
                second_shortest_path = shortest_path
            node.adj.add(node_adj)

    return second_shortest_path


def dijkstra(source, dest, all_nodes):
    shortest_path_set = set()
    total_cost = 0
    for v in graph.nodes:
        v.c = -1
        v.p = None
        v.d = sys.maxsize

    source.c = 0
    source.d = 0

    while len(all_nodes) != 0:
        current = extract_min(all_nodes)
        total_cost += current.d
        shortest_path_set.add(current)

        if dest == current:
            break

        for v in current.adj:
            if (min.d + weight[current][v]) < v.d:
                v.d = current.d + weight[current][v]
                v.p = current
    return total_cost, shortest_path_set


def extract_min(nodes):
    min_dist = min(nodes, key=attrgetter('d'))
    nodes.remove(min_dist)
    return min_dist


weight = [][]  # weight[x][y] is the cost for edge x -> y
