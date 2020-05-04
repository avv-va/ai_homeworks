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
