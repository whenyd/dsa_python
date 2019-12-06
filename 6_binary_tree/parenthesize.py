"""Preorder traversal"""

# 应该使用普通的树而不是二叉树
from linked_binary_tree import LinkedBinaryTree

# Electronics R’Us
#   1 R&D
#   2 Sales
#     2.1 Domestic
#     2.2 International
#       2.2.1 Canada
#       2.2.2 America
toc = LinkedBinaryTree()
toc._add_root('Electronics R’Us')
toc._add_left(toc.root(), 'R&D')
toc._add_right(toc.root(), 'Sales')
toc._add_left(toc.right(toc.root()), 'Domestic')
toc._add_right(toc.right(toc.root()), 'International')
toc._add_left(toc.right(toc.right(toc.root())), 'Canada')
toc._add_right(toc.right(toc.right(toc.root())), 'America')


def parenthesize(t, p, rep):
    if t.is_empty():
        return

    rep += str(p.element())

    if not t.is_leaf(p):
        first_time = True
        for c in t.children(p):
            sep = ' (' if first_time else ', '
            rep += sep
            first_time = False
            rep = parenthesize(t, c, rep)
        rep += ')'
    return rep


rep = parenthesize(toc, toc.root(), '')
print(rep)
