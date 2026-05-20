#When the main problem divided into sub main problem then we use the recursion to solve the problem 
#When you see that the problem can be solved by solving the same problem with smaller input
#then you can use reccuresion to solve the problem
#Reccurion also use the stack so that we avoide to use recurresion

# def factorial(num):
#     if num <= 1:
#         return 1
#     return num* factorial(num -1)

# print(factorial(4))

#=====================================================================================

#CapiytalizaFirst solution using recursion

# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result 
    
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:])

# print(capitalizeFirst(['car' , 'taco' , 'banana']))

#====================================================================================

# def power(base , exponent):
#     if exponent == 0:
#         return 1
#     return base * power(base, exponent -1 )

# print(power(2,0))
# print(power(2,2))
# print(power(2,4))

#====================================================================================

#product array solution

# def productOfArray(arr):
#     if len(arr) == 0:
#         return 1
#     return arr[0] * productOfArray(arr[1:])

# print(productOfArray([1,2,3]))
# print(productOfArray([1,2,3,10]))

#=====================================================================================

#Reverse Solution

def reverse(string):
    if len(string) <= 1:
        return string
    return string[len(string) - 1] + reverse(string[0:len(string) - 1])
print(reverse('python'))
print(reverse('appmillers'))

#======================================================================================

def isPalindrome(string):
    if len(string) == 0:
        return True
    if string[0] != string[len(string)-1]:
        return False
    return isPalindrome(string[1:-1])

print(isPalindrome('awesome'))





#=====================================================================================

#Some recursion solution

def someRecursion(arr, cb):
    if len(arr) == 0:
        return False
    if not(cb(arr[0])):
        return someRecursion(arr[1:], cb)
    return True
def isOdd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
print(someRecursion([1,2,3,4] , isOdd))
print(someRecursion([4,6,8,9] , isOdd))
print(someRecursion([4,6,8] , isOdd))