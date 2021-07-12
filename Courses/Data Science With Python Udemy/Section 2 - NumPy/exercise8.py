'''
This exercise is from The Bootcamp of Data Science with Python Udemy course.
Tomas Angelini
Exercise 8
'''

K = np.array([[np.nan, 1, 10, 0],
              [np.nan, np.nan, np.nan, np.nan],
              [100, 50, np.nan, -25],
              [30, np.nan, np.nan, 130]])

np.isnan(K)
print(f'There are {np.isnan(K).sum()} missing data in K')