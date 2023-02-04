from BinaryTree import TreeNode


class BST:
    def __init__(self):
        self.root = None

    def get_root(self):
        return self.root

    def pre_order_traverse(self, curr, func):
        if not curr:
            return

        func(curr)
        self.pre_order_traverse(curr.left, func)
        self.pre_order_traverse(curr.right, func)

    def in_order_traverse(self, curr, func):
        if not curr:
            return

        self.in_order_traverse(curr.left, func)
        func(curr)
        self.in_order_traverse(curr.right, func)

    def __make_left(self, curr, left):
        curr.left = left
        if left:
            left.parent = curr

    def __make_right(self, curr, right):
        curr.right = right
        if right:
            right.parent = curr

    def insert(self, key):
        new_node = TreeNode(key)

        curr = self.root
        if not curr:
            self.root = new_node
            return

        while True:
            parent = curr
            if key < curr.key:
                curr = curr.left
                if not curr:
                    self.__make_left(parent, new_node)
                    return
            else:
                curr = curr.right
                if not curr:
                    self.__make_right(parent, new_node)
                    return

    def search(self, target):
        curr = self.root
        while curr:
            if curr.key == target:
                return curr
            elif curr.key > target:
                curr = curr.left
            elif curr.key < target:
                curr = curr.right
        return curr

    def __delete_recursion(self, curr, target):  # 삭제하는 노드가 리프 노드인지 자식만 있는 노드인지 나누어서 삭제해야함
        if not curr:
            return None
        elif target < curr.key:
            new_left = self.__delete_recursion(curr.left, target)
            self.__make_left(curr, new_left)
        elif target > curr.key:
            new_right = self.__delete_recursion(curr.right, target)
            self.__make_right(curr, new_right)
        else:
            if not curr.left and not curr.right:
                curr = None
            elif not curr.right:
                curr = curr.left
            elif not curr.left:
                curr = curr.right
            else:
                replace = curr.left
                replace = self.max(replace)
                curr.key, replace.key = replace.key, curr.key
                new_left = self.__delete_recursion(curr.left, replace.key)
                self.__make_left(curr, new_left)
        return curr

    def delete(self, target):
        new_root = self.__delete_recursion(self.root, target)
        self.root = new_root

    def min(self, cur):
        while cur.left is not None:
            cur = cur.left
        return cur

    def max(self, cur):
        while cur.right is not None:
            cur = cur.right
        return cur

    def prev(self, cur):
        if cur.left:
            return self.max(cur.left)

        parent = cur.parent

        while parent and cur is parent.left:
            cur = parent
            parent = parent.parent

        return parent

    def next(self, cur):
        if cur.right:
            return self.min(cur.right)

        parent = cur.parent

        while parent and cur is parent.right:
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
bst.in_order_traverse(bst.get_root(), f)
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

bst.pre_order_traverse(bst.get_root(), f)
# bst.inorder_traverse(bst.get_root(), f)
print()
print('*'*100)
