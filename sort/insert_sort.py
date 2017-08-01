# -*- coding:utf-8 -*-


# 定义方法
def insert_sort(alist):
    # 核心部分：把整个序列看成两部分
    # for j in range():
        # 计算序列长度
    length = len(alist)
    # 从无序序列中取数据
    for i in range(1, length):
        # 把取出数据插入
        for x in range(i-1, -1, -1):
            if alist[i] < alist[x]:
                # 交换数据
                alist[i], alist[x] = alist[x], alist[i]
                # 更新下标
                i = x
            else:
                break


if __name__ == "__main__":
    alist = [11, 22, 34, 2, 5]
    insert_sort(alist)
    print(alist)