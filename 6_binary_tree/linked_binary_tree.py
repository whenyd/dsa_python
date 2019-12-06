"""
由于多种原因, 我们选择不将更新方法声明为Tree或BinaryTree抽象基类的一部分.
首先, 尽管封装原理表明一个类的外在行为不必取决于内部表示, 但是运算的效率在很大
程度上取决于表示. 我们希望每个树类的具体实现都提供最合适的更新方式.

第二个原因是我们可能不希望此类更新方法成为公共接口的一部分. 树的应用程序很多,
而适合一种应用程序的某些形式的更新操作在另一种应用程序中可能是不可接受的. 但是,
如果将更新方法放在基类中, 则从该基类继承的任何类都将继承该更新方法. 例如, 考虑
方法T.replace(p, e)用另一个元素e替换存储在位置p的元素的可能性. 这样的通用
方法在算术表达式树的上下文中可能是不可接受的, 因为我们可能希望强制内部节点仅将
运算符存储为元素.

Reference:
- Data Structures and Algorithms in Python. Michael T. Goodrich,
  Roberto Tamassia, Michael H. Goldwasser. P318.
"""

from base.tree import BinaryTree
from base.node import _BinaryTreeNode


class LinkedBinaryTree(BinaryTree):

    class Position(BinaryTree.Position):
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(other) and other._node is self._node

    def __init__(self):
        self._root = None
        self._size = 0

    def _validate(self, p):
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        if p._node._parent is p._node:
            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1
        return count

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    # --------------------------- update method ---------------------------

    def _add_root(self, e):
        if self._root is not None:
            raise ValueError('Root exists')

        self._size = 1
        self._root = _BinaryTreeNode(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError('Left child exists')
        self._size += 1
        node._left = _BinaryTreeNode(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError('Right child exists')
        self._size += 1
        node._right = _BinaryTreeNode(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """Delete the node at Position p, and replace it with its child, if any.

        Return the element that had been stored at Position p.
        Raise ValueError if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError('p has two children')

        child = node._left if node._left else node._right
        if child is not None:
            child._parent = node._parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:  # todo node.is_left()
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = None  # todo node.deprecated()
        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p):
            raise ValueError('position must be leaf')
        if not type(self) is type(t1) is type(t2):
            raise TypeError('Tree types must match')

        self._size += len(t1) + len(t2)
        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0
        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0


if __name__ == '__main__':
    bt = LinkedBinaryTree()
    bt._add_root(1)
    bt._add_left(bt.root(), 2)
    bt._add_right(bt.root(), 3)
    bt._add_left(bt.left(bt.root()), 4)
    bt._add_right(bt.left(bt.root()), 5)
    bt._add_left(bt.right(bt.root()), 6)

    # for p in bt.preorder():
    #     print(p.element())
    #
    # print()
    # for p in bt.postorder():
    #     print(p.element())
    #
    # print()
    # pos = bt.positions()
    # for p in pos:
    #     print(p.element())

    for p in bt.inorder():
        print(p.element())
