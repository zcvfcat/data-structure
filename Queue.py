class Queue:
    def __init__(self) -> None:
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[0]
