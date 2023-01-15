class RBNode:
    def __init__(self, key) -> None:
        self.key = key

        self.color = 'RED'
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        return str(self.key)


class RedBlackTree:
    def __init__(self) -> None:
        self.__root = None
        self.__EXT = RBNode(None)
        self.__EXT.color = 'BLACK'

    def get_root(self):
        return self.__root

    def pre_order_traverse(self, cur, func, *args, **kwargs):
        if cur == self.__EXT:
            return

        func(cur, *args, **kwargs)
        self.pre_order_traverse(cur.left, func, * args, **kwargs)
        self.pre_order_traverse(cur.right, func, * args, **kwargs)

    def __left_rotate(self, n):
        r = n.right
        l = r.left

        l.parent = n
        n.right = l

        if n == self.__root:
            self.__root = r
        elif n.parent.left == n:
            n.parent.left = r
        else:
            n.parent.right = r

        r.parent = n.parent
        r.left = n
        n.parent = r

    def __right_rotate(self, n):
        l = n.left
        r = l.right

        r.parent = n
        n.left = r

        if n == self.__root:
            self.__root = l
        elif n.parent.left == n:
            n.parent.left = l
        else:
            n.parent.right = l

        l.parent = n.parent
        l.right = n
        n.parent = l

    def __insert_fix(self, n):
        pn = gn = un = None

        pn = n.parent

        while pn != None and pn.color == 'RED':
            gn = pn.parent
            if gn.left == pn:
                un = gn.right

                if un.color == 'RED':
                    gn.color = 'RED'
                    gn.color = un.color = 'BLACK'

                    n = gn
                    pn = n.parent

                else:
                    if pn.right == n:
                        self.__left_rotate(pn)
                        n, pn = pn, n

                    pn.color, gn.color = gn.color, pn.color
                    self.__right_rotate(gn)

            else:
                un = gn.left
                if un.color == 'RED':
                    gn.color = 'RED'
                    pn.color = un.color = 'BLACK'

                    n = gn
                    pn = n.parent
                else:
                    if pn.left == n:
                        self.__right_rotate(pn)
                        n, pn = pn, n

                    pn.color, gn.color = gn.color, pn.color
                    self.__left_rotate(gn)

        self.__root.color = 'BLACK'

    def insert(self, key):
        new_node = RBNode(key)
        new_node.left = self.__EXT
        new_node.right = self.__EXT

        cur = self.__root
        if not cur:
            self.__root = new_node
            self.__root.color = 'BLACK'
            return

        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                if cur == self.__EXT:
                    parent.left = new_node
                    new_node.parent = parent
                    break

            else:
                cur = cur.right
                if cur == self.__EXT:
                    parent.right = new_node
                    new_node.parent = parent
                    break

        self.__insert_fix(new_node)

    def print_node(self, rbn):
        if rbn:
            print("node : {}, ".format(rbn.key), end="")
            if rbn.color == "RED":
                print("color : RED, ", end="")
            else:
                print("color : BLACK, ", end="")
            if rbn.left:
                print("left : {}, ".format(rbn.left.key), end="")
            if rbn.right:
                print("right : {}, ".format(rbn.right.key), end="")
            if rbn.parent:
                print("parent : {}".format(rbn.parent.key), end="")
            print()


print('*' * 100)
rbt = RedBlackTree()

for i in range(10):
    rbt.insert(i)

rbt.pre_order_traverse(rbt.get_root(), rbt.print_node)
print('*' * 100)
