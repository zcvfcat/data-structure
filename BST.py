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
