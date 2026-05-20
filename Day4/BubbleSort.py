# def bubbleSort(array):
#     for i in range(len(array)-1):
#         for j in range(len(array)-i-1):
#             if array[j] > array[j+1]:
#                 temp =array[j]
#                 array[j] =array[j+1]
#                 array[j+1]=temp
#     print(array)
#     print()

# array=[64,34,25,12,22,11,90]
# bubbleSort(array)

#==================================================================================
#Input: 578378923
#Output: 3
#The repeated digits in the a data are 7,8 and 3. so, the security key is 3

mylist=[5,7,8,3,7,8,9,2,3]
newlist=[]
for i in range(len(mylist)):
    count=0
    key=mylist[i]
    j=i+1
    while j<len(mylist):
        if key == mylist[j]:
            newlist.append(key)
        j=j+1
print(len(newlist))

