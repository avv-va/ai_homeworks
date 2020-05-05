class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


class Node:
    def __init__(self, id):
        self.id = id
        self.p = None
        self.c = -1
        self.d = sys.maxsize
        self.adj = list()

class Edge:
    def __init__(self, a, b):
        self.a = a
        self.b = b