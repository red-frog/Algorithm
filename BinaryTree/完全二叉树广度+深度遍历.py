# -*- coding:utf-8 -*-


# 定义节点类
import queue


class Node(object):
    def __init__(self, data):
        # 定义数据域
        self.data = data
        # 定义指针域
        # 定义左右孩子节点
        self.left_child = None
        self.right_child = None


class BinaryTree(object):
    def __init__(self):
        self.__root = None

    def add(self, data):
        # 定义个队列存储节点
        asis_queue = queue.Queue()
        # 定义新节点
        new_node = Node(data)
        # 判断根节点是否为空
        if self.__root is None:
            self.__root = new_node
        else:
            asis_queue.put(self.__root)
        while not asis_queue.empty():
            cur = asis_queue.get()
            if cur.left_child is None:
                cur.left_child = new_node
                return
            else:
                asis_queue.put(cur.left_child)
            if cur.right_child is None:
                cur.right_child = new_node
                return
            else:
                asis_queue.put(cur.right_child)

    def travel(self):
        if self.__root is None:
            return
        else:
            # 定义个队列
            asis_queue = queue.Queue()
            # 将根节点放入队列
            asis_queue.put(self.__root)
            while not asis_queue.empty():
                # 取出根结点
                cur = asis_queue.get()
                # 打印数据
                print(cur.data, end=" ")
                if cur.left_child is None:
                    pass
                else:
                    asis_queue.put(cur.left_child)
                if cur.right_child is None:
                    pass
                else:
                    asis_queue.put(cur.right_child)
            else:
                print(" ")

    def get(self):
        # 返回根节点
        return self.__root

    def front_travel(self, tree):
        # 先序遍历，根，左，右
        if tree is None:
            # 判断节点是否为空，若为空则返回
            return
        print(tree.data, end=" ")
        self.front_travel(tree.left_child)
        self.front_travel(tree.right_child)

    def mid_travel(self, tree):
        # 中序遍历，先左，再根，再右
        if tree is None:
            return
        self.mid_travel(tree.left_child)
        print(tree.data, end=" ")
        self.mid_travel(tree.right_child)

    def back_travel(self, tree):
        # 后序遍历，先左右，后根
        if tree is None:
            return
        self.back_travel(tree.left_child)
        self.back_travel(tree.right_child)
        print(tree.data, end=" ")

if __name__ == "__main__":
    bt = BinaryTree()
    for i in range(10):
        bt.add(i)
    bt.travel()
    bt.front_travel(bt.get())
    print(" ")
    bt.mid_travel(bt.get())
    print(" ")
    bt.back_travel(bt.get())