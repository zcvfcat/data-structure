# 미완성
from math import inf
from heapq import heappush, heappop


class Edge:
    def __init__(self, node, edge, weight):
        self.node = node
        self.edge = edge
        self.weight = weight


class Graph:
    def __init__(self, node_length):
        self.graph = [[] for _ in range(node_length)]
        self.edges = []

        self.node_length = node_length

    def add_edge(self, node, edge, weight):
        self.graph[node].append((edge, weight))
        self.graph[edge].append((node, weight))

        self.edges.append(Edge(node, edge, weight))

    def MST_prim(self):
        mst = Graph(self.node_length)
        weights = [inf for _ in range(self.node_length)]

        TV = set()
        heap = []
        for node in range(1, self.node_length):
            heappush(heap, (inf, node, None))

        weights[0] = 0
        heappush(heap, (0, 0, None))

        while heap:
            weight, node, edge = heappop(heap)

            TV.add(node)
            if edge != None:
                mst.add_edge(node, edge, weight)

            for edge, cost in self.graph[node]:
                if edge not in TV and cost < weights[edge]:
                    weights[edge] = cost
                    heappush(heap, (cost, edge, node))

        return mst

    def print_edges(self):
        for edge in self.edges:
            print("({}, {}) : {}".format(edge.node, edge.edge, edge.weight))


graph = Graph(6)

graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 2)
graph.add_edge(0, 3, 8)
graph.add_edge(1, 2, 5)
graph.add_edge(1, 4, 12)
graph.add_edge(2, 3, 7)
graph.add_edge(2, 4, 17)
graph.add_edge(3, 4, 4)
graph.add_edge(3, 5, 14)

mst = graph.MST_prim()

mst.print_edges()
