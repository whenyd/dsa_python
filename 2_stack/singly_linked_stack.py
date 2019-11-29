from base.exception import EmptyError
from base.node import _SinglyNode


class SinglyLinkedStack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._top = _SinglyNode(e, self._top)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')

        return self._top._element

    def pop(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')

        item = self._top._element
        self._top = self._top._next
        self._size -= 1

        return item
