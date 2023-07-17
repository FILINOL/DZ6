def find_indexes(arr, min_val, max_val):
    indexes = []
    for i in range(len(arr)):
        if min_val <= arr[i] <= max_val:
            indexes.append(i)
    return indexes

array = [1, 3, 5, 2, 4, 6, 8, 7, 9, 10]
minimum = 2
maximum = 8
result = find_indexes(array, minimum, maximum)
print(result)