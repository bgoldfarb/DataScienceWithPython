import numpy as np

arr = np.arange(0,11)
print(arr)

#Double each element of array
print(arr+arr)

#Scalars
print(arr+100)

#Universal Array Functions
print(np.sqrt(arr))

print(np.exp(arr))

print(np.max(arr))

print(np.sin(arr))

print(np.cos(arr))

print(np.log(arr))

#Numpy Problems

#Create an array of 10 zeros
zeroArray = np.zeros(10)
print(zeroArray)

#Create an array of 10 ones
onesArray = np.ones(10)
print(onesArray)

#Create an array of 10 fives
fivesArray = np.ones(10) * 5
print(fivesArray)

#Create an array of integers from 10 to 50 inclusive
array1 = np.arange(10, 51)
print(array1)

#Create an array of even integers from 10 to 50
evenArray = np.arange(10,51, 2)
print(evenArray)

#Create a 3x3 matrix with values ranging from 0 to 8
threeByThreeMatrix = np.arange(9).reshape(3,3)
print(threeByThreeMatrix)

#Create a 3x3 identity matrix
idArray = np.eye(3)
print(idArray)


#Generate random number between 0 and 1
randomNum = np.random.rand(1)
print(randomNum)

#Generate array of 25 random numbers from a standard normal distribution 
randArray = np.random.randn(25)
print(randArray)

#Create a 2x2 matrix starting with 0.01 to 1 increment by 0.01
array2 = np.arange(1,101).reshape(10,10)/100
print(array2)
otherArray2 = np.linspace(0.01, 1, 100).reshape(10,10)
print(otherArray2)

#Create an array of 20 linearlly spaced points between 0 and 1
array3 = np.linspace(0,1,20)
print(array3)

mat = np.arange(1,26).reshape(5,5)
print(mat)

#Grab the lower right quadrant of mat starting with 12

myNewArray = mat[2:,1:]
print(myNewArray)

#Grab just the number 20 from mat

just20 = mat[3,4]
print(just20)

#Grab the column up to 17 from mat

colUpTo17 = mat[:3, 1:2]
print(colUpTo17)

#Grab the last row of mat

lastRow = mat[4,:]
print(lastRow)

#Get the sum of all the values in mat

theSum = np.sum(mat)
print(theSum)

#Get the std deviation of mat

stdDev = np.std(mat)
print(stdDev)

#Get the sum of all columns

colSum = mat.sum(axis=0)
print(colSum)