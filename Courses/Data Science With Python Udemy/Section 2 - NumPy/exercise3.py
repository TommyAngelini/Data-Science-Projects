'''
This exercise is from The Bootcamp of Data Science with Python Udemy course.
Tomas Angelini
Exercise 3
'''

import numpy as np

# three ways to make an np array
# a) use list as an argument
list_ = [-1, 4, 7, 9]
array1 = np.array(list_)
print(array1)

# b) use range function 
array2 = np.array(range(1,11))
print(array2)

array4 = np.array(range(1990, 2021, 5))
print(array4)

array5 = np.array(range(2020, 1890, -10))
print(array5)

# c) use tuple as argument
array3 = np.array(tuple([10, 11, 12, 13, 14]))
print(array3)

array6 = np.array(100)
print(array6)