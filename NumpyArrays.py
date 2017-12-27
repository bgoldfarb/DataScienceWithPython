import numpy as np


my_list = [1,2,3]
print(my_list)

arr = np.array(my_list)
print(arr)

my_mat = [[1,2,3], [4,5,6], [7,8,9]]
print(my_mat)

np_mat = np.array(my_mat)
print(np_mat)

print(np.arange(0,11, 3))

print(np.zeros((3,2)))

print(np.ones((3,4)))

print(np.linspace(0,20,50))

#Identity Array
print(np.eye(4))

print(np.random.rand(5))

#Standard Normal Dist
print(np.random.randn(2,3))

#Finding random integers
print(np.random.randint(0,50))
randomInts = np.random.randn(2,3) 

#reutrns max value of array
print("Random array", randomInts)

#Location of max or min number of array
print("Max: ", randomInts.max())
print(randomInts.argmax())

#Reshaping arrays
print("Shape of array", randomInts.shape)
randomInts.reshape(6)
print("Shape of reshaped array", randomInts.shape)

#Type of array
print("Type of array", randomInts.dtype)