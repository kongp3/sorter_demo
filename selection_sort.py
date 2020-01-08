# -*- coding: utf-8 -*-


def selectionSort(array):
    for i in range(0, len(array)):
        min_num_index = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_num_index]:
                min_num_index = j

        temp = array[i]
        array[i] = array[min_num_index]
        array[min_num_index] = temp
    return array


if __name__ == '__main__':
    ll = [3, 38, 44, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print selectionSort(ll)
