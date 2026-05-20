#=======================================================================================

#Q-1

#Reverse Each Word in a String
# Input ="Hello World"
# Output = "olleH dlroW"

# s = input("Enter a string: ")

# word = ""

# for ch in s:
#     if ch != " ":
#         word = ch + word
#     else:
#         print(word, end=" ")
#         word = ""

# print(word)

#=======================================================================================

#Q-2

#Check for Valid Parentheses:
#Input = ({{()}})
#Output = valid

# def valid_parentheses(s):

#     stack = []

#     for ch in s:

#         if ch in "({[":
#             stack.append(ch)

#         else:

#             if len(stack) == 0:
#                 return "invalid"

#             top = stack.pop()

#             if ch == ')' and top != '(':
#                 return "invalid"

#             if ch == '}' and top != '{':
#                 return "invalid"

#             if ch == ']' and top != '[':
#                 return "invalid"

#     if len(stack) == 0:
#         return "valid"
#     else:
#         return "invalid"


# s = input("Enter brackets: ")

# print(valid_parentheses(s))

#=======================================================================================

#Q-3
#Insertion Sort Algorithm
#Sort the List [5, 3, 8, 6, 2] in ascending order.

# arr = [5,3,8,6,2]
# for i in range(1, len(arr)):
#     key = arr[i]
#     j = i-1
#     while j >= 0 and arr[j] > key:
#         arr[j+1] = arr[j]
#         j = j-1
#     arr[j+1] = key
# print(arr) 

#=======================================================================================

#Q-4
#Selection Sort Algorithm

# arr = [20,12,10,15,2]
# for i in range(len(arr)):
#     min = i
#     j = i+1
#     while j < len(arr):
#         if arr[j] < arr[min]:
#             min = j
#         j = j+1
#     arr[i], arr[min] = arr[min],  arr[i]
        
# print(arr)

#=======================================================================================

#Find All Duplicates in a List
#Use a loop and a directonary to count occurrences
#Sample Output: [4, 3, 2, 7, 8, 2, 1, 5, 5]
#output: [2, 5]

nums = [4, 3, 2, 7, 8, 2, 1, 5, 5]

count = {}
duplicates = []

for i in nums:

    if i in count:
        count[i] += 1
    else:
        count[i] = 1

for key in count:

    if count[key] > 1:
        duplicates.append(key)

print(duplicates)

#=====================================================================================

#Sort Dictionery by key or Value
#Use the sorted() function with a custom key or use list comprehension
#Input: {"C:3,"B":2,"A":1}
#Output: (Ascending by key ): {"A":1,"B":2,"C":3}
#output: (Desending by value ): {"C":3, "B":2,"A",1}

# d = {"C": 3, "B": 2, "A": 1}

# items = []

# for k in d:
#     items.append([k, d[k]])

# # Ascending by Key
# for i in range(len(items)):
#     for j in range(i + 1, len(items)):

#         if items[i][0] > items[j][0]:
#             temp = items[i]
#             items[i] = items[j]
#             items[j] = temp

# print("Ascending by key :")

# print("{", end=" ")
# for i in range(len(items)):
#     print("'" + items[i][0] + "':", items[i][1], end=" ")
# print("}")

# # Descending by Value
# for i in range(len(items)):
#     for j in range(i + 1, len(items)):

#         if items[i][1] < items[j][1]:
#             temp = items[i]
#             items[i] = items[j]
#             items[j] = temp

# print("Descending by value :")

# print("{", end=" ")
# for i in range(len(items)):
#     print("'" + items[i][0] + "':", items[i][1], end=" ")
# print("}")