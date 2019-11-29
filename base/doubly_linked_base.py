from base.node import DoublyNode


class DoublyLinkedBase:

    def __init__(self):
        self._header = DoublyNode()
        self._trailer = DoublyNode()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        node = DoublyNode(e, predecessor, successor)
        predecessor._next = node
        successor._prev = node
        self._size += 1

        return node

    def _delete_node(self, node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1

        element = node._element
        # 将结点属性都标记为None, 有助于GC
        node._prev = node._next = node._element = None

        return element
