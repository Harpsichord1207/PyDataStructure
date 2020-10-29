class Node:

    def __init__(self, value=0, _next=None):
        self.value = value
        self.next = _next

    def __str__(self):
        return '{}->{}'.format(self.value, self.next)


class SinglyLinkedList:

    def __init__(self, array=None):
        self.root = None
        if array is not None:
            for a in array:
                self.add_node(a)

    @classmethod
    def _add_node(cls, node, value):
        if node is None:
            return Node(value)
        else:
            node.next = cls._add_node(node.next, value)
        return node

    def add_node(self, value):
        self.root = self._add_node(self.root, value)

    def __str__(self):
        assert not self.has_circle(), 'current linked list has circle'
        return 'SinglyLinkedList: {}'.format(self.root)

    # 单链表反转
    @classmethod
    def _reverse(cls, node):
        pre = node
        curr = node.next
        pre.next = None
        while curr:
            tmp = curr.next
            curr.next = pre
            pre = curr
            curr = tmp
        return pre

    def reverse(self):
        self.root = self._reverse(self.root)

    def has_circle(self):
        slow = self.root
        fast = self.root
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == '__main__':
    n1 = Node(3)
    n2 = Node(5)
    n1.next = n2
    print(n1)

    sll = SinglyLinkedList([1, 3, 5, 7, 9])
    print(sll)
    sll.reverse()
    print(sll)

    sll.root.next.next.next.next.next = sll.root
    print(sll)
