def merge_sort(lists):
    if len(lists) > 1:
        mid = len(lists) // 2
        left_lists = lists[:mid]
        right_lists = lists[mid:]

        merge_sort(left_lists)
        merge_sort(right_lists)
        i = j = k = 0

        while i < len(left_lists) and j < len(right_lists):
            if left_lists[i] < right_lists[j]:
                lists[k] = left_lists[i]
                i = i + 1
            else:
                lists[k] = right_lists[j]
                j = j + 1
            k = k + 1

        # for remaining elements in lists
        while i < len(left_lists):
            lists[k] = left_lists[i]
            i = i + 1
            k = k + 1

        while j < len(right_lists):
            lists[k] = right_lists[j]
            j = j + 1
            k = k + 1


lists = [1, 5, 14, 65, 45, 75, 12, 35, 45, 75, 15, 25, 6, 4, 3, 88, 101]
merge_sort(lists)
print(lists)
