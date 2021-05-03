# Problem Statement #
# Implement a function find_second_maximum(lst) which returns the second largest element in the list.
#
# Input: #
# A List
#
# Output: #
# Second largest element in the list
#
# Sample Input #
# [9,2,3,6]
# Sample Output #
# 6

class Challenge:
    def __init__(self):
        self.arr = [9,2,3,6]

    def find_second_maximum(self, lst):
        max = float('-inf')
        secondmax = float('-inf')
        for val in lst:
            if val > max:
                secondmax = max
                max = val
            elif val > secondmax:
                secondmax = val
        return secondmax

    def show(self):
        print(self.find_second_maximum(self.arr))

    def run(self):
        self.show()
