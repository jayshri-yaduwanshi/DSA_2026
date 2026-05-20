
mydict={
    101:"Python",
    102:"Java", 
    103:"C++",
    104:"JavaScript",
    105:"C#",
    101:"Python3.10" ,  #we cannot have duplicate keys in a dictionary, so the value of key 101 will be updated to "Python3.10"  
    104:"JavaScript ES6"   #we cannot have duplicate keys in a dictionary, so the value of key 104 will be updated to "JavaScript ES6"    
}
# print(mydict)

#With the help of key we have to print values
# a=mydict[102]   #we can access the value of a key in a dictionary by using the key
# print(a)

#We will replace old value by new value
# mydict[102]="Java SE"   #we can change the value of a key in a dictionary by using the key
# print(mydict)

#only print key x=0,1
# for x in mydict:
#     print(x)

#only print value
# for x in mydict.values():
#     print(x)

#additing a new key value pair
# mydict["mobile_no"]=98707457438
# print(mydict)

#we can remove a key value pair from a dictionary by using the pop() method
# mydict.pop(105)   
# print(mydict)

# #Q-1

# a={(1,2):1,(2,3):2,(4,5):3}
# print(a[4,5])  #3 because we can use a tuple as a key in a dictionary

# #Q-2

# a={'a':1,'b':2,'c':3}
# print(a['a','b']) #TypeError: unhashable type: 'tuple' because we cannot use a tuple as a key in a dictionary if it is not defined as a key in the dictionary

#Q-3

# arr={}
# arr[1]=1
# arr['1']=2
# arr[1] +=1
# print(arr)   
# sum=0
# for k in arr:
#     sum+=arr[k]
# print(sum)   #4 because we have 1+2+1=4

#Q-4

# mydict={}
# mydict[1]=1
# mydict['1']=2
# mydict[1.0]=4
# print(mydict)
# sum=0
# for k in mydict:
#     sum+=mydict[k]
# print(sum)   #6

#Q-5
# my_dict={}
# my_dict[(1,2,4)]=8
# my_dict[(4,2,1)]=10
# my_dict[(1,2)]=12
# sum=0
# for k in my_dict:
#     sum +=my_dict[k]
# print(sum)
# print(my_dict)

#Q-6

# box={}
# jars={}
# crates={}
# box['biscuit']=1
# box['cake']=3
# box['jam']=4
# crates['box']=box
# crates['jars']=jars
# print(len(crates[box]))  #TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')

#Q-7

# dict={'c':97,'a':96,'b':98}
# for _ in sorted(dict):
#     print(dict[_])       # 96 98 97

#Q-8

# rec={"Name":"Python","Age":"20"}
# r=rec.copy()
# print(id(r)==id(rec)) #False

#Q-9

# rec={"Name":"python","Age":"20","NJ":"Addr"}
# id1=id(rec)
# print(id1)
# del rec
# rec={"Name":"python","Age":"20","NJ":"Addr"}
# id2=id(rec)
# print(id2)
# print(id1==id2)

#=======================================================================================================

#Find the key with the maximum value in a dictionery
#Input: {"A":50,"B":30,"C":70}
#Output:"C"

# Find the key with the maximum value using loop

# data = {"A": 50, "B": 30, "C": 70}

# max_key = ""
# max_value = 0

# for key in data:
#     if data[key] > max_value:
#         max_value = data[key]
#         max_key = key

# print(max_key)

#=======================================================================================================

#Find the Key With the minimum value in dictionery
#Input: {"A":50,"B":30,"C":70}
#Output:"B"

# Find the key with the minimum value using loop

# data = {"A": 50, "B": 30, "C": 70}

# min_key = ""
# min_value = float('inf')

# for key in data:
#     if data[key] < min_value:
#         min_value = data[key]
#         min_key = key

# print(min_key)

#=======================================================================================================

#Count Frequency of Elemeent in a list using a dictonary

#Input:[1,2,2,3,4,3,5]
#Ouput:{"1":1,"2":2,"3":2,"4":1,"5":1}

# Count frequency of elements in a list using dictionary

# numbers = [1, 2, 2, 3, 4, 3, 5]

# freq = {}

# for num in numbers:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1

# print(freq)

#===================================================================================================
#123456=654321

# num=123456
# a=num%10 #6
# num=num//10 
# b=num%10
# num=num//10
# c=num%10
# num=num//10
# d=num%10
# num=num//10
# e=num%10
# f=num//10
# rev=a*100000+b*10000+c*1000+d*100+e*10+f*1
# print(rev)

#=====================================================================================================

Amount=int(input("Please Enter Amount for Withdraw : "))
print(" 100 notes = ",Amount//100)
print(" 50 notes = ",(Amount%100)//50)
print(" 20 notes = ",((Amount%100)%50)//20)
print(" 10 notes = ",(((Amount%100)%50)%20)//10)
print(" 5 notes = ",((((Amount%100)%50)%20)%10)//5)
print(" 2 notes = ",(((((Amount%100)%50)%20)%10)%5)//2)
print(" 1 notes = ",((((((Amount%100)%50)%20)%10)%5)%2)//1)