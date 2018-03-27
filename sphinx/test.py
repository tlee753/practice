class Sorter():
    """
    this is a class called Sorter
    """

    def __init__(self, array):
        self.array = array

    def sort(self):
        sortHelper(0, self.array)
        """ this is a test comment"""

    def sortHelper(i, array):
        if (i == len(array) - 1):
            return

        sortHelper(i + 1, array)
        # what will happen to me now
        sorted = False
        while (not sorted and not(i == len(array) - 1)):
            if (array[i] < array[i + 1]):
                sorted = True
            else:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                i += 1


if __name__ == "__main__":
    sort = Sorter([3, 2, 1])
    sort.sort()
    print(sort.array)