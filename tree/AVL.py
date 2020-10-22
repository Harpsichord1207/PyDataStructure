# https://andrewpqc.github.io/2018/01/09/binary-search-tree-avl/
# https://www.cs.usfca.edu/~galles/visualization/AVLtree.html
import copy

from tree.binary_search_tree import BinarySearchTree


class AVL(BinarySearchTree):

    @classmethod
    def get_height(cls, node, _type):
        if node is None:
            return 0
        if _type == 'left':
            if node.l_child is None:
                return 1
            return 1 + cls.get_height(node.l_child, 'left')
        else:
            if node.r_child is None:
                return 1
            return 1 + cls.get_height(node.r_child, 'right')

    # 获取平衡因子
    @classmethod
    def get_bf(cls, node):
        if node is None:
            return 0
        return cls.get_height(node, 'left') - cls.get_height(node, 'right')

    @classmethod
    def rotate(cls, node):
        pass

    # 右旋
    @classmethod
    def rotate_ll(cls, node):
        new_node = node.l_child
        node.l_child = new_node.r_child
        new_node.r_child = node
        return new_node

    # 左旋
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


if __name__ == '__main__':
    pass
