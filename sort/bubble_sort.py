# -*- coding:utf-8 -*-


def bubble_sort(alist):
    length = len(alist)
    # 控制比较序列长度
    for j in range(length, 1, -1):
        for i in range(j-1):
            if alist[i] > alist[i+1]:
                # 交换位置，将大的放在后面
                alist[i], alist[i+1] = alist[i+1], alist[i]
            else:
                pass
    print(alist)


if __name__ == "__main__":
    list = [12, 132, 143, 1, 10, 23]
    bubble_sort(list)