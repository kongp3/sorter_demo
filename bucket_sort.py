# -*- coding: utf-8 -*-


def bucket_sort(array):
    # 好烂的一个基数排序
    fn_bucket = list()
    ret_array = list()

    for j in range(0, 5):
        tmp_bucket = list()
        for i in range(0, 10):
            tmp_bucket.append([])
        for i in range(0, len(array)):
            tmp_bucket[array[i]/ (10 ** j) % 10].append(array[i])

        if len(tmp_bucket[0]) == len(array):
            break
        else:
            fn_bucket = tmp_bucket
    for item in fn_bucket:
        for i in range(1, len(item)):
            for j in range(0, len(item)-i):
                if item[j] > item[j+1]:
                    item[j], item[j+1] = item[j+1], item[j]
        ret_array += item
    return ret_array


if __name__ == '__main__':
    ll = [3, 38, 44, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]
    print bucket_sort(ll)
