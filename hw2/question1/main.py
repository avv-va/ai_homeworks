from models import Vertex, Graph
import sys

if __name__ == "__main__":
    pass


def bfs(graph, sourceV):
    for v in graph.vertices:
        v.c = -1
        v.p = None
        v.d = sys.maxsize

    sourceV.c = 0
    sourceV.d = 0

    queue = []
    queue.append(sourceV)

    while (len(queue) != 0):
        current = queue.pop(0)
        current.c = 1

        print('Node: {}'.format(current.id))

        for v in current.adj:
            if v.c == -1:
                v.c = 0
                v.p = current
                v.d = current.d + 1
                queue.add(v)


def dfs(graph):
    for v in range graph.vertices:
        for v2 in graph.vertices:
            v2.c = -1
            v2.p = None
        dfsvisit(graph, v)


def dfsvisit(graph, source):
    source.c = 0
    for v in source.adj:
        if v.c == -1:
            v.p = source
            dfsvisit(graph, v)
    source.c = 1
