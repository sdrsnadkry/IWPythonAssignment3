def quick_sort(lists, first, last):
    if first < last:
        p = partition(lists, first, last)

        quick_sort(lists, first, p - 1)
        quick_sort(lists, p + 1, last)


def partition(lists, first, last):
    pivot = lists[first]
    i = first + 1
    j = last

    while i < j:
        while lists[i] < pivot:
            i = i + 1
        while lists[j] > pivot:
            j = j - 1
        if i < j:
            lists[i], lists[j] = lists[j], lists[i]

    lists[first], lists[j] = lists[j], lists[first]

    return j


lists = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(lists, 0, len(lists) - 1)
print(lists)
