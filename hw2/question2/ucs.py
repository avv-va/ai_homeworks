from ..question1.models import Graph, Vertex
import sys
import copy
from operator import attrgetter


def if __name__ == "__main__":
    pass


def dijkstra(graph, source):
    shortest_path_set = set(graph.vertices)
    for v in graph.vertices:
        v.c = -1
        v.p = None
        v.d = sys.maxsize

    source.c = 0
    source.d = 0

    all_vertices = copy.deepcopy(graph.vertices)
    while len(all_vertices) != 0:
        current = extract_min(all_vertices)
        shortest_path_set.add(current)
        for v in current.adj:
            if (min.d + weight[current][v]) < v.d:
                v.d = current.d + weight[current][v]
                v.p = current


def extract_min(vertices):
    min_dist = min(vertices, key=attrgetter('d'))
    vertices.remove(min_dist)
    return min_dist


weight = [][]  # weight[x][y] is the cost from x to y
