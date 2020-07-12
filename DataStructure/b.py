def insertion_sort(lists):
    n = len(lists)
    for index in range(1, n):
        current_value = lists[index]
        position = index

        while position > 0 and lists[position - 1] > current_value:
            lists[position] = lists[position - 1]
            position -= 1

        lists[position] = current_value


lists = [1, 6, 7, 5, 6, 11, 15, 10]
insertion_sort(lists)
print(lists)
