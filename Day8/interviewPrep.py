# try:
#     a = int(input("Enter a First number"))
#     b = int(input("Enter a second number"))
#     print(a/b)
# except ZeroDivisionError:
#     print("cant devide by zero")
# except ValueError:
#     print("Enter only integer value :")
# else:
#     print("Everything is ok")
#=============================================
# import logging
# logging.basicConfig(filename="newfile.txt", level=logging.DEBUG)
# try:
#     a=int(input("enter first integer no"))
#     b=int(input("enter second integer no"))
#     print(a/b)
# except (ZeroDivisionError, ValueError) as message:
#     print(message)
#     logging.exception(message)
# print("Logging level is set up. check 'newfile.txt' for log details.")
#================================================
# import csv
# f = open("employee.csv",'a')
# a = csv.writer(f)
# #a.writerow(["EmpID", "Emp Name", "Emp Age"])
# empid=int(input("enter employee id"))
# empName = input("enter employee name")
# age = int(input("enter employee age"))
# a.writerow([empid, empName, age])
# print("file has created")
#================================================
import csv

f = open("student.csv", 'a')
a = csv.writer(f)

#a.writerow(["StudID", "StudName", "Phy", "Chem", "Math", "Total", "Percentage", "Result"])

studid = int(input("Enter Student ID : "))
studname = input("Enter Student Name : ")

phy = int(input("Enter Physics Marks : "))
chem = int(input("Enter Chemistry Marks : "))
math = int(input("Enter Maths Marks : "))

# calculate total and percentage
total = phy + chem + math
percentage = total / 3

# check condition
if phy >= 40 and chem >= 40 and math >= 40:
    result = "Pass"
else:
    result = "Fail"

# write into csv file
a.writerow([studid, studname, phy, chem, math, total, percentage, result])

print("File has created")

f.close()
