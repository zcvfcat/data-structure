class Stack:
    def __init__(self) -> None:
        self.container = list()

    def empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        if self.empty():
            return None

        return self.container.pop()

    def peek(self):
        if self.empty():
            return None

        return self.container[-1]
