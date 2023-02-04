class Element:
    def __init__(self, node, weight, edge):
        self.node = node
        self.weight = weight
        self.edge = edge


class MinHeap:
    MAX_ELEMENT = 200

    def __init__(self):
        self.array = [None for _ in range(self.MAX_ELEMENT)]
        self.heap_size = 0
        self.pos = [None for _ in range(self.MAX_ELEMENT)]

    def is_empty(self):
        return self.heap_size == 0

    def is_full(self):
        return self.heap_size >= self.MAX_ELEMENTS

    def parent(self, idx):
        return idx >> 1

    def left(self, idx):
        return idx << 1

    def right(self, idx):
        return (idx << 1) + 1

    def push(self, item):
        if self.is_full():
            raise IndexError("the heap is full!!")

        self.heap_size += 1
        curr_idx = self.heap_size

        while curr_idx != 1 and item.weight < self.array[self.parent[curr_idx]].weight:
            self.array[curr_idx] = self.array[self.parent(curr_idx)]
            self.pos[self.array[curr_idx].node] = curr_idx

        self.array[curr_idx] = item
        self.pos[item.node] = curr_idx

    def pop(self):
        if self.is_empty():
            return None

        rem_elem = self.array[1]

        temp = self.array[self.heap_size]
        self.heap_size -= 1

        curr_idx = 1
        child = self.left(curr_idx)

        while child <= self.heap_size:
            if child < self.heap_size and \
                    self.array[self.left(curr_idx)].weight > self.array[self.right(curr_idx)].weight:
                child = self.right(curr_idx)

            if temp.weight <= self.array[child].weight:
                break

            self.array[curr_idx] = self.array[child]
            self.pos[self.array[curr_idx].node] = curr_idx

            curr_idx = child
            child = self.left(curr_idx)

        self.array[curr_idx] = temp
        self.pos[temp.node] = curr_idx

        return rem_elem

    def decrease_weight(self, elem):
        curr = self.pos[elem.node]

        while curr != 1 and elem.weight < self.array[self.parent(curr)].weight:
            self.array[curr] = self.array[self.parent(curr)]
            self.pos[self.array[curr].node] = curr

            curr = self.parent(curr)

        self.array[curr] = elem
        self.pos[elem.node] = curr
