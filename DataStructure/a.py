def bubble_sort(lists):
    n = len(lists)

    for i in range(n - 1, 0, -1):
        for j in range(0, i):
            if lists[j] > lists[j + 1]:
                temp = lists[j]
                lists[j] = lists[j + 1]
                lists[j + 1] = temp


lists = [12, 15, 9, 24, 1, 6, 55, 18, 11, 0, 2]
bubble_sort(lists)

print(lists)


