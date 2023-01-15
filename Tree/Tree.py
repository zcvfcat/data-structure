from queue import Queue


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


def pre_order(cur):  # 전위
    if not cur:
        return

    print(cur.data, end=' ')
    pre_order(cur.left)
    pre_order(cur.right)


def in_order(cur):  # 중위
    if not cur:
        return

    pre_order(cur.left)
    print(cur.data, end=' ')
    pre_order(cur.right)


def post_order(cur):  # 후위
    if not cur:
        return

    pre_order(cur.left)
    pre_order(cur.right)
    print(cur.data, end=' ')


def iter_pre_order(cur):
    stack = []
    while True:
        while cur:
            print(cur.data, end='  ')
            stack.append(cur)
            cur = cur.left

        try:
            cur = stack.pop()
            if not cur:
                break

            cur = cur.right
        except:
            break


def iter_in_order(cur):
    stack = []
    while True:
        while cur:
            stack.append(cur)
            cur = cur.left

        try:
            cur = stack.pop()
            if not cur:
                break

            print(cur.data, end='  ')
            cur = cur.right
        except:
            break


def level_order(cur):
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
iter_pre_order(n1)
print()

# inorder(n1)
iter_in_order(n1)
print()

post_order(n1)
print()

level_order(n1)
print()
