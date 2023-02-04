class Element:
    def __init__(self, key):
        self.key = key


class MaxHeap:
    MAX_ELEMENTS = 100

    def __init__(self):
        self.array = [None for _ in range(self.MAX_ELEMENTS + 1)]
        self.heap_size = 0

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
            raise IndexError("the heap is full !!")

        self.heap_size += 1
        curr_idx = self.heap_size

        while curr_idx != 1 and item.key > self.array[self.parent(curr_idx)].key:
            self.array[curr_idx] = self.array[self.parent(curr_idx)]
            curr_idx = self.parent(curr_idx)
        self.array[curr_idx] = item

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
                    self.array[self.left(curr_idx)].key < self.array[self.right(curr_idx)].key:
                child = self.right(curr_idx)

            if temp.key >= self.array[child].key:
                break

            self.array[curr_idx] = self.array[child]
            curr_idx = child
            child = self.left(curr_idx)

        self.array[curr_idx] = temp

        return rem_elem


def print_heap(h):
    for node in range(1, h.heap_size + 1):
        print("{}".format(h.arr[node].key), end=" ")
    print()


h = MaxHeap()

h.push(Element(2))
h.push(Element(14))
h.push(Element(9))
h.push(Element(11))
h.push(Element(6))
h.push(Element(8))

print_heap(h)

while not h.is_empty():
    rem = h.pop()
    print(f'poped item is {rem.key}')
    print_heap(h)
