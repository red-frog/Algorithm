# -*- coding:utf-8 -*-


def binary_search(alist, data):
    # 计算中间的下标
    start_index = 0
    end_index = len(alist) - 1
    while start_index <= end_index:
        # mid_index = (end_index - start_index)//2
        # 不能用减法，必须用加法，如3和7
        mid_index = (end_index + start_index) // 2
        if alist[mid_index] == data:
            print("找到了")
            print(alist[mid_index])
            return
        elif alist[mid_index] > data:
            # 证明在列表左侧
            # 更新结束下标
            # end_index = mid_index-1
            alist = alist[:mid_index]
            return binary_search(alist, data)
        else:
            # alist[mid_index] < data
            # 更新开始下标

            # start_index = mid_index + 1
            alist = alist[mid_index+1:]
            return binary_search(alist, data)
    else:
        print("没有此元素")

if __name__ == "__main__":
    list = [11, 12, 14, 16, 17, 18]
    binary_search(list, 16)
    binary_search(list, 15)
    binary_search(list, 18)