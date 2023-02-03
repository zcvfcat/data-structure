class DisjointSet:
    def __init__(self, node_length):
        self.parent = [-1 for _ in range(node_length)]

    def simple_find(self, i):
        while self.parent[i] >= 0:
            i = self.parent[i]
        return i

    def simple_union(self, node, edge):
        self.parent[node] = edge

    def collapsing_find(self, node):
        root = trail = lead = None
        root = node
        while self.parent[root] >= 0:
            root = self.parent[root]

        trail = node
        while trail != root:
            lead = self.parent[trail]
            self.parent[trail] = root
            trail = lead

        return root

    def weighted_union(self, node_a, node_b):
        temp_cnt = self.parent[node_a] + self.parent[node_b]

        if self.parent[node_a] > self.parent[node_b]:
            self.parent[node_a] = node_b
            self.parent[node_b] = temp_cnt

        else:
            self.parent[node_b] = node_a
            self.parent[node_a] = temp_cnt


ds = DisjointSet(5)
# ds.simple_union(1, 2)
# ds.simple_union(4, 2)
# ds.simple_union(3, 0)
# print(ds.parent)

# for i in range(5):
#     print("parent[{}] : {}".format(i, ds.simple_find(i)))

ds.parent[2] = -5
ds.parent[4] = 2
ds.parent[0] = 4
ds.parent[1] = 0
ds.parent[3] = 1

print(ds.parent)
print("the root is {}". format(ds.collapsing_find(3)))
print(ds.parent)
