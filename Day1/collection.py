# #Collection Dataa types
# #List

# # mylist=["khushi","sneha",77.90,"priya","khushi",77]
# # print(mylist)
# # print(type(mylist))
# # print(mylist[0])
# # print(mylist[1])
# # print(mylist[2])
# # print(mylist[-1])
# # print(mylist[2:5])
# # print(mylist[:5])
# # print(mylist[1:])
# # print(mylist[1:7:2])    

# # mylist[2]="Akshay"
# # print(mylist)

# # if "khushi" in mylist:
# #     print("Yes, The element is present in the list")
# # else:
# #     print("No, The element is not present in the list")

# # mylist.append("Rohit")
# # mylist.append("Aachal") # append() method is used to add an element at the end of the list
# # print(mylist)

# # mylist.insert(2,"Sanskruti") # insert() method is used to add an element at a specific index in the list
# # print(mylist)

# # mylist.remove("khushi") # remove() method is used to remove the first occurrence of an element from the list
# # print(mylist)

# # newlist=mylist.copy() # copy() method is used to create a copy of the list
# # print(newlist)

# mylist=[['Khushi','akre'],[65.78],[990088,"KKK"]]
# print("example of multidimensional list: ")
# print(mylist)
# #print(mylist[row][col])
# print(mylist[0][0])#Khushi
# print(mylist[0][1])#akre    
# print(mylist[1][0])#65.78
# print(mylist[2][0])#990088
# print(mylist[2][1])#KKK
# #-------------------------------------------------------------------------------

# list2=[550,34.56,'Khushi']
# del list2[2]
# #del list2 # del keyword is used to delete the entire list
# print(list2) # this will raise an error because list2 has been 

# list2=[550,34.56,'Khushi']
# list2.clear() # clear() method is used to remove all the elements from the list
# print(list2) # this will print an empty list because all the elements have been removed from

# name="Khushi"
# print(name)
# myname=list(name) # list() function is used to convert a string into a list of characters
# print(myname)

# #sorting example
# numbers=[5,2,9,1,8,6]
# #numbers.sort() # sort() method is used to sort the elements of the list in ascending order
# numbers.sort(reverse=True) # sort() method with reverse=True is used to sort the elements of the list in descending order
# print(numbers)

# '''default sorting order is ascending order and if we want to 
# sort in descending order then we can use reverse=True parameter 
# in the sort() method.we should know that list should contain 
# homogeneoous data  python2 first short numbers then string follow '''

# #variable
# mylist=[5,2,9,1,8,6]
# newlist=mylist # this will create a new reference to the same list in memory
# print(id(newlist))
# print(id(mylist)) # both newlist and mylist are pointing to the same memory location

# mylist=[44,22,77,0,8,99]
# for i in mylist:
#     print(i)

# input=[0,1,4,0,2,5]
# output=[1,4,2,5,0,0]

#move th zero in the last

# for i in input:
#     if i==0:
#         input.remove(i)
#         input.append(i)
# print(input)

# Find the second largest element

# list1=[7,3,9,2,8]
# # list1.sort(reverse=True)
# # print(list1[1])

# list1.sort()
# print(list1[-2])

# a=[1,2,3,4,5,6,7,8,9]
# a[::2]=10,20,30,40,50,60 # this will print every second element of the list starting from the first element
# print(a)

# a=[1,2,3,4,5]
# print(a[3:0:-1]) # this will print the elements of the list in reverse order starting from the fourth element to the first element

# arr =[[1,2,3,4],[4,5,6,7],[8,9,10,11],[12,13,14,15]]
# for i in range(0,4):
#     print(arr[i].pop()) # this will print the last element of each sublist and remove it from the original list

# arr=[1,2,3,4,5,6]
# for i in range(1,6):
#     arr[i-1]=arr[i]

# for i in range(0,6):
#     print(arr[i], end=" ")

# fruit_list1=["apply",'berry','cherry','pappaya']
# fruit_list2=fruit_list1
# fruit_list3=fruit_list1[:]
# fruit_list2[0]="mango"
# fruit_list3[1]="grapes"

# sum=0
# for ls in (fruit_list1,fruit_list2,fruit_list3):
#     if ls[0]=="mango":
#         sum+=1
#     if ls[1]=="grapes":
#         sum+=20
# print(sum)

#find the common elemeny in the 3 lists

list1=[1,2,3]
list2=[2,3,4]
list3=[3,4,5]
common_elements=[]
for i in list1:
    if i in list2 and i in list3:
        common_elements.append(i)
print(common_elements)

#Write a program to calculate and return the sum of distance between the adjacent numbers in an array of positive integers.

mylist=[]
N=int(input("Enter the value of N: "))
for i in range(N):
    num=int(input("Enter a values: "))
    mylist.append(num)
#print(len(mylist))
sum=0
for i in range(len(mylist)-1):
    if i+1 in range(len(mylist)):
        sum+=abs(mylist[i]-mylist[i+1])
print("The sum of distance between the adjacent numbers is: ",sum)
