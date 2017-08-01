# -*- coding:utf-8 -*-


# 希尔排序
def shell_sort(alist):
    # gap取值
    gap = 4
    # 计算序列长度
    length = len(alist)
    while gap > 0:
        # 通过gap分割序列，对每个子序列进行插入排序
        for j in range(0, gap, 1):
            #
            for i in range(j+gap, length, gap):
                # 从无序序列中取一个元素插入到前面的有序序列中
                while i >= gap:
                    if alist[i - gap] > alist[i]:
                        alist[i], alist[i-gap] = alist[i-gap], alist[i]
                        i -= gap
                        # print(alist)
                    else:
                        # print('这块')
                        return
                # print("不对")

        print("更换gap")
        gap = gap//2

if __name__ == "__main__":
    list = [7, 1, 8, 21, 5, 12, 56, 14]
    shell_sort(list)
    print(list)