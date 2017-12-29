import numpy as np

#Creates an array with 11 elements
arr = np.arange(0,11)
print(arr)

#Prints slice from 1 to 5 inclusive 
print(arr[1:5])

#Print everything up to 6
print(arr[:6])

#Numpy arrays have ability to broadcast
broadcastArray = arr
broadcastArray[0:5] = 50
#Note how the arr array is changed need to use copy method
print(broadcastArray)
print(arr)

arr = np.arange(0,11)
broadcastArray = arr.copy()
print(broadcastArray)


#Row by Column
arr_2d = np.array([[5,10,15],[20,25,30], [35,40,45]])
print(arr_2d)

#To get 5 from this array...
print(arr_2d[0][0])
#To get 15 from this array...
print(arr_2d[0][2])
#To get 40 from this array...
print(arr_2d[2][1])

#Comma single bracket notation
print(arr_2d[2,1])


#Top right corner, everything but row 3 and past column 2
print(arr_2d[:2,1:])


#Conditional Selection

arr = np.arange(1,11)
bool_arr = arr > 5
print(bool_arr)
#only prints array where numbers are greater than 5
print(arr[bool_arr])

#Print all elements of the array less than 3
print(arr[arr < 3])

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)

#Grab 13, 14, 23,24
print(arr_2d[1:3,3:5])