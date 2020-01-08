# -*- coding: utf-8 -*-
def bubble_sort(array):
    for i in range(1, len(array)):
        for j in range(0, len(array)-i):
            if array[j] > array[j+1]:
                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp
    return array


def bb2(array):
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1-i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array


if __name__ == '__main__':
    import time
    ll = [3, 38, 44, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    start = time.time()
    print bubble_sort(ll)
    end = time.time()
    a = end - start

    start = time.time()
    print bb2(ll)
    end = time.time()
    b = end - start

    print a > b
