class Empty(Exception):
    pass


class SinglyLinkedQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._front = None
        self._back = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        return self._front._element

    def enqueue(self, e):
        node = self._Node(e, None)

        if self._front is None:
            self._front = node
        else:
            self._back._next = node

        self._back = node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise Empty('Stack is empty')

        item = self._front._element
        self._front = self._front._next
        self._size -= 1

        if self.is_empty():
            self._back = None

        return item
