# -*- coding: utf-8 -*-
def insertion_sort(array):
    for i in range(1, len(array)):
        pre_index = i - 1
        current = array[i]
        while pre_index >= 0 and array[pre_index] > current:
            array[pre_index+1] = array[pre_index]
            pre_index -= 1
        array[pre_index+1] = current
    return array


if __name__ == '__main__':
    ll = [3, 38, 44, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print insertion_sort(ll)
