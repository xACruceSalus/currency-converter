from collections import namedtuple


inf = float('inf')
Edge = namedtuple('Edge', 'start, end, cost')

class Graph():
    def __init__(self, edges):
        self.edges = edges2 = [Edge(*edge) for edge in edges]
        self.vertices = set(sum(([e.start, e.end] for e in edges2), []))

    def dijkstra(self, source, dest):
        assert source in self.vertices
        dist = {vertex: inf for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        dist[source] = 0
        q = self.vertices.copy()
        neighbours = {vertex: set() for vertex in self.vertices}
        for start, end, cost in self.edges:
            neighbours[start].add((end, cost))

        while q:
            u = min(q, key=lambda vertex: dist[vertex])
            q.remove(u)
            if dist[u] == inf or u == dest:
                break
            for v, cost in neighbours[u]:
                alt = dist[u] + cost
                if alt < dist[v]:                   # Relax (u,v,a)
                    dist[v] = alt
                    previous[v] = u
        s, u = [], dest
        while previous[u]:
            s.insert(0, u)
            u = previous[u]
        s.insert(0, u)
        return s


graph = Graph([("JPY", "EUR", .0069),
               ("EUR", "USD", 1.35),
               ])


print(graph.dijkstra("JPY", "USD"))

# Answer is .0092