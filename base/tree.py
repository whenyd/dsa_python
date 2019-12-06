"""
Abstract base class of tree ADT.
"""
from abc import ABC


class Tree:
    """树的抽象基类."""

    class Position:
        """树中结点的位置ADT."""

        def element(self):
            """返回存储在当前Position的元素."""
            raise NotImplementedError('must be implemented by subclass')

        def __eq__(self, other):
            raise NotImplementedError('must be implemented by subclass')

        def __ne__(self, other):
            return not self == other

    def root(self):
        """返回root的Position, 空树返回None."""
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        """返回p的父结点的Position, p为root返回None."""
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        """Return the number of children that Position p has."""
        raise NotImplementedError('must be implemented by subclass')

    def positions(self):
        """Generate an iteration of all positions of tree T."""
        return self.preorder()

    def __len__(self):
        """Return the total number of elements in the tree."""
        raise NotImplementedError('must be implemented by subclass')

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    def depth(self, p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """Return the height of the tree.

        O(n^2) worst-case time.
        """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """Return the height of the tree.

        O(n) worst-case time.
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p=None):
        """Return the height of the subtree rooted at Position p.

        If p is None, return the height of the entire tree.
        """
        if p is None:
            p = self.root()
        return self._height2(p)

    def preorder(self):
        """
        Algorithm preorder(T, p):
            perform the “visit” action for position p
            for each child c in T.children(p) do
                preorder(T, c)
        """
        if not self.is_empty():
            yield from self._subtree_preorder(self.root())
            # for p in self._subtree_preorder(self.root()):
            #     yield p

    def _subtree_preorder(self, p):
        yield p
        for c in self.children(p):
            yield from self._subtree_preorder(c)
            # for other in self._subtree_preorder(c):
            #     yield other

    def postorder(self):
        """
        Algorithm postorder(T, p):
            for each child c in T.children(p) do
                preorder(T, c)
            perform the “visit” action for position p
        """
        if not self.is_empty():
            yield from self._subtree_postorder(self.root())

    def _subtree_postorder(self, p):
        for c in self.children(p):
            yield from self._subtree_postorder(c)
        yield p

    def breadth_first(self):
        """
        Algorithm breadthfirst(T):
            Initialize queue Q to contain T.root( )
            while Q not empty do
                p = Q.dequeue( )  {p is the oldest entry in the queue}
                perform the “visit” action for position p
                for each child c in T.children(p) do
                    Q.enqueue(c)  {add p’s children to the end of the queue for later visits}
        """
        if self.is_empty():
            return

        queue = [self.root()]  # 实际可以用queue.Queue()或SinglyLinkedQueue
        while len(queue) > 0:
            p = queue.pop(0)
            yield p
            for c in self.children(p):
                queue.append(c)


class BinaryTree(Tree, ABC):

    def left(self, p):
        """Return the position that represents the left child of p,
        or None if p has no left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def right(self, p):
        """Return the position that represents the left child of p,
        or None if p has no left child.
        """
        raise NotImplementedError('must be implemented by subclass')

    def sibling(self, p):
        """Return the position that represents the sibling of p,
        or None if p has no sibling.
        """
        parent = self.parent(p)
        if parent is None:
            return None

        if p == self.left(parent):
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)

        if self.right(p) is not None:
            yield self.right(p)

    def inorder(self):
        """
        Algorithm inorder(p):
            if p has a left child lc then
                inorder(lc) {recursively traverse the left subtree of p}
            perform the “visit” action for position p
            if p has a right child rc then
                inorder(rc) {recursively traverse the right subtree of p}
        """
        if not self.is_empty():
            yield from self._subtree_inorder(self.root())

    def _subtree_inorder(self, p):
        left = self.left(p)
        if left is not None:
            yield from self._subtree_inorder(left)
        yield p
        right = self.right(p)
        if right is not None:
            yield from self._subtree_inorder(right)

    def positions(self):
        return self.inorder()
