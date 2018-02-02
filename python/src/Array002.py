import collections


def main(num):

    arr = collections.OrderedDict()
    ret = []
    for i in num:
        bin_count = bin(i).count('1')
        if arr.get(bin_count) is None:
            arr[bin_count] = []
        arr[bin_count].append(i)

    for i in num:
        bin_count = bin(i).count('1')
        arr[bin_count] = sorted(arr[bin_count])

    for item in arr.values():
        for ch in item:
            ret.append(ch)

    print(ret)

    return ret


n = [5, 3, 7, 10]
main(n)
