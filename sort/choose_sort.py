# -*- coding:utf-8 -*-


def select_sort(alist):
    length = len(alist)
    for i in range(length-1):
        for j in range(i+1, length):
            if alist[i] > alist[j]:
                alist[i], alist[j] = alist[j], alist[i]
                # print(alist)
            else:
                pass
    print(alist)


if __name__ == "__main__":
    list = [15, 1, 2, 2, 5]
    select_sort(list)