
from collections import deque


class Graph:
    def __init__(self, node_length):
        self.graph = [[] for _ in range(node_length)]
        self.visited = [False for _ in range(node_length)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False

    def bfs(self, node):
        q = deque([node])
        self.init_visited()

        self.visited[node] = True

        while q:
            node = q.popleft()
            edges = self.graph[node]

            for edge in edges:
                if not self.visited[edge]:
                    q.append(edge)
                    self.visited[edge] = True

    def dfs(self, v):
        self.init_visited()
        self.__dfs_recursion(v)

    def __dfs_recursion(self, node):
        print(node, end=" ")
        self.visited[node] = True

        edges = self.graph[node]
        for edge in edges:
            if not self.visited[edge]:
                self.__dfs_recursion(edge)

    def iter_dfs(self, node):
        stack = list()
        self.init_visited()

        stack.append(node)
        self.visited[node] = True
        print(node, end=" ")

        is_visited = False

        while not stack:
            is_visited = False
            node = stack[-1]

            edges = self.graph[node]

            for edge in edges:
                if not self.visited[edge]:
                    stack.append(edge)
                    self.visited[edge] = True
                    print(edge, end=" ")
                    is_visited = True
                    break

            if not is_visited:
                stack.pop()

    def dfs_all(self):
        self.init_visited()

        for node in range(len(self.visited)):
            if not self.visited[node]:
                self.__dfs_recursion(node)


g = Graph(6)
g.add_edge(1, 0)
g.add_edge(0, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)
g.add_edge(2, 5)

# 예상 출력 결과 : 3  0  4  1  2  5
g.bfs(3)
print()
# 예상 출력 결과 : 3  0  1  4  2  5
g.dfs(3)
print()

g.iter_dfs(3)
print("\n\n\n")

print("dfs_all test code")
g2 = Graph(6)
g2.add_edge(0, 3)
g2.add_edge(1, 3)
g2.add_edge(2, 5)
g2.add_edge(4, 5)

print("dfs")
g2.dfs(1)
print()

print("dfs_all")
g2.dfs_all()
print()
