class _SinglyNode:
    __slots__ = '_element', '_next'

    def __init__(self, element=None, next_=None):
        self._element = element
        self._next = next_


class _DoublyNode:
    __slots__ = '_element', '_prev', '_next'

    def __init__(self, element=None, prev=None, next_=None):
        self._element = element
        self._prev = prev
        self._next = next_
