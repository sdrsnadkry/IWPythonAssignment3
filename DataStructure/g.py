def interpolation_search(lists, n, item):
    low = 0
    high = n - 1

    while low <= high and lists[low] <= item <= lists[high]:
        index = low + int(((float(high - low) / (lists[high] - lists[low])) * (item - lists[low])))

        if lists[index] == item:
            return index

        if lists[index] < item:
            low = index + 1

        else:
            high = index - 1

    return False


lists = [5, 10, 12, 15, 25, 45, 65, 85, 87, 95]
item = 45
result = interpolation_search(lists, len(lists), item)

if result:
    print("Element found at index ", result)
else:
    print("Element not found")
