
from Tree.Tree import TreeNode, iter_in_order, iter_pre_order, level_order, post_order


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
