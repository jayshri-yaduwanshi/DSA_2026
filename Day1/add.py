# #Why python is called as dynamically typed language

# age=33
# pi=3.1
# name="Khushi"
# result=True

# print(type(age))
# print(type(pi))
# print(type(name))
# print(type(result))

# #==========================================================================================================

# print(id(age))
# print(id(pi))
# print(id(name))
# print(id(result))

# #==========================================================================================================

# #Why all fundamentals datatypes are immutable

# math = 50
# chem = 50
# phy = 50

# print(id(math))
# print(id(chem))
# print(id(phy))

# print(2+2)
# print("2"+"2")
# a=int(input("Enter First number: "))#"2"
# b=int(input("Enter second number: "))#"2"
# print(a+b)

# #============================================================================

# #int() used to convert other datatypes to integer 3.14=int=3
# #print(int(10+5j))
# print(int(3.14))
# print(int(True))#=1
# print(int(False))#=0
# #print(int("4.22"))
# print(int("4"))

# #We cannot complex value to int
# #print(int(10+5j))
# #We cannot convert floting point value to string to int
# #can't convert string name to int '''

# #==========================================================================================================

# #float() used to convert other datatypes to float
# #print(float(10+5j))
# print(float(3))
# print(float(True))
# print(float(False))
# print(float(4.22))
# print(float("4"))
# print(float("Khushi"))

#We cannot convert complex value to float
#can't convert string name to float

#==========================================================================================================
# complex() used to convert other datatypes to complex
# print(complex(3))
# print(complex(3.14))
# print(complex(True))
# print(complex(False))
# print(complex("4"))
# print(complex("4.22"))
# #print(complex("Khushi"))
# print(complex(5,-3))
# print(complex(True,False))

#==========================================================================================================
#bool() used to convert other datatypes to boolean
# print(bool(0)) #False
# print(bool(0.0))#False
# print(bool(15))#True
# print(bool(3.14))#True
# print(bool(False))#False
# print(bool(True))#true
# print(bool(0+0j))#False
# print(bool(1+3j))#True
# print(bool(""))#False
#print(bool("Khushi"))

#==========================================================================================================

#simple if
# a=int(input("Enter any Single digit number: "))
# if a>0:
#     print("This is a positive number")
# if a<0:
#     print("This is a negative number")
# if a==0:
#     print("This is a zero")

#==========================================================================================================
#if-else
# day = input("Enter any day of the week: ")
# if day=="SATURDAY" or day=="saturday" or day=="SUNDAY" or day=="sunday":
#     print("Weekend")
# else:    
#     print("Weekday")

#==========================================================================================================

# per =65
# if per>=65:
#     print("Graded A")
# elif per>=65 and per>=50:
#     print("Graded B")
# else:
#     print("Failed")

#==========================================================================================================

#How to identify the given string is in uppercase lowercase  special character or number

# a=input("Enter any single character: ")
# if a.isupper():
#     print("This is an uppercase character")
# elif a.islower():
#     print("This is a lowercase character")
# elif a.isdigit():
#     print("This is a number")
# else:
#     print("This is a special character")

#==========================================================================================================

# chr =ord(input("Enter any single character: "))
# if chr>=65 and chr<=90:
#     print("This is an uppercase character")
# elif chr>=97 and chr<=122:
#     print("This is a lowercase character")
# elif chr>=48 and chr<=57:
#     print("This is a number")
# else:
#     print("This is a special character")

#==========================================================================================================

#membership operator
# in 
# not in
# name = "Khushi"
# print("h" in name)
# print("p" in name)
# print("s" not in name)

#identifier operator(address comparison)
# is
# is not

# math =50
# chem =50
# print(math is chem)#True because both math and chem are pointing to the same memory location

#==========================================================================================================

# for i in range(5):#i=0
#     print(i)

# #for (initialization; condition; increment/decrement)
# for i in range(2,11,2):
#     print(i)

# for i in range(5,0,-1):
#     print(i)

# for i in range(1,11):
#     print(i*2)

# for i in range(1,11):
#     print(i*1," ",i*2, "  ",i*3, "  ",i*4, "     ",i*5, "    ",i*6, "   ",i*7, "     ",i*8, "   ",i*9, "     ",i*10)

# print("------------------------------------------------------------------------------------")

# for i in range(1,11):
#     print(i*11, " ",i*12, " ",i*13, " ",i*14, " ",i*15, " ",i*16, " ",i*17, " ",i*18, " ",i*19, " ",i*20)

#==========================================================================================================

# Write a program to accept there paper marks and calculate the total,percentage and check if the 
# he / she is paased in all the subject so print pass else print fail

# if percentage is greater than 65 and gender="male" so he is eligible for placement else 
# not eligible for placement

# math = int(input("Enter marks of math: "))
# chem = int(input("Enter marks of chem: "))
# phy = int(input("Enter marks of phy: "))
# bio = int(input("Enter marks of bio: "))
# gender=input("Enter gender:")
# total = math+chem+phy+bio
# per = total/4
# if math>=35 and chem>=35 and phy>=35 and bio>=35:
#     print("Congratulations! You are passed")
#     print("Total marks: ",total)
#     print("Percentage: ",per)
# else:
#     print("Fail")
#     print("Total marks: ",total)
#     print("Percentage: ",per)

# if per>=65 and gender=="male":
#     print("Congratulations! You are eligible for placement")
# else:
#     print("Sorry! You are not eligible for placement")

#==========================================================================================================

# for i in range(1,5):
#     if i==3:
#         break
#     print(i)

# for i in range(1,5):

#     if i==3:
#         continue
#     print(i)

#==========================================================================================================

for i,j in zip(range(1,6),range(5,0,-1)):
    if(i==3 and j==3):
        continue
    print(i , " ", j)