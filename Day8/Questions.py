#Remove Leading Zeros from a List of Integers:
#Use list slicing or a loop to remove zeros until a non zeros element is encountered
#Input: [0,0,1,2,0,3,0,0,4]
#Output: [1,2,0,3,0,0,4]

# list = [0,0,1,2,0,3,0,0,4]

# while list and list[0] == 0:
#     list.pop(0)

# print(list)

#=======================================================================================
#Find the First Missing Positive integer
#Use a loop and reposition elements to place each positive integer at its respective index
#input: [3,4,-1,1]
#output: 2

# Find the first missing positive integer

# nums = [3, 4, -1, 1]

# n = len(nums)

# # Place each number at its correct index
# for i in range(n):
#     while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
#         correct_index = nums[i] - 1
#         nums[i], nums[correct_index] = nums[correct_index], nums[i]

# # Find the first missing positive
# for i in range(n):
#     if nums[i] != i + 1:
#         print(i + 1)
#         break
# else:
#     print(n + 1)

#======================================================================================
 
#Find the Smallest Missing Positive Integers:
#Use a loop and reposition elements to place each positive integer at its respective index 
#Input: [7,8,9,11,12]
#Output: 1

# Find the smallest missing positive integer

nums = [7, 8, 9, 11, 12]

n = len(nums)

# Place numbers at correct index
for i in range(n):
    while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
        correct_index = nums[i] - 1
        nums[i], nums[correct_index] = nums[correct_index], nums[i]

# Find missing positive
for i in range(n):
    if nums[i] != i + 1:
        print(i + 1)
        break
else:
    print(n + 1)