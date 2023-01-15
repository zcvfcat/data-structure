# 미완성
from math import inf
from heapq import heappush, heappop


class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w


class Graph:
    def __init__(self, vertex_num):
        self.adj_list = [[] for _ in range(vertex_num)]
        self.edge_list = []

        self.vertex_num = vertex_num

    def add_edge(self, u, v, w):
        self.adj_list[u].append((v, w))
        self.adj_list[v].append((u, w))

        self.edge_list.append(Edge(u, v, w))

    def MST_prim(self):
        mst = Graph(self.vertex_num)
        w_list = [inf for _ in range(self.vertex_num)]

        TV = set()
        heap = []
        for i in range(1, self.vertex_num):
            heappush(heap, (i, inf, None))

        w_list[0] = 0
        heappush(heap, (0, 0, None))

        while heap:
            w, v, _from = heappop(heap)

            TV.add(v)
            if _from != None:
                mst.add_edge(v, _from, w)

            adj_v = self.adj_list[v]
            for u, w_u_v in adj_v:
                if u not in TV and w_u_v < w_list[u]:
                    w_list[u] = w_u_v
                    # TODO: heap

        return mst

    def print_edges(self):
        for edge in self.edge_list:
            print("({}, {}) : {}".format(edge.u, edge.v, edge.w))


g = Graph(6)

g.add_edge(0, 1, 10)
g.add_edge(0, 2, 2)
g.add_edge(0, 3, 8)
g.add_edge(1, 2, 5)
g.add_edge(1, 4, 12)
g.add_edge(2, 3, 7)
g.add_edge(2, 4, 17)
g.add_edge(3, 4, 4)
g.add_edge(3, 5, 14)

mst = g.MST_prim()

mst.print_edges()
