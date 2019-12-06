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


# Solution 1: O(n^2)
# for p in toc.preorder():
#     print(toc.depth(p)*2*' '+p.element())


# Solution 2: O(n)
def preorder_indent(t, p, d):
    print(2 * d * ' ' + p.element())
    for c in t.children(p):
        preorder_indent(t, c, d + 1)


# preorder_indent(toc, toc.root(), 0)


# Solution 3: Display with indentation and also explicit numbering
def preorder_label(t, p, d, path):
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label, p.element())

    path.append(0)  # 当前结点的子树, 当前结点的序号为0
    for c in t.children(p):
        preorder_label(t, c, d+1, path)
        path[-1] += 1  # 兄弟结点数量+1
    path.pop()  # 回到上一层


preorder_label(toc, toc.root(), 0, [])
