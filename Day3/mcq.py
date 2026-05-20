#=======================================================================================

#2. Count Substrings in a string
#Input: "abababab" and "ab"
#Output:4

# string = "abababab"
# substring = "ab"
# count = 0
# for i in range(len(string) - len(substring) + 1):
#     if string[i:i+len(substring)] == substring:
#         count += 1
# print(count)

#============================================================================================

#1. Maximum Consecutive Ones:
#Input: [1,1,0,1,1,1,0,1,1,1,1]
#output:4

# arr = [1,1,0,1,1,1,0,1,1,1,1]
# count = 0
# max_count = 0
# for num in arr:
#     if num == 1:
#         count += 1       
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print(max_count)

#====================================================================================

#Row wise max value

#[[100,198,333,323],
# [122,232,221,111],
#  [223,565,245,764]]

# list=[[100,198,333,323],
#       [122,232,221,111],
#       [223,565,245,764]]
# for i in list:
#     max_value=i[0]
#     for j in i:
#         if j>max_value:
#             max_value=j
#     print(max_value)

#=======================================================================================

#input = khushi*is*a*good*programmer
#output = ****khushiisagoodprogrammer

# string ='khushi*is*a*good*programmer'
# newname=''
# val='' 
# for i in string:
#     if i!='*':
#         newname+=i
#     else:
#         val+=i
# print(newname)
# print(str(val+newname))

#===================================================================================
#input:aaabbbbccceeeee
#output:a3b4c3e5

# name='aaabbbbccceeeee'
# newname={}
# for i in range(len(name)):
#     key=name[i]
#     count=0
#     for j in range(len(name)):
#         if key == name[j]:
#             count+=1
#     newname[key] = count
# #Print(newname)
# for i,j in newname.items():
#     print(i,j,sep='',end='')

#=====================================================================================

# salary = int(input('Enter your salary :'))
# rating = int(input('Enter your performance appraisal rating :'))
# increment =0
# if rating >=1 and rating<=3:
#     increment = salary*10/100
# elif rating>=3.1 and rating<=4:
#     increment = salary*30/100
# elif rating>=4.1 and rating<=5:
#     increment = salary*40/100
# else:
#     print('Invalid rating')
# print('Incrementted Salary: ' ,increment+salary)

#===========================================================================
#basic salary=20000
#so we have to calculate the 
#HRA of basicSalary =20%
#TA of basicSalary = 30%
#DA of GrossSalary = 45%
#Calculate GrossSalary =?

basicSalary =20000
print("HRA of BasicSalary = 20%")
print("TA of BasicSalary = 30%")
print("DA of GrossSalary = 45%")
GrossSalary=4000+6000+9000+basicSalary
print("Gross Salary = ", GrossSalary)
