from typing import Any


class PriorityQueue:
    def __init__(self, dict):
        self.S = dict

    def __str__(self):
        return str(self.S)

    def insert(self, v, priority):
        self.S[v] = priority

    def minimum(self):
        if not self.S:
            return None
        mink = min(self.S, key=self.S.get)
        return (mink, self.S[mink])

    def extract_min(self):
        if not self.S:
            return None
        mink, min_val = self.minimum()
        del self.S[mink]
        return (mink, min_val)

    def decrease_distance(self, v, k):
        if v in self.S and self.S[v] > k:
            self.S[v] = k
            return True
        return False


class Vertex:
    data: Any

    def __init__(self, data=None):
        self.data = data

    def __str__(self):
        return self.data


class Edge:
    vertices: set[Vertex]
    weight: float

    def __init__(self, vertex1=None, vertex2=None, weight=1.0):
        if (vertex1 and vertex2) is not None:
            self.vertices = {vertex1, vertex2}
        else:
            self.vertices = set()

    def __str__(self):
        if self.vertices is not None:
            return ' - '.join(str(self.vertices))


class Graph:
    def __init__(self):
        self.vertices = []
        self.adj = {}

    def add_vertex(self, v):
        if v not in self.vertices:
            self.vertices.append(v)
            self.adj[v] = {}

    def add_edge(self, u, v, weight):

        if u not in self.adj: self.add_vertex(u)
        if v not in self.adj: self.add_vertex(v)
        self.adj[u][v] = weight
        self.adj[v][u] = weight

    def weight(self, vertex1, vertex2):

        if vertex1 in self.adj and vertex2 in self.adj[vertex1]:
            return self.adj[vertex1][vertex2]
        return float('inf')

    def from_adjacency_matrix(self, matrix):

        self.vertices = []
        self.adj = {}
        rows = len(matrix)
        for i in range(rows):
            self.add_vertex(f"v{i}")

        for i in range(rows):
            for j in range(rows):
                if matrix[i][j] != 0:
                    u = self.vertices[i]
                    v = self.vertices[j]
                    self.adj[u][v] = matrix[i][j]

    def dijkstra(self, vertex0):
        d = {}
        for v in self.vertices:
            d[v] = [[], float('inf')]
        d[vertex0] = [[vertex0], 0]
        pq_dict = {v: d[v][1] for v in self.vertices}
        queue = PriorityQueue(pq_dict)
        while queue.S:
            u_tuple = queue.extract_min()
            if u_tuple is None:
                break
            u, dist_u = u_tuple
            if dist_u == float('inf'):
                break
            neighbors = self.adj.get(u, {})
            for v, w in neighbors.items():
                if v in queue.S:
                    alt = dist_u + self.weight(u, v)
                    if alt < d[v][1]:
                        d[v][1] = alt
                        d[v][0] = d[u][0] + [v]
                        queue.decrease_distance(v, alt)
        return d


queue = PriorityQueue({'a': 0, 'b': 2, 'c': 3, 'd': 0})
assert str(queue) == "{'a': 0, 'b': 2, 'c': 3, 'd': 0}"
queue.insert('e', 0.5)
assert str(queue) == "{'a': 0, 'b': 2, 'c': 3, 'd': 0, 'e': 0.5}"
assert queue.minimum() == ('a', 0)
assert str(queue) == "{'a': 0, 'b': 2, 'c': 3, 'd': 0, 'e': 0.5}"
assert queue.extract_min() == ('a', 0)
assert str(queue) == "{'b': 2, 'c': 3, 'd': 0, 'e': 0.5}"
queue.decrease_distance('b', 1)
assert str(queue) == "{'b': 1, 'c': 3, 'd': 0, 'e': 0.5}"
queue.decrease_distance('d', 5)
assert str(queue) == "{'b': 1, 'c': 3, 'd': 0, 'e': 0.5}"
G = Graph()
for i in range(6): G.add_vertex(f"v{i}")
G.add_edge(G.vertices[0], G.vertices[1], 1)
G.add_edge(G.vertices[0], G.vertices[3], 5)
G.add_edge(G.vertices[0], G.vertices[5], 3)
G.add_edge(G.vertices[1], G.vertices[2], 2)
G.add_edge(G.vertices[1], G.vertices[4], 4)
G.add_edge(G.vertices[2], G.vertices[4], 4)
G.add_edge(G.vertices[3], G.vertices[5], 2)
G.add_edge(G.vertices[3], G.vertices[4], 1)
G.add_edge(G.vertices[4], G.vertices[5], 3)
print()
d = G.dijkstra(G.vertices[2])
for x in d:
    print(f"{x}:", end=" ")
    for y in d[x][0]:
        print(f"{y},", end=" ")
    print(d[x][1])
G = Graph()
G.from_adjacency_matrix(
    [[0, 7, 9, 0, 0, 14], [7, 0, 10, 15, 0, 0], [9, 10, 0, 11, 0, 2], [0, 15, 11, 0, 6, 0], [0, 0, 0, 6, 0, 9],
     [14, 0, 2, 0, 9, 0]])
d = G.dijkstra(G.vertices[0])
print()
print()
print()
print()
print()
for z in d:
    print(f"{z}:", end=" ")
    for y in d[z][0]:
        print(f"{y},", end=" ")
    print(d[z][1])
