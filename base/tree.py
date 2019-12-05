from abc import ABC
from abc import abstractmethod


class Tree(ABC):
    """树的抽象基类."""

    class Position(ABC):
        """树中结点的位置ADT."""

        @abstractmethod
        def element(self):
            """返回存储在当前Position的元素."""
            pass

        @abstractmethod
        def __eq__(self, other):
            pass

        def __ne__(self, other):
            return not self == other

    @abstractmethod
    def root(self):
        """返回root的Position, 空树返回None."""
        pass

    @abstractmethod
    def parent(self, p):
        """返回p的父结点的Position, p为root返回None."""
        pass

    @abstractmethod
    def children(self, p):
        """Generate an iteration of Positions representing p s children."""
        pass

    @abstractmethod
    def num_children(self, p):
        """Return the number of children that Position p has."""
        pass

    @abstractmethod
    def positions(self):
        """Generate an iteration of all positions of tree T."""
        pass

    @abstractmethod
    def __len__(self):
        """Return the total number of elements in the tree."""
        pass

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