arr = [3, 9, 2, 7, 8, 1, 6, 4, 5]

def sort(array):
    sortHelper(0, array)

def sortHelper(i, array):
    if (i == len(array) - 1):
        return

    sortHelper(i + 1, array)

    sorted = False
    while (not sorted and not(i == len(array) - 1)):
        if (array[i] < array[i + 1]):
            sorted = True
        else:
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp
            i += 1


sort(arr)
print(arr)