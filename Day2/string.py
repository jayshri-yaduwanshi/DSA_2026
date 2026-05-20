#============================================================================================

#product of Array Except self

#Input: [1,2,3,4]]
#output: [24,12,8,6]



    


#============================================================================================

# print("Khushi".find('u')) # this will print the index of the first occurrence of the character 'u' in the string "Khushi"
# print("Khushi".index('u')) # this will print the index of the first occurrence of the character 'u' in the string "Khushi"
# print("Khushi".count('h')) # this will print the number of occurrences of the character 'h' in the string "Khushi"

#=-============================================================================================

#Pattern Printing

# 1. Input:
# 1 1 1
# 2 2 2
# 3 3 3

# for i in range(1,4):# outer loop ==>rows
#     for j in range(1,4): # inner loop ==>columns
#         print(i,end=" ") # this will print the value of i followed by a space and stay on the same line
#     print() # this will print a new line after each row is printed

# 2. Input:
# A A A A A 
# B B B B B 
# C C C C C 
# D D D D D 
# E E E E E 

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1): # outer loop ==>rows
#     for j in range(1,n+1): # inner loop ==>columns
#         print(chr(64+i),end=" ") # this will print the value of i followed by a space and stay on the same line
#     print() # this will print a new line after each row is printed

# 3. Input:
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1): # outer loop ==>rows
#     for j in range(1,n+1): # inner loop ==>columns
#         print("*",end=" ") # this will print the value of j followed by a space and stay on the same line
#     print() # this will print a new line after each row is printed  

#4. Input:
# A A A A A 
# B B B B 
# C C C 
# D D 
# E

# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1): # outer loop ==>rows
#     for j in range(1,n+2-i): # inner loop ==>columns
#         print(chr(64+i),end=" ") # this will print the value of i followed by a space and stay on the same line
#     print() # this will print a new line after each row is printed

#5. Input:
# Enter the number of rows: 5
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * * 

# import time
# n=int(input("Enter the number of rows: "))
# for i in range(1,n+1): # outer loop ==>rows
#     print(" "*(n-i),end="") # this will print the spaces before the stars in each row
#     for j in range(1,i+1): # inner loop ==>columns
#         time.sleep(1)
#         print("*",end=" ") # this will print the value of j followed by a space and stay on the same line
#     print() # this will print a new line after each row is printed

#===========================================================================================

#Bodmas

# a=50
# b=30
# c=20
# d=10
# print((a+b)*c/d) # this will print the result of the expression (a+b)*c/d according to the order of operations (BODMAS)
# print((a-b)*c/d) # this will print the result of the expression (a-b)*c/d according to the order of operations (BODMAS)
# print((a*b)/c-d) # this will print the result of the expression (a*b)/c-d according to the order of operations (BODMAS)

#===========================================================================================

#the special characters having no meaning are ('@','#','$','%','^','&','*','(',')','-','+','=','{','}','[',']','|','\',';',':','"',"'",'<','>','?','/'  )

#input="gasgg54@vscsdls"
#output=4

# input="gasgg54@#vscsd!s^"
# count=0
# for i in input:
#     if i in ['@','#','!','^']:
#         count+=1
# print(count)

# var='gasgg54@#vscsd!s"'
# count=0
# z=ord('0')
# print(z)
# if z>=97 and z<=122:
#     count+=1        
# elif z>=65 and z<=90:
#     count+=1
# else:
#     count+=1
# print(count)

#===========================================================================================

# input="this is a test"
# print(input.title()) # this will print the string with the first character of each word in uppercase and the rest of the characters in lowercase    

#===========================================================================================

# print('khushiakre378469'.isalpha()) # True # this will print False because the string contains numbers
# print('khushiakre'.isalpha()) # True # this will print True because the string contains only alphabets
# print('6563f'.isdigit()) # False # this will print False because the string contains alphabets
# print('6563'.isdigit()) # True # this will print True because the string contains only digits
# print('njbhfbhh'.islower()) # True # this will print True because the string contains only lowercase letters
# print('NJHBF'.isupper()) # True # this will print True because the string contains only uppercase letters
# print(' '.islower()) # False # this will print False because the string contains only a space character
# print(' '.isupper()) # False # this will print False because the string contains only a space character
# print('Khushi Akre'.istitle()) # True # this will print True because the string contains the first character of each word in uppercase and the rest of the characters in lowercase
# print(''.istitle()) # False # this will print False because the string is empty
# print(' '.isspace()) # True # this will print True because the string contains only a space character
# print("Hello".startswith('H')) # True # this will print True because the string starts with 'H'
# print("Hello".endswith('o')) # True # this will print True because the string ends with

#==========================================================================================

#Check for Pangram
# input="The quick brown fox jumps over the lazy dog"
# output="Pangram"

# input = "The quick brown fox jumps over the lazy dog"
# input = input.replace(" ", "")  # Remove spaces from the input string
# input = input.lower()  # Convert the input string to lowercase
# alphabet = "abcdefghijklmnopqrstuvwxyz"
# is_pangram = True   
# for letter in alphabet:
#     if letter not in input:
#         is_pangram = False
#         break   
# if is_pangram:
#     print("Pangram")    

#==========================================================================================

#count Words in a String 

# input="The quick brown fox jumps over the lazy dog"
# words=1
# for i in input:
#     if i==" ":
#         words+=1
# print("Number of Words: ",words)

#==========================================================================================

#Chech for Palindrome

#input="madam"
#output="madam"

# input="madam"
# print(input)
# print(input[::-1]) # this will print the string in reverse order
# if input==input[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
#==========================================================================================

#Count vowels and consonnats in a string

# vowels=['a','e','i','o','u']
# name="Khushi"
# cons=0
# vow=0
# for i in name:
#     if i in vowels:
#         vow+=1
#     else:
#         cons+=1
# print("Number of Vowels: ",vow)
# print("Number of Consonants: ",cons)

#==========================================================================================

#Check for Anagram

# input="listen" 
# print(input)
# input2="silent"
# print(input2)
# if sorted(input)==sorted(input2):
#     print("Anagram")
# else:   
#     print("Not Anagram")

#==========================================================================================

# name="Khushi"
# for i in name:
#     print(i) # this will print each character of the string in a new line

#=========================================================================================

#Remove Duplicate character from string
#input="Khushi"
#output="Khusi"

# input="khushi"
# output=""
# for i in input:
#     if i not in output:
#         output += i
# print(output) # this will print the string with duplicate characters removed

#==========================================================================================================

#Reverse a string
#input="Khushi"
#output="ihsuhK"

# input="Khushi"
# output=""
# for i in range(len(input)-1, -1, -1):
#     output+=input[i]
# print(output)

#==========================================================================================

# name="Khushi"
# sal=500000
# age=20
# print("{} sal is {} and age is {}".format(name,sal,age)) # this will print the string with the values of the variables name, sal and age using the format() method
# print("{0} sal is {1} and age is {2}".format(name,sal,age)) # this will print the string with the values of the variables name, sal and age using the format() method with positional arguments
# print("{X} sal is {Y} and age is {Z}".format(X=name,Y=sal,Z=age)) # this will print the string with the values of the variables name, sal and age using the format() method with keyword arguments
# A=1
# print(f"{A} is a Good Girl")

#=========================================================================================

# name="khushi" #this is a string
# print(name[0])# this will print the first character of the string because the index starts from 0
# print(name[1]) # this will print the second character of the string because the index starts from 0
# print(name[-1]) # this will print the last character of the string because the index -1 refers to the last character of the string
# print(name[0:5])    # this will print the string from index 0 to 4 because the end index is exclusive
# print(name[:5]) # this will print the string from index 0 to 4 because the end index is exclusive
# print(name[1:]) # this will print the string from index 1 to the end of the string
# print(name[:]) # this will print the entire string
# print(name[1:5:2]) # this will print every 2nd character from index 1 to 4
# print(name[::-1]) # this will print the string in reverse order

#==========================================================================================================

# s="Python are High Level Programming Language"
# print(s.lower()) # lower() method is used to convert all the characters of the string to lowercase
# print(s.upper()) # upper() method is used to convert all the characters of the string to uppercase
# print(s.capitalize()) # capitalize() method is used to convert the first character of the string to uppercase and the rest of the characters to lowercase
# print(s.title()) # title() method is used to convert the first character of each word in the string to uppercase and the rest of the characters to lowercase
# print(s.swapcase()) # swapcase() method is used to convert the uppercase characters to lowercase

#==========================================================================================================