# -*- coding: utf-8 -*-


def hill_sort(array, step=2):
    n = len(array)
    gap = int(n / step)

    while gap > 0:
        for i in range(gap, len(array)):
            pre_index = i - gap
            current = array[i]

            while pre_index >= 0 and array[pre_index] > current:
                array[pre_index+gap] = array[pre_index]
                pre_index -= gap
            array[pre_index+gap] = current
        gap = int(gap / step)
    return array


def shellSort(array):
    n = len(array)
    gap = int(n / 2)

    while gap > 0:

        for i in range(gap, n):

            current = array[i]
            j = i
            while j >= gap and array[j - gap] > current:
                array[j] = array[j - gap]
                j -= gap
            array[j] = current
        gap = int(gap / 2)
    return array


if __name__ == '__main__':
    ll = [3, 38, 44, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print hill_sort(ll)
