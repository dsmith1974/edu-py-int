# Problem Statement #
# Implement a function right_rotate(lst, k) which will rotate the given list by k. This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.
#
# Input #
# A list and a positive number by which to rotate that list
#
# Output: #
# The given list rotated by k elements
#
# Sample Input #
# lst = [10,20,30,40,50]
# n = 3
# Sample Output #
# lst = [30,40,50,10,20]

# https://stackoverflow.com/questions/509211/understanding-slice-notation

class Challenge:
    def __init__(self):
        self.arr = [10,20,30,40,50]

    def right_rotate(self, lst, k):
        k = 0 if len(lst) == 0 else k % len(lst)
        return lst[-k:] + lst[:-k]

    def show(self):
        print(self.right_rotate(self.arr, 3))

    def run(self):
        self.show()
