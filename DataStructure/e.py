def linear_search(lists, item):
    found = False
    index = -1
    for i in range(len(lists)):
        if lists[i] == item:
            found = True
            index = i

    if found:
        print('Found at index ' + str(index))
    else:
        print('Not Found')


lists = [1, 2, 8, 55, 56, 15, 75, 100, 105, 150]
item = 100
linear_search(lists, item)
