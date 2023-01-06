from BinaryTree import TreeNode


class BST:
    def __init__(self) -> None:
        self.root = None

    def get_root(self):
        return self.root

    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def inorder_traverse(self, cur, func):
        if not cur:
            return

        self.inorder_traverse(cur.left, func)
        func(cur)
        self.inorder_traverse(cur.right, func)

    def __make_left(self, cur, left):
        cur.left = left
        if left:
            left.parent = cur

    def __make_right(self, cur, right):
        cur.right = right
        if right:
            right.parent = cur

    def insert(self, key):
        new_node = TreeNode(key)

        cur = self.root
        if not cur:
            self.root = new_node
            return

        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                if not cur:
                    self.__make_left(parent, new_node)
                    return
            else:
                cur = cur.right
                if not cur:
                    self.__make_right(parent, new_node)
                    return

    def search(self, target):
        cur = self.root
        while cur:
            if cur.key == target:
                return cur
            elif cur.key > target:
                cur = cur.left
            elif cur.key < target:
                cur = cur.right
        return cur

    def __delete_recursion(self, cur, target):
        if not cur:
            return None
        elif target < cur.key:
            new_left = self.__delete_recursion(cur.left, target)
            self.__make_left(cur, new_left)
        elif target > cur.key:
            new_right = self.__delete_recursion(cur.right, target)
            self.__make_right(cur, new_right)
        else:
            if not cur.left and not cur.right:
                cur = None
            elif not cur.right:
                cur = cur.left
            elif not cur.left:
                cur = cur.right
            else:
                replace = cur.left
                replace = self.max(replace)
                cur.key, replace.key = replace.key, cur.key
                new_left = self.__delete_recursion(cur.left, replace.key)
                self.__make_left(cur, new_left)
        return cur

    def delete(self, target):
        new_root = self.__delete_recursion(self.root, target)
        self.root = new_root

    def min(self, cur):
        while cur.left != None:
            cur = cur.left
        return cur

    def max(self, cur):
        while cur.right != None:
            cur = cur.right
        return cur

    def prev(self, cur):
        if cur.left:
            return self.max(cur.left)

        parent = cur.parent

        while parent and cur == parent.left:
            cur = parent
            parent = parent.parent

        return parent

    def next(self, cur):
        if cur.right:
            return self.min(cur.right)

        parent = cur.parent

        while parent and cur == parent.right:
            cur = parent
            parent = parent.parent

        return parent


print('*'*100)
bst = BST()

bst.insert(6)
bst.insert(3)
bst.insert(2)
bst.insert(4)
bst.insert(5)
bst.insert(8)
bst.insert(10)
bst.insert(9)
bst.insert(11)


def f(x): return print(x.key, end='  ')


#bst.preorder_traverse(bst.get_root(), f)
bst.inorder_traverse(bst.get_root(), f)
print()

searched_node = bst.search(8)
if searched_node:
    print(f'searched key : {searched_node.key}')

    prev_node = bst.prev(searched_node)
    if prev_node:
        print(f'prev key : {prev_node.key}')
    else:
        print(f'this is the first key of the BST')

    next_node = bst.next(searched_node)
    if next_node:
        print(f'next key : {next_node.key}')
    else:
        print(f'this is the last key of the BST')
else:
    print('there is no such key')
print()


print(f'MIN(bst) : {bst.min(bst.get_root()).key}')
print(f'MAX(bst) : {bst.max(bst.get_root()).key}')

# bst.delete(9)
# bst.delete(8)
bst.delete(6)

# print(bst.delete(15))

bst.preorder_traverse(bst.get_root(), f)
# bst.inorder_traverse(bst.get_root(), f)
print()
print('*'*100)
