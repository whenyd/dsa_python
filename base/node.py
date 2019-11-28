class SinglyNode:
    __slots__ = '_element', '_next'

    def __init__(self, element=None, next_=None):
        self._element = element
        self._next = next_


class DoublyNode:
    __slots__ = '_element', '_prev', '_next'

    def __init__(self, element, prev, next_):
        self._element = element
        self._prev = prev
        self._next = next_
