# -*- coding: utf-8 -*-


def quick_sort(array):
    # 传入 数组 和 左右边界下标
    return q_sort(array, 0, len(array)-1)


def q_sort(array, l, r):
    if l < r:
        # 确认基准值的下标
        p_index = patition(array, l, r)
        q_sort(array, l, p_index-1)
        q_sort(array, p_index+1, r)
    return array


def patition(array, l, r):
    p_value = array[l]

    while l < r:
        while l < r and array[r] >= p_value:
            r -= 1
        else:
            array[l] = array[r]

        while l < r and array[l] <= p_value:
            l += 1
        else:
            array[r] = array[l]
    array[l] = p_value
    return l


if __name__ == '__main__':
    ll = [3, 38, 44, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print quick_sort(ll)
