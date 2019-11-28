from base.exception import EmptyError
from base.node import SinglyNode


class CircularlyLinkedQueue:
    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')

        return self._tail._next._element

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('Stack is empty')

        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next

        self._size -= 1

        return old_head._element

    def enqueue(self, e):
        node = SinglyNode(e, None)

        if self.is_empty():
            node._next = node
        else:
            node._next = self._tail._next
            self._tail._next = node

        self._tail = node
        self._size += 1

    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
