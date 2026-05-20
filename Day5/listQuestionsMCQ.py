#=================================================================
#Q-1

# def func(value, values):
#     var = 1
#     values[0] = 44
# t = 3
# v = [1,2,3]
# func(t,v)
# print(t, v[0]) # 3 44

#================================================================================

#Q-2

# def f(i,values = []):
#     values.append(i)
#     print(values) # [1] [1,2] [1,2,3]

# f(1)
# f(2)
# f(3)

#==========================================================================================

#Q-3

# fruit = {}
# def addone(index):
#     if index in fruit:
#         fruit[index] += 1
#     else:
#         fruit[index] = 1

# addone('Apple')
# addone('Banana')
# addone('apple')
# print(len(fruit)) # 3

#==========================================================================================

#Q-4
#Write a program to accept student name and marks from the keyword 
#and creates a dictonery. Also display student marks aby taking a student name 

# n=int(input("Enter the number of Student :"))
# student = {}

# for i in range(n):
#     name = input("Enter Student Name : ")
#     marks = int(input("Enter Student Marks : "))
#     student[name]=marks

# print(student)

# while True:
#     name = input("Enter student name to get Marks : ")
#     marks = student.get(name,-1)
#     if marks == -1:
#         print("Student Not Found !!!!")
#     else:
#         print("The Marks of ",name, "are " ,marks)
#     option = input("Do You want to find another Student marks[Yes|No] : ")
#     if option == "No":
#         break

# print("Thanks for using our Application ")

#======================================================================================

#Q-5

#Write a program to access each character of String in forward and backward direction
#by using while loop?
#Input = "Learning Python is Very easy "

# input="Learning Python is very easy"
# i=0
# print("Forward Direction : ")
# while i < len(input):
#     print(input[i], end="")
#     i += 1

# print("\n")

# print("Backward Direction : ")
# i=len(input)-1
# while i >= 0:
#     print(input[i],end="")
#     i -= 1

#=======================================================================================

#Q-6

#Input:abcdfjgerj abcdfjger
#output:j
#The Character "j" at the end of the sent
#String was lost in the network during transmission 

# s1 = input()
# s2 = input()
# for ch in s1:
#     if ch not in s2:
#         print(ch)
#         break 

#==================================================================================

#Q-7

# v = ['a','e','i','o','u']
# w = input("Enter the word where we will search the vowels : ")
# w = "khushi"
# found = []
# for i in w:
#     if i in v:
#         if i not in found:
#             found.append(i)
# print('Found vowels = ',found)
# print('Unique vowels', len(found), 'from the given word =' ,w)

#===================================================================================

#Q-8

#Input:
#6 30 50
#29 38 12 48 39 55
# Output: 
# 38 48 39
#Explanation: There are three employee with distances 38,48 and 39 whose distance 
#from the office list within the given range

# x, y, z = map(int, input().split())

# mylist = list(map(int, input().split()))

# for j in mylist:
#     if j >= y and j <= z:
#         print(j, end=' ')


#=====================================================================================

#Q-9

# import datetime

# #datetime formatting
# date = datetime.datetime.now()
# print("It's now : {: %d/%m/%Y %H:%M:%S}".format(date))

#=====================================================================================

#Q-10

# x = ['A','B','C']
# y = ['A','B','C']
# z = [1,2,3,4]
# print(x == y) #True
# print(x == z) #False
# print(x != z) #True

#=====================================================================================

#Q-11

# val=[2**i for i in range(1,6)] #i=1,2,3,4,5
# print(val) #[2, 4, 8, 16, 32]

#=====================================================================================

#Q-12

# s= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# val=[i*i for i in range(1,11)] 
# print(val) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

#========================================================================================

#Q-13

#Dictionary Compresion:

# squares={x:x*x for x in range(1,6)}
# print(squares)

# doubles={x:2*x for x in range(1,6)}
# print(doubles)

#========================================================================================

#Q-14

#How to read a multiple values from the keyboard in a single line

# a, b= [int(x) for x in input("Enter 2 numbers : ").split('')]
# print("Produnct is : ", a*b)
# 
# a,b,c= [float(x) for x in input("Enter 3 numbers : ").split(',')]
# print("The Sum is : ",a+b+c) 

#========================================================================================

#Q-15

#using else block
# mycart = [10,20,800,60,70] 
# for item in mycart:
#     if item > 400:
#         print("This is not in my budget")
#         continue
#     print(item)
# else:
#     print("You have purchased everything")

#========================================================================================

#Q-16

# # username = "admin"
# # password = "admin"


# while(True):
#     username = input("Enter Your Username : ")
#     password = input("Enter Your Password : ")
#     if username == "admin" and password == "admin":
#         print("Login Successfully !!!!")
#         break
#     else:
#         print("Login Denied !!!!!")
#         continue

#========================================================================================

#Q-17->>> Tower of Hanoi Problem 
import time
class Tower:
    def __init__(self):
        print("WELCOME TO TOWER OF HANOI GAME")
        print()
        print("Given Problem     A= [3,2,1]       B= []       c= []   ")
        print()
        print("Expected output   A= []       B= []       c= [3,2,1]   ")
        self.A = []
        self.B = []
        self.C = []

    def tower(self,item):
        self.A.append(item)
        time.sleep(3)
        print("A =", self.A)
        print("Items in Tower A\n")

    def pass1(self):
        self.temp = self.A.pop(2)
        self.C.append(self.temp)
        time.sleep(3)
        print("A= ",self.A    ,"   ",   "B= ",self.B    ,"   ",   "C= ",self.C)
        print("Pass One Completed==============================================\n")

    def pass2(self):
        self.temp = self.A.pop(1)
        self.B.append(self.temp)
        time.sleep(3)
        print("A= ",self.A    ,"   ",   "B= ",self.B    ,"   ",   "C= ",self.C)
        print("Pass Second Completed==============================================\n")

    def pass3(self):
        self.temp = self.C.pop(0)
        self.B.append(self.temp)
        time.sleep(3)
        print("A= ",self.A    ,"   ",   "B= ",self.B    ,"   ",   "C= ",self.C)
        print("Pass Three Completed==============================================\n")

    def pass4(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A= ",self.A    ,"   ",   "B= ",self.B    ,"   ",   "C= ",self.C)
        print("Pass Four Completed==============================================\n")

    def pass5(self):
        self.temp = self.B.pop(1)
        self.A.append(self.temp)
        time.sleep(3)
        print("A= ",self.A    ,"   ",   "B= ",self.B    ,"   ",   "C= ",self.C)
        print("Pass Five Completed==============================================\n")

    def pass6(self):
        self.temp = self.B.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A= ",self.A    ,"   ",   "B= ",self.B    ,"   ",   "C= ",self.C)
        print("Pass Six Completed==============================================\n")

    def pass7(self):
        self.temp = self.A.pop(0)
        self.C.append(self.temp)
        time.sleep(3)
        print("A= ",self.A    ,"   ",   "B= ",self.B    ,"   ",   "C= ",self.C)
        print("Pass Seven Completed==============================================\n")

obj =Tower()
obj.tower(3)
obj.tower(2)
obj.tower(1)
obj.pass1()
obj.pass2()
obj.pass3()
obj.pass4()
obj.pass5()
obj.pass6()
obj.pass7()

