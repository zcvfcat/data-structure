# 비순환 그래프

class DirectAcyclicGraph:
    def __init__(self, node_length):
        self.graph = [[] for _ in range(node_length)]
        self.visited = [False for _ in range(node_length)]

    def add_edge(self, node, edge):
        self.graph[node].append(edge)

    def init_visited(self):
        for node in range(len(self.visited)):
            self.visited[node] = False

    def dfs(self, node, paths):
        self.visited[node] = True

        edges = self.graph[node]
        for edge in edges:
            if not self.visited[edge]:
                self.dfs(edge, paths)

        paths.append(node)

    def topological_sort(self):
        self.init_visited()
        paths = []

        for node in range(len(self.visited)):
            if not self.visited[node]:
                self.dfs(node, paths)

        paths.reverse()
        return paths


graph = DirectAcyclicGraph(7)
graph.add_edge(0, 4)
graph.add_edge(1, 3)
graph.add_edge(1, 4)
graph.add_edge(2, 3)
graph.add_edge(3, 5)
graph.add_edge(3, 6)
graph.add_edge(4, 2)

ts_list = graph.topological_sort()

for i in ts_list:
    print(i, end=" ")
