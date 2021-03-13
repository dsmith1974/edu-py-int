# https://www.educative.io/module/lesson/data-structures-in-python/393G9ZlnOEQ

#Challenge 1: Remove Even Integers from List
#Given a list of size n, remove all even integers from it. Implement this solution in Python and see
#if it runs without an error.

#Problem Statement #
#Implement a function that removes all the even elements from a given list. Name it remove_even(list).

#Input #
#A list with random integers.

#Output #
#A list with only odd integers

#Sample Input #
#my_list = [1,2,4,5,10,6,3]
#Sample Output #
#my_list = [1,5,3]

# https://www.geeksforgeeks.org/python-program-to-print-odd-numbers-in-a-list/
# list comprehension
# filter and lambda odd_nos = list(filter(lambda x: (x % 2 != 0), list1))

# https://www.geeksforgeeks.org/python-separate-odd-and-even-index-elements/
# list slicing


class Challenge:
    def __init__(self):
        self.list = [1,2,4,5,10,6,3]

    def remove_even(self):
        self.list = [item for item in self.list if item % 2 != 0]

    def show(self):
        print(self.list)

    def run(self):
        self.remove_even()
        self.show()



