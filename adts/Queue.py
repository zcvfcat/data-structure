class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        return not self.container

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[0]


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

while not q.empty():
    print(q.dequeue(), end='  ')
