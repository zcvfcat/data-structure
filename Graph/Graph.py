
from queue import Queue


class Graph:
    def __init__(self, vertex_num):
        self.adj_list = [[] for _ in range(vertex_num)]
        self.visited = [False for _ in range(vertex_num)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False

    def bfs(self, node):
        q = Queue()
        self.init_visited()

        q.put(node)
        self.visited[node] = True

        while not q.empty():
            node = q.get()
            edges = self.adj_list[node]

            for edge in edges:
                if not self.visited[edge]:
                    q.put(edge)
                    self.visited[edge] = True

    def dfs(self, v):
        self.init_visited()
        self.__dfs_recursion(v)

    def __dfs_recursion(self, node):
        print(node, end=" ")
        self.visited[node] = True

        edges = self.adj_list[node]
        for edge in edges:
            if not self.visited[edge]:
                self.__dfs_recursion(edge)

    def iter_dfs(self, v):
        stack = list()
        self.init_visited()

        stack.append(v)
        self.visited[v] = True
        print(v, end=" ")

        is_visited = False

        while not stack:
            is_visited = False
            v = stack[-1]

            edges = self.adj_list[v]

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

        for i in range(len(self.visited)):
            if not self.visited[i]:
                self.__dfs_recursion(i)


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
