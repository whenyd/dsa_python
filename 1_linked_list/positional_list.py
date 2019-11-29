from base.doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    # ------------------------ nested Position class ------------------------
    class Position:
        """An abstraction representing the location of a single element."""
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            """Constructor should not be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    # --------------------------- utility method ---------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError('p must be proper Position type')

        if p._container is not self:
            raise ValueError('p does not belong to this container')

        # _DoublyLinkedBase._delete_node方法中删除的结点
        if p._node._next is None:
            raise ValueError('p is no longer valid')

        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)."""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # ------------------------------ accessors ------------------------------
    def first(self):
        """返回链表的第一个位置, 空链表返回None."""
        return self._make_position(self._header._next)

    def last(self):
        """返回链表的最后一个位置, 空链表返回None."""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------- mutators -------------------------------
    # override以便返回Position实例, 而不是结点
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """在列表头部插入元素并返回Position实例."""
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """在列表尾部插入元素并返回Position实例."""
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """删除并返回位置p的元素."""
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self, p, e):
        """用新的值e替换位置p的元素值, 并返回旧的值."""
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
