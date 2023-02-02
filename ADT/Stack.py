class Stack:
    def __init__(self):
        self.container = list()

    def empty(self):
        return not self.container

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


s = Stack()

s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)

while not s.empty():
    print(s.pop(), end='  ')
