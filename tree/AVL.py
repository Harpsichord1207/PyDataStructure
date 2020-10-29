# https://andrewpqc.github.io/2018/01/09/binary-search-tree-avl/
# https://www.cs.usfca.edu/~galles/visualization/AVLtree.html

from tree.binary_search_tree import BinarySearchTree, Node


class AVL(BinarySearchTree):

    @classmethod
    def get_child_height(cls, node, _type):
        if node is None:
            return 0
        if _type == 'left':
            if node.l_child is None:
                return 1
            return 1 + cls.get_child_height(node.l_child, 'left')
        else:
            if node.r_child is None:
                return 1
            return 1 + cls.get_child_height(node.r_child, 'right')

    # 获取平衡因子
    def get_bf(self):
        if self.root is None:
            return 0
        return self.get_child_height(self.root, 'left') - self.get_child_height(self.root, 'right')

    # 左左 右旋
    @classmethod
    def rotate_ll(cls, node):
        new_node = node.l_child
        node.l_child = new_node.r_child
        new_node.r_child = node
        return new_node

    # 右右 左旋
    @classmethod
    def rotate_rr(cls, node):
        new_node = node.r_child
        node.r_child = new_node.l_child
        new_node.l_child = node
        return new_node

    # 右左旋
    @classmethod
    def rotate_lr(cls, node):
        node.r_child = cls.rotate_ll(node.r_child)
        return cls.rotate_rr(node)

    # 左右旋
    @classmethod
    def rotate_rl(cls, node):
        node.l_child = cls.rotate_rr(node.l_child)
        return cls.rotate_ll(node)

    @classmethod
    def _insert(cls, node, value):
        if node is None:
            node = Node(value)
        elif value == node.value:
            pass
        elif value < node.value:
            node.l_child = cls._insert(node.l_child, value)
            if cls._get_height(node.l_child) - cls._get_height(node.r_child) >= 2:
                if value < node.l_child.value:
                    node = cls.rotate_ll(node)
                else:
                    node = cls.rotate_rl(node)
        else:
            node.r_child = cls._insert(node.r_child, value)
            if cls._get_height(node.r_child) - cls._get_height(node.l_child) >= 2:
                if value > node.r_child.value:
                    node = cls.rotate_rr(node)
                else:
                    node = cls.rotate_lr(node)
        return node

    @classmethod
    def _delete(cls, node, value):
        if node is None:
            return
        if node.value == value:
            if node.l_child is None:
                return node.r_child
            elif node.r_child is None:
                return node.l_child
            else:
                # 需要删除的node 其左子树比右子树高
                if cls._get_height(node.l_child) > cls._get_height(node.r_child):
                    # 找到左子树里的最大node并删除
                    _max_l_value = cls._max(node.l_child)
                    node = cls._delete(node, _max_l_value)
                    # 将删除的node的值赋予当前node
                else:
                    _min_r_value = cls._min(node.r_child)
                    node = cls._delete(node, _min_r_value)
                    node.value = _min_r_value
        elif node.value > value:
            node.l_child = cls._delete(node.l_child, value)
            if cls._get_height(node.r_child) - cls._get_height(node.l_child) >= 2:
                if cls._get_height(node.r_child.l_child) < cls._get_height(node.r_child.r_child):
                    node = cls.rotate_rr(node)
                else:
                    node = cls.rotate_lr(node)
        else:
            node.r_child = cls._delete(node.r_child, value)
            if cls._get_height(node.l_child) - cls._get_height(node.r_child) >= 2:
                if cls._get_height(node.l_child.l_child) < cls._get_height(node.l_child.r_child):
                    node = cls.rotate_rl(node)
                else:
                    node = cls.rotate_ll(node)
        return node


if __name__ == '__main__':

    avl = AVL([1, 2, 3, 4, 5, 6, 7, 8])
    print(avl.get_bf())
    print(avl.root)
    avl.delete(5)
    print(avl.get_bf())
    print(avl.root)
    # avl.root = avl.rotate_rr(avl.root)
    # print(avl.get_bf())
