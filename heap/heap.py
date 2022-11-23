class Heap:
    def __init__(self, *args) -> None:
        if len(args) != 0:
            self.array = args[0]
        else:
            self.array = []

    def insert(self, x):
        self.array.append(x)
        self.__percolateUp(len(self.array) - 1)

    def __percolateUp(self, i: int):
        parent = (i - 1) // 2
        if i > 0 and self.array[i] > self.array[parent]:
            self.array[i], self.array[parent] = self.array[parent], self.array[i]
            self.__percolateUp(parent)

    def deleteMax(self):
        if not self.isEmpty():
            max = self.array[0]
            self.array[0] = self.array.pop()
            self.__percolateDown(0)
            return max
        else:
            return None

    def __percolateDown(self, i: int):
        child = 2 * i + 1
        right = 2 * i + 2

        if child <= len(self.array) - 1:
            if right <= len(self.array) - 1 and self.array[child] < self.array[right]:
                child = right
            if self.array[i] < self.array[child]:
                self.array[i], self.array[child] = self.array[child], self.array[i]
                self.__percolateDown(child)

    def max(self):
        return self.array[0]

    def buildHeap(self):
        for i in range((len(self.array) - 2) // 2, - 1, -1):
            self.__percolateDown(i)

    def isEmpty(self) -> bool:
        return len(self.array) == 0

    def clear(self):
        self.array = []

    def size(self) -> int:
        return len(self.array)


h1 = Heap([1, 11, 9, 2, 3])
h1.buildHeap()
h1.clear()
# h1.heapPrint()
h1.insert(7)
h1.insert(5)
h1.insert(9)
h1.insert(4)
h1.insert(11)
h1.insert(19)
h1.insert(20)
h1.insert(21)
h1.insert(11)
# h1.heapPrint()
h1.deleteMax()
# h1.heapPrint()
