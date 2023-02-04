from DisjointSet import DisjointSet


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
        self.graph[node].append(edge)
        self.graph[edge].append(node)

        self.edges.append(Edge(node, edge, weight))

    def MST_kruskal(self):
        mst = Graph(self.node_length)
        ds = DisjointSet(self.node_length)
        self.edges.sort(key=lambda edge: edge.weight)
        mst_edge_num = 0
        edge_idx = 0

        while mst_edge_num < self.node_length - 1:
            edge = self.edges[edge_idx]
            if ds.collapsing_find(edge.node) != ds.collapsing_find(edge.edge):
                mst.add_edge(edge.node, edge.edge, edge.weight)
                ds.weighted_union(ds.collapsing_find(edge.node), ds.collapsing_find(edge.edge))
                mst_edge_num += 1
            edge_idx += 1

        return mst

    def print_edges(self):
        for edge in self.edges:
            print("({}, {}) : {}".format(edge.node, edge.edge, edge.weight))


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

mst = g.MST_kruskal()

mst.print_edges()
