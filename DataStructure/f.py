def binary_search(lists, item):
    first = 0
    last = len(lists) - 1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if lists[mid] == item:
            found = lists.index(item)
        else:
            if item < lists[mid]:
                last = mid - 1
            else:
                first = mid + 1

    return found


result = binary_search([1, 2, 3, 4, 5, 6, 7, 8], 5)

if result:
    print('Item found at index ', result)
else:
    print('Item not found')
