class Empty(Exception):
    pass


class SinglyLinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._top = self._Node(e, self._top)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        return self._top._element

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        item = self._top._element
        self._top = self._top._next
        self._size -= 1

        return item
