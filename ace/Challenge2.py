# https://www.educative.io/module/lesson/data-structures-in-python/B137p8P75QW

# Problem Statement #
# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list.
# Name it merge_lists(lst1, lst2).
#
# Input #
# Two sorted lists.
#
# Output #
# A merged and sorted list consisting of all elements of both input lists.
#
# Sample Input #
# list1 = [1,3,4,5]
# list2 = [2,6,7,8]
# Sample Output #
# arr = [1,2,3,4,5,6,7,8]

# https://www.geeksforgeeks.org/python-list-sort/
# reverse, key
#
# https://www.geeksforgeeks.org/python-combining-two-sorted-lists/
# sorted()
# heapq.merge

class Challenge:
    def __init__(self):
        self.lst1 = [1,3,4,5]
        self.lst2 = [2,6,7,8]


    def merge_lists(self):
        ind1 = 0
        ind2 = 0
        while (ind1 < len(self.lst1) and ind2 < len(self.lst2)):
            if (self.lst1[ind1] > self.lst2[ind2]):
                self.lst1.insert(ind1, self.lst2[ind2])
                ind1 += 1
                ind2 += 1
            else:
                ind1 += 1

        if (ind2 < len(self.lst2)):
            self.lst1.extend(self.lst2[ind2:])
        return self.lst1

    def show(self):
        print(self.lst1)

    def run(self):
        self.merge_lists()
        self.show()
