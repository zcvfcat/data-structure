from queue import Queue
from Stack import Stack


class TreeNode:
    def __init__(self, data=None) -> None:
        self.__data = data
        self.__left = None
        self.__right = None

    def __del__(self) -> None:
        print(f'data {self.__data} is deleted')

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


def preorder(cur):  # 전위
    if not cur:
        return

    print(cur.data, end=' ')
    preorder(cur.left)
    preorder(cur.right)


def inorder(cur):  # 중위
    if not cur:
        return

    preorder(cur.left)
    print(cur.data, end=' ')
    preorder(cur.right)


def postorder(cur):  # 후위
    if not cur:
        return

    preorder(cur.left)
    preorder(cur.right)
    print(cur.data, end=' ')


def iter_preorder(cur):
    stack = Stack()
    while True:
        while cur:
            print(cur.data, end='  ')
            stack.push(cur)
            cur = cur.left

        cur = stack.pop()
        if not cur:
            break

        cur = cur.right


def iter_inorder(cur):
    stack = Stack()
    while True:
        while cur:
            stack.push(cur)
            cur = cur.left
        cur = stack.pop()
        if not cur:
            break

        print(cur.data, end='  ')
        cur = cur.right


def levelorder(cur):
    q = Queue()

    q.put(cur)

    while not q.empty():
        cur = q.get()
        print(cur.data, end=' ')

        if cur.left:
            q.put(cur.left)

        if cur.right:
            q.put(cur.right)


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

# preorder(n1)
iter_preorder(n1)
print()

# inorder(n1)
iter_inorder(n1)
print()

postorder(n1)
print()

levelorder(n1)
print()
