# -*- coding: utf-8 -*-


def qs_blind(array):
    return qs_package(array, 0, len(array)-1)


def qs_package(array, l, r):
    if l < r:
        p_index = patition(array, l, r)

        qs_package(array, l, p_index-1)
        qs_package(array, p_index+1, r)

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
    print qs_blind(ll)
