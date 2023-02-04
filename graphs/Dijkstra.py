from math import inf
from heapq import heappush, heappop


class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item):
        heappush(self.heap, item)

    def pop(self):
        return heappop(self.heap)


class ShortestPath:
    def __init__(self, s, distance, p):
        self.source = s
        self.distance = distance
        self.p = p

    def print_shortest_path(self, dest):
        if self.source == dest:
            print(dest, end=" ")
            return

        if sp.p[dest] != None:
            self.print_shortest_path(self.p[dest])
        else:
            print('There is no path')
            return
        print(dest, end=' ')


class Graph:
    BIG_NUMBER = inf

    def __init__(self, node_length):
        self.edges = [[None for _ in range(node_length)] for _ in range(node_length)]
        self.node_length = node_length

    def add_edge(self, node, edge, weight):
        self.edges[node][edge] = weight

    def dijkstra(self, s):
        distance = [self.BIG_NUMBER for _ in range(self.node_length)]
        paths = [None for _ in range(self.node_length)]

        S = set()
        pq = MinPriorityQueue()

        for node in range(self.node_length):
            pq.push((self.BIG_NUMBER, node))

        distance[s] = 0
        pq.push((0, s))

        while len(S) < self.node_length:
            weight, node = pq.pop()
            if distance[node] != weight:
                continue

            S.add(node)

            edges = self.adjacent_set(node)
            for edge, cost in edges:
                if edge not in S and distance[edge] > distance[node]+cost:
                    distance[edge] = distance[node]+cost
                    paths[edge] = node
                    pq.push((distance[edge], edge))

        sp = ShortestPath(s, distance, paths)
        return sp

    def adjacent_set(self, node):
        edges = []

        for edge in range(self.node_length):
            weight = self.edges[node][edge]
            if weight:
                edges.append((edge, weight))
        return edges


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 3)
g.add_edge(1, 3, 5)
g.add_edge(2, 1, 5)
g.add_edge(2, 3, 8)
g.add_edge(3, 1, 4)
g.add_edge(3, 2, 12)

source = 0
sp = g.dijkstra(source)
for i in range(g.node_length):
    print(f"distance[{i}] : {sp.distance[i]}, p[{i}] : {sp.p[i]}")

dest = 3
print(f"path from {source} to {dest}")
sp.print_shortest_path(dest)
print()
