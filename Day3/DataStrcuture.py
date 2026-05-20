# =====================================================================================

# Data Strcture: data Strcture are different 
# ways of organizing data on your computer,
# that can be used effectively.

#======================================================================================

# Name        TimeComplexity
# Constant     O(1)
# Linear       O(N)
# Logarithmic O(logN)
# Quadratic  O(N power 2)
# Exponentional O(2 power N)

#==================================================================================

# O(1)-Constant Time

# array=[1,2,3,4,5]
# array[0] //it takes constant time to access first elemet
#---------------------------------------------------------------------------
# O(N) -Linear time

#array =[1,2,3,4,5]
#for elemet in array:
#  print (elemet) //linear time since it is visiting every elemet of array
#------------------------------------------------------------------------------
#O(logN)-Logrithmic time

# array =[1,2,3,4,5]
# for index in range(0,len(array),3):
#     print(array[index]) #logrithmic time since it is visiting only some element 
#-------------------------------------------------------------------------------------
#O(N power 2)- Quadratic time
#####Looking array a every index in the array twice
# array=[1,2,3,4,5]
#for x in array:
#    for y in array:
#       print(x,y)
#-----------------------------------------------------------------------------
#O(2 power N)-Exponential time
#
#def fibonaci(n):
#    if n<=1:
#       return n
#      return fibonacii(n-1)+fibonacci(n-2)

#===================================================================================

#Find Biggest number 
def findBiggestNumber(sampleArray):
    biggestNumber=sampleArray[0]
    for index in range(1,len(sampleArray)):
        if sampleArray[index]>biggestNumber:
            biggestNumber=sampleArray[index]
    print(biggestNumber)

sampleArray=[5,7,9,2,3,4]
findBiggestNumber(sampleArray)