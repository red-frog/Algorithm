# -*- coding:utf-8 -*-
from queue import Queue


class Node(object):
    def __init__(self, data):
        # 定义数据域
        self.data = data
        # 定义左孩子
        self.left_child = None
        # 定义右孩子
        self.right_child = None


class BinaryTree(object):
    def __init__(self):
        # 　构造空的二叉树
        self.__root = None

    def add(self, data):
        # 创造新节点
        new_node = Node(data)
        # 添加完成以后保证二叉树满足完全二叉树
        # 　需要队列辅助
        assis_queue = Queue()
        if self.__root is None:
            # 则让根指向新节点
            self.__root = new_node
        else:
            # 根有值，把根放入队列
            assis_queue.put(self.__root)
        # 查找要插入的位置
        while not assis_queue.empty():
            # 获取节点
            cur = assis_queue.get()
            if cur.left_child is None:
                cur.left_child = new_node
                return
            else:
                # 左孩子不为空，加入队列
                assis_queue.put(cur.left_child)
            if cur.right_child is None:
                cur.right_child = new_node
                return
            else:
                # 右孩子不为空，加入队列
                assis_queue.put(cur.right_child)

    def travel(self):
        # 广度遍历
        if self.__root is None:
            return
        else:
            # 定义辅助队列
            asis_queue = Queue()
            # 放入根节点值
            asis_queue.put(self.__root)
            while not asis_queue.empty():
                # 取值
                cur = asis_queue.get()
                print(cur.data, end=" ")
                if cur.left_child is None:
                    pass
                else:
                    # 将左孩子节点放入队列
                    asis_queue.put(cur.left_child)
                if cur.right_child is None:
                    pass
                else:
                    asis_queue.put(cur.right_child)
            else:
                print(" ")


if __name__ == "__main__":
    bt = BinaryTree()

    for i in range(10):
        bt.add(i)

    bt.travel()