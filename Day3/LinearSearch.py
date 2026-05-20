# def linearSearch(array,target):
#     for i in range(0,len(array)): #i=0
#         if array[i] == target:
#             return i

# array=[1,2,3,4,8,7,9]
# target=7 # search the target value i.e 7
# result =linearSearch(array,target)
# if result == -1:
#     print("Target value not found ")
# else:
#     print("Element Found at index ", result)

#===================================================================================

# removing spaces from the string :
# 1. rstrip() =====>To remove Spaces at right hand side 
# 2. lstrip() =====>To remove spaces at left hand side
# 3. strip() =====>To remove spaces both side 

city=input("Enter Your city :")
scity=city.strip()
if scity =='Hydrabad':
    print("Hello Hydrabad .. Adab")
elif scity =='Chennai':
    print("Hello Madrasi...Vanakkam")
elif scity == 'Banglore':
    print("Hello Kannadiga...Shubhodaya")
else:
    print("Your entered city is invalid")