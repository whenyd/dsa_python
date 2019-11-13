class Node:
    def __init__(self, item=None, next_=None):
        self.item = item
        self.next = next_


class SingleLinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        node = self.head
        while node is not None:
            print(node.item)
            node = node.next

    def creat_by_insert_head(self, item_iter):
        """头插法建立链表, 新结点始终插入到链表头部."""
        for item in item_iter:
            self.insert_to_head(item)

    def creat_by_insert_tail(self, item_iter):
        """尾插法建立链表, 新结点始终插入到链表尾部."""
        for item in item_iter:
            node = Node(item)
            if self.head is None:
                self.head = node
                tail = self.head
            else:
                tail.next = node  # 新结点加入尾部
                tail = node  # tail指向新结点

    # def creat_by_insert_tail(self, item_iter):
    #     """尾插法建立链表, 新结点始终插入到链表尾部."""
    #     self.head = Node(item_iter[0])  # 生成器出错
    #     tail = self.head
    #     for item in item_iter[1:]:
    #         node = Node(item)
    #         tail.next = node  # 新结点加入尾部
    #         tail = node  # tail指向新结点

    def insert_to_head(self, item=None):
        node = Node(item, self.head)  # 新结点next指向当前head
        self.head = node  # 移动head到新结点

    # def insert_to_tail(self, item):
    #     node = Node(item)
    #     self.tail.next = node

    def insert_after(self, node, item):
        if node is None or self.head is None:
            return

        new_node = Node(item)
        new_node.next = node.next  # 新结点next指向原来结点的next
        node.next = new_node  # 原来结点的next指向新结点

    def insert_before(self, node, item):
        if node is None or self.head is None:
            return

        if node == self.head:
            self.insert_to_head(item)

        new_node = Node(item)

        # 寻找node的前一个结点
        this = self.head
        while this.next != node and this.next is not None:
            this = this.next

        if this is None:
            return

        new_node.next = node
        this.next = new_node

    def delete_node_o1(self, node):
        """O(1)时间复杂度删除指定结点."""
        if node.next is None or node.next.next is None:
            # 正常从头查找删除, 平均时间复杂度还是O(1)
            pass

        next_node = node.next
        node.item = next_node.item
        node.next = next_node.next
        del next_node

    def reverse_by_loop(self):
        """用循环的方式翻转链表.

        需要借助三个指针: pre, this, next.
        """
        if self.head is None or self.head.next is None:
            return

        # 初始
        ptr_pre = None
        ptr_this = self.head

        # 翻转
        while ptr_this is not None:
            ptr_next = ptr_this.next  # 下一个待处理结点
            ptr_this.next = ptr_pre  # 当前结点指向前一个结点, 局部翻转
            ptr_pre = ptr_this  # pre_node向前移动
            ptr_this = ptr_next  # this_node向前移动, 指向待处理结点

        self.head = ptr_pre

    def reverse_by_recursion(self):
        # 第二个条件使递归进栈结束
        if self.head is None or self.head.next is None:
            return

        # 将head之外的结点作为新链表递归
        # 实际会移动new_list.head到最后一个结点,
        # 而self.head为倒数第二个结点
        new_list = SingleLinkedList()
        new_list.head = self.head.next
        new_list.reverse_by_recursion()

        # 下面两行实现新链表的翻转
        self.head.next.next = self.head  # 将原链表的head加入新链表尾部(已被翻转)
        self.head.next = None  # 原链表的head指向null, 即新链表尾结点指向null

        self.head = new_list.head  # new_list.head是原链表的尾结点

    # @classmethod
    # def reverse_by_recursion(cls, head):
    #     # self.head指向最后一个结点时递归进栈结束
    #     if head is None or head.next is None:
    #         return head
    #
    #     # 向前移动head到最后一个结点
    #     new_head = cls.reverse_by_recursion(head.next)
    #
    #     head.next.next = head
    #     head.next = None
    #     return new_head

    def get_last_node(self, k=1):
        if self.head is None:
            return

        ptr_fast = self.head
        ptr_slow = self.head

        for i in range(k-1):
            if ptr_fast.next is None:
                return
            ptr_fast = ptr_fast.next

        while ptr_fast.next is not None:
            ptr_fast = ptr_fast.next
            ptr_slow = ptr_slow.next

        return ptr_slow

    def middle_node(self):
        if self.head is None:
            return

        if self.head.next is None:
            return self.head

        ptr_fast = self.head
        ptr_slow = self.head

        # 如果要求在链表长度为偶数的情况下，返回中间两个节点的第一个，可以用下面的循环条件
        # while (fast && fast->next != NULL && fast->next->next != NULL)
        while ptr_fast is not None and ptr_fast.next is not None:
            ptr_fast = ptr_fast.next.next
            ptr_slow = ptr_slow.next

        return ptr_slow

    @staticmethod
    def merge_list(list1, list2):
        if list1.next is None and list2.next is None:
            return
        elif list1.next is None:
            return list2
        elif list2.next is None:
            return list1

        head = Node()
        ptr = head

        while list1.next is not None and list2.next is not None:
            if list1.item < list2.item:
                ptr.next = list1
                list1 = list1.next
            else:
                ptr.next = list2
                list2 = list2.next

            ptr = ptr.next

        # key
        if list1.next is not None:
            ptr.next = list1
        if list2.next is not None:
            ptr.next = list2

        new_list = SingleLinkedList()
        new_list.head = head.next

        return new_list

    def has_ring(self):
        ptr_fast = self.head
        ptr_low = self.head
        while ptr_fast is not None and ptr_fast.next is not None:
            ptr_fast = ptr_fast.next.next
            ptr_low = ptr_low.next
            if ptr_fast == ptr_low:
                return True

        return False

    @staticmethod
    def is_intersect(list1, list2):
        """相交, 则在某个结点之后两个链表是一样的, 不会分叉,
        因为分叉结点的next不唯一, 不满足链表定义.
        """
        last_node_1 = list1.get_last_node()
        last_node_1.next = list2.head
        value = list1.has_ring()
        last_node_1.next = None
        return value

    @staticmethod
    def is_intersect_on(list1, list2):
        """相交O(n1+n2)的解法: 尾指针是同一个结点."""
        last_node_1 = list1.get_last_node()
        last_node_2 = list2.get_last_node()
        return last_node_1 is last_node_2


if __name__ == '__main__':
    # slist = SingleLinkedList()
    # slist.creat_by_insert_tail([1, 2, 3])
    # slist.insert_to_head(4)

    # rev = reverse_by_recursion(slist.head)
    # node = rev
    # while node is not None:
    #     print(node.item)
    #     node = node.next
    #
    # slist.reverse_by_recursion()

    # merge
    # slist1 = SingleLinkedList()
    # slist1.creat_by_insert_tail([1, 2, 4])
    # slist2 = SingleLinkedList()
    # slist2.creat_by_insert_tail([1, 3, 4])
    # slist = SingleLinkedList.merge_list(slist1.head, slist2.head)
    # slist.print_list()

    # middle
    # n1 = slist1.middle_node()

    # ring
    # slist = SingleLinkedList()
    # slist.creat_by_insert_tail([[0, 1], 2, 3])
    # print(slist.has_ring())
    # last = slist.get_last_node()
    # last_2nd = slist.get_last_node(2)
    # last.next = last_2nd
    # print(slist.has_ring())

    # intersect
    slist1 = SingleLinkedList()
    slist1.creat_by_insert_tail([x for x in range(3)][::-1])
    slist2 = SingleLinkedList()
    slist2.creat_by_insert_tail([5, 4, 3])
    slist2.get_last_node().next = slist1.head
    print(SingleLinkedList.is_intersect(slist1, slist2))
    print(SingleLinkedList.is_intersect_on(slist1, slist2))
