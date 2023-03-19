def selectionSort(array):

    for i in range(len(array)):
        min_index = i

        for j in range(i + 1, len(array)):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])


array = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
selectionSort(array)
print('The array after sorting in Ascending Order by selection sort is:')
print(array)

# complexity of O(n^2)