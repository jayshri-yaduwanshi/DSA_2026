#While Loop

# i=1
# while i<=5:
#     print(i)
#     i+=1

#=====================================================================================

#========================================function=========================================

# def hello(): # called funtion
#     print("Hello World")

# hello() # calling function
# hello()

#-====================================================================================

# def arthimetic(a,b):
    
#     sum=a+b
#     sub=b-a
#     div=a/b
#     mul=a*b
#     return sum,sub,div,mul

# #positional Argument
# result=arthimetic(5,5)
# print("Arthmetic =",result)

#========================================================================================

#How many types of arguments we pass in funtions 
# -1.posional
# -2.keyword
# -3.default
# -4.variable length aurgument /varible numbers of argumenst

#======================================================================================

#Keyword argument

# def credential(username, password):
#     if username==password:
#         print("Login Successfully")
#     else:
#         print("Invalid creditional")

# credential(username ="admin", password="admin")#Calling function

#=====================================================================================

#Default argument 

# def cityName(city="Mahableshwar"):
#     print(city)

# cityName("Nagpur")
# cityName("Lonavala")
# cityName()

#=====================================================================================

#variable length argument/variable number of arguments

# def cityName(*name):
#     print(name)

# cityName("Nagpur", "Delhi", "Lonawala", "Pune")

#=====================================================================================

#Modularity apporach in function

# import sys 
# def add():
#     a=int(input("Enter the value of a "))
#     b=int(input("Enter the value of b "))
#     print(a+b)

# def sub():
#     a=int(input("Enter the value of a "))
#     b=int(input("Enter the value of b "))
#     print(a-b)

# def mul():
#     a=int(input("Enter the value of a "))
#     b=int(input("Enter the value of b "))
#     print(a*b)

# def div():
#     a=int(input("Enter the value of a "))
#     b=int(input("Enter the value of b "))
#     print(a/b)

# while True:
#     print("1. Addition")
#     print("2. Substraction")
#     print("3. Division")
#     print("4. Multiplication")
#     print("5. Exits")
#     choice=int(input("Enter Your Choice : "))
#     if choice == 1:
#         add() #Calling funtion
#     elif choice == 2:
#         sub() #calling function
#     elif choice == 3:
#         mul() # calling funtion
#     elif choice == 4:
#         div() # calling function
#     elif choice == 5:
#         sys.exit()

#=====================================================================================




