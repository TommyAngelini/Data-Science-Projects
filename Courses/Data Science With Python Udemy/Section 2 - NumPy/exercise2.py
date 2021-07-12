'''
This exercise is from The Bootcamp of Data Science with Python Udemy course.
Tomas Angelini
Exercise 2
'''

import numpy as np

def inspect_array(array):
     
    if(type(array) != np.ndarray):
        print('The inserted object is not a NumPy array.')
    else:
        print('Shape: ', array.shape)
        print('Size: ', array.size)
        print('# Dimensions: ', array.ndim)
        print('# Bytes: ', array.nbytes)
        print('Data Type: ', array.dtype)
        print('Type', type(array))

def main():
    inspect_array([1,2,3])
    inspect_array(np.array([1,2,3]))

if __name__ == '__main__':
    main()