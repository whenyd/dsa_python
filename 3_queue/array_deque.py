from array_queue import ArrayQueue


class Empty(Exception):
    pass


class ArrayDeque(ArrayQueue):
    def __init__(self, capacity=10):
        super().__init__(capacity)

    def add_last(self, e):
        super().enqueue(e)

    def delete_first(self):
        super().dequeue()

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        # 最后一个数据保的位置, 比队尾空位置提前一个索引
        last_idx = (self._front + self._size - 1) % self.capacity
        return self._data[last_idx]

    def add_first(self, e):
        if self.is_full():
            self._resize(self.capacity * 2)

        self._front = (self.capacity + self._front - 1) % self.capacity
        self._data[self._front] = e
        self._size += 1

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty')

        last_idx = (self._front + self._size - 1) % self.capacity
        item = self._data[last_idx]
        self._data[last_idx] = None
        self._size -= 1

        if 0 < self._size < self.capacity // 4:
            self._resize(self.capacity // 2)

        return item


if __name__ == '__main__':
    queue = ArrayDeque(4)
    queue.add_first(0)
    queue.add_first(2)
    queue.add_last(4)
    queue.delete_first()
    queue.last()
    queue.first()
    queue.delete_first()
    queue.add_first(1)
    queue.add_last(2)
    queue.add_last(3)
    queue.add_last(6)

    print('OK')

