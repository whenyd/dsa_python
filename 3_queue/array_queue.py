from base.exception import EmptyError


class ArrayQueue:
    """Circularly array queue."""
    def __init__(self, capacity=10):
        self.capacity = capacity
        self._data = [None] * capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def is_full(self):
        return self._size == self.capacity

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise EmptyError('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise EmptyError('Queue is empty')

        item = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1

        if 0 < self._size < self.capacity // 4:
            self._resize(self.capacity // 2)

        return item

    def enqueue(self, e):
        if self.is_full():
            self._resize(self.capacity * 2)

        # back是队尾的空位置
        # 它在front的位置向前size, 而循环队列需要对capacity取余数
        back = (self._front + self._size) % self.capacity
        self._data[back] = e
        self._size += 1

    def _resize(self, cap):
        data = self._data
        self.capacity = cap
        self._data = [None] * self.capacity

        walk = self._front
        for i in range(self._size):
            self._data[i] = data[walk]
            walk = (walk + 1) % len(data)

        self._front = 0


if __name__ == '__main__':
    queue = ArrayQueue(4)
    queue.enqueue(0)
    queue.enqueue(2)
    queue.enqueue(4)
    queue.dequeue()
    queue.enqueue(6)
    queue.dequeue()
    queue.enqueue(8)
    queue.enqueue(10)
    queue.enqueue(12)

    queue = ArrayQueue(2)
    for i in range(17):
        queue.enqueue(i)  # capacity=32, size=17

    for i in range(8):
        print(queue.dequeue())  # capacity=32, size=9

    while not queue.is_empty():
        print(queue.dequeue())

    print('OK')
