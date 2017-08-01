# -*- coding:utf-8 -*-


# 定义归并排序方法
def merge_sort(alist):
    # 设置递归终止条件
    if len(alist) == 1:
        return alist
    # 拆分序列
    mid_index = len(alist)//2
    left = merge_sort(alist[:mid_index])
    right = merge_sort(alist[mid_index:])
    # 合并两个子序列
    # 定义两个游标分别指向两个序列起始位置
    new_list = []
    left_index = right_index = 0
    # 用or行不行
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            new_list.append(left[left_index])
            left_index += 1
        else:
            new_list.append(right[right_index])
            right_index += 1
    else:
        # 处理序列中剩余数据
        # if left_index < len(left):
        #     new_list += left[left_index:]
        # else:
        #     pass
        # if right_index < len(right_index):
        #     new_list += right[right_index]
        # else:
        #     pass
        new_list += left[left_index:]
        new_list += right[right_index:]
    return new_list

# 最优最坏时间复杂度：logn(拆分过程:1+2+3+...logn  和为2logn-1）
#             合并次数：logn(n)
#              nlogn + 2logn-1    ---->O(nlogn)
# 稳定性：人为控制(稳定)

if __name__ == "__main__":
    alist = [23, 44, 55, 12, 12, 12, 99, 33, 20]
    result = merge_sort(alist)
    print(result)