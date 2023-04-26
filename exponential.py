
# print(names) #is a list of food items [strawberry,biryani,....]
# print(randomlist) #our list that we use in exponential searching. (checks the availibility of the item)


class Search:
    def __init__(self, names, user, index):
        self.user = user
        self.names = names
        # gives the key to be searched for exponential search algo
        self.index = index

    def binarySearch(self, randomlist, l, r, index):
        if r >= l:
            mid = l + (r-l) // 2

            # If the element is present at
            # the middle itself
            if randomlist[mid] == index:
                return mid

            # If the element is smaller than mid,
            # then it can only be present in the
            # left subarray of the randomlist
            if randomlist[mid] > index:
                return self.binarySearch(randomlist, l, mid - 1, index)

            # Else he element can only be
            # present in the right of the randomlist
            return self.binarySearch(randomlist, mid + 1, r, index)
            # We reach here if the element is not present
        return -1

    # Returns the position of first
    # occurrence of x in list
    def exponentialSearch(self, randomlist, n, index):
        # IF x is present at first
        # location itself
        if randomlist[0] == index:
            return 0

        # Find range for binary search
        # j by repeated doubling
        i = 1
        while i < n and randomlist[i] <= index:
            i = i * 2

        # Call binary search for the found range
        return self.binarySearch(randomlist, i // 2, min(i, n-1), index)
