class Graph:
    def __init__(self, vertices):
        self.vertices = vertices


class Vertex:
    def __init__(self, id):
        self.id = id
        self.p = None
        self.c = -1
        self.d = sys.maxsize
        self.adj = list()
