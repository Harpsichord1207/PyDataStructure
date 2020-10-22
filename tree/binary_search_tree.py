class Node:

    def __init__(self, value, l_child=None, r_child=None):
        self.value = value
        self.l_child = l_child
        self.r_child = r_child

        # self.count = 1  # can be used to handle duplicates

    def __str__(self, level=0):
        ret = "\t" * level + repr(self.value)
        if self.r_child is not None:
            ret = ret + self.r_child.__str__(level + 1)

        if self.l_child is not None:
            ret = self.l_child.__str__(level + 1) + ret
        ret += "\n"
        return ret


class BinarySearchTree:

    def __init__(self, array=None):
        self.root = None
        if array is not None:
            for value in array:
                self.insert(value)

    @classmethod
    def _query(cls, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        if node.value > value:
            return cls._query(node.l_child, value)
        else:
            return cls._query(node.r_child, value)

    def query(self, value):
        return self._query(self.root, value)

    @classmethod
    def _traversals(cls, node, _type='in'):
        if node is None:
            return
        if _type == 'in':
            yield from cls._traversals(node.l_child, 'in')
            yield node.value
            yield from cls._traversals(node.r_child, 'in')
        elif _type == 'pre':
            yield node.value
            yield from cls._traversals(node.l_child, 'pre')
            yield from cls._traversals(node.r_child, 'pre')
        elif _type == 'post':
            yield from cls._traversals(node.l_child, 'post')
            yield from cls._traversals(node.r_child, 'post')
            yield node.value

    def to_list(self, _type='in'):
        return [v for v in self._traversals(self.root, _type)]

    @classmethod
    def _insert(cls, node, value):
        if node is None:
            node = Node(value)
        elif value == node.value:
            # node.count += 1
            pass
        elif value > node.value:
            node.r_child = cls._insert(node.r_child, value)
        else:
            node.l_child = cls._insert(node.l_child, value)
        return node

    def insert(self, value):
        self.root = self._insert(self.root, value)

    @classmethod
    def _min(cls, node):
        if node.l_child:
            return cls._min(node.l_child)
        return node.value

    @classmethod
    def _max(cls, node):
        if node.r_child:
            return cls._max(node.r_child)
        return node.value

    @classmethod
    def _delete(cls, node, value):
        if node is None:
            return
        if node.value < value:
            node.r_child = cls._delete(node.r_child, value)
        elif node.value > value:
            node.l_child = cls._delete(node.l_child, value)
        if node.value == value:
            if node.l_child and node.r_child:
                min_value_r_child = cls._min(node.r_child)
                node.value = min_value_r_child
                node.r_child = cls._delete(node.r_child, min_value_r_child)
            elif node.l_child is None and node.r_child is None:
                node = None
            elif node.l_child is None:
                node = node.r_child
            else:
                node = node.l_child
        return node

    def delete(self, value):
        self.root = self._delete(self.root, value)


if __name__ == '__main__':
    bst = BinarySearchTree([3, 2, 5, 4, 8, 7, 9, 1, 2])
    print(bst.root)
    print(bst.to_list())
    print(bst.query(6))
    print(bst.query(5))
    bst.delete(5)
    print(bst.to_list())
