# -*- coding:utf-8 -*-


def bubble_sort(alist):
    length = len(alist)
    # 控制比较序列长度
    for j in range(length, 1, -1):
        flag = True
        for i in range(j-1):
            if alist[i] > alist[i+1]:
                # 交换位置
                alist[i], alist[i+1] = alist[i+1], alist[i]
                print(alist)
                flag = False
            else:
                pass
        else:
            if flag:
                return
    print(alist)


if __name__ == "__main__":
    list = [15, 1, 2, 3, 4]
    bubble_sort(list)