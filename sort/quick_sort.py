# -*- coding:utf-8 -*-


# 定义快速排序方法
def quick_sort(alist, start=None, end=None):
    # 核心，查找基准元素位置
    if start is None and end is None:
        # 　１、保存基准元素，当前序列的第一个元素
        start = 0
        end = len(alist) - 1

    # 递归的终止条件
    if start >= end:
        return
    # 基准变量必须放在先判断递归条件后面，因为如果start>end,3会出现越界的问题。
    base_value = alist[start]
    # 定义两个游标
    left = start
    right = end
    while left < right:
        # 移动右边的游标直至遇到比基准元素小的元素，把当前元素移到左边
        while right > left:
            # 为什么要加上等于号，为了稳定等于的话不会换位置，会继续移动
            if alist[right] >= base_value:
                right -= 1
            else:
                # "把当前元素交换到右边"
                alist[left], alist[right] = alist[right], alist[left]
                # print(alist)
                break
        # 移动左边游标
        while left < right:
            # 加上等于号的目的得注意
            if alist[left] <= base_value:
                left += 1
            else:
                # 把当前元素交换到左边
                alist[right], alist[left] = alist[left], alist[right]
                break
        # print(alist)
    else:
        # 在当前位置保留基准元素
        alist[left] = base_value
    # 处理左边序列
    quick_sort(alist, start, left - 1)
    # 处理右边序列
    quick_sort(alist, right + 1, end)
# 最优时间复杂度：logn*(n-1)   logn是次数。。重新听

if __name__ == "__main__":
    list = [23, 44, 55, 12, 21, 67, 99, 33, 20]
    # print(list)
    quick_sort(list)
    print(list)
