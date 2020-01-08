# -*- coding: utf-8 -*-


def hill_sort(array, step=None):
    if not step:
        step = len(array)

    gap = len(array) / step
    while gap > 0:
        for i in range(gap, len(array)):
            pre_index = i - gap
            current = array[i]

            while pre_index >= 0 and array[pre_index] > current:
                array[pre_index+gap] = array[pre_index]
                pre_index -= gap
            array[pre_index+gap] = current

        gap /= step
    return array


if __name__ == '__main__':
    ll = [3, 38, 44, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print hill_sort(ll, 2)
