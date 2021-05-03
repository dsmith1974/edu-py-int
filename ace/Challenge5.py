# Problem Statement #
# Implement a function findMinimum(lst) which finds the smallest number in the given list.
#
# Input: #
# A list of integers
#
# Output: #
# The smallest number in the list
#
# Sample Input #
# arr = [9,2,3,6]
# Sample Output #
# 2

# max() min()
# max(lis, key = lambda x: x[1]), https://stackoverflow.com/questions/18296755/python-max-function-using-key-and-lambda-expression

class Challenge:
    def __init__(self):
        self.arr = [9,2,3,6]

    def find_minimum(self, arr):
        minimum = arr[0]
        # At every Index compare its value with minimum and if its less
        # then make that index value new minimum value
        for val in arr:
            if val < minimum:
                minimum = val

        return minimum

    def show(self):
        print(self.find_minimum(self.arr))

    def run(self):
        self.show()
