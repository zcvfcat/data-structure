# 비순환 그래프

class DirectAcyclicGraph:
    def __init__(self, node_length):
        self.graph = [[] for _ in range(node_length)]
        self.visited = [False for _ in range(node_length)]

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False

    def dfs(self, v, ts_list):
        self.visited[v] = True

        adj_v = self.graph[v]
        for u in adj_v:
            if not self.visited[u]:
                self.dfs(u, ts_list)

        ts_list.append(v)

    def topological_sort(self):
        self.init_visited()
        ts_list = []
        for i in range(len(self.visited)):
            if not self.visited[i]:
                self.dfs(i, ts_list)
        ts_list.reverse()
        return ts_list


d = DirectAcyclicGraph(7)
d.add_edge(0, 4)
d.add_edge(1, 3)
d.add_edge(1, 4)
d.add_edge(2, 3)
d.add_edge(3, 5)
d.add_edge(3, 6)
d.add_edge(4, 2)

ts_list = d.topological_sort()

for i in ts_list:
    print(i, end=" ")
