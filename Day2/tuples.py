#==================================================================================================================

# mytuple=("khushi","Vaibhav","Pooja","Chintu","Chanchal","Rahul")
# print(mytuple)
# print(type(mytuple))

# mytuple[2]="Prathamesh"   #we cannot change the value of tuple because it is immutable
# print(mytuple)
#==================================================================================================================

#Q-1.

# init_tuple=()
# print(init_tuple.__len__())   #length of tuple is 0

#Q-2.

# init_tuple_a='a','b'
# init_tuple_b='a','b'
# print(init_tuple_a==init_tuple_b)   #True because both the tuples have same values

#Q-3.

# init_tuple_a='1','2'
# init_tuple_b=('3','4')
# print(init_tuple_a+init_tuple_b)   #('1', '2', '3', '4') because we can concatenate two tuples

#Q-4.

# l=[1,2,3]
# init_tuple=('Python',)* (l.__len__() -l[::-1][0])  #('Python', 'Python', 'Python') because we can repeat the tuple by multiplying it with an integer
# print(init_tuple)

#Q-5.

# init_tuple=('Python',)* 3
# print(type(init_tuple))   

#Q-6.

# init_tuple=(1,)*3
# init_tuple[0]=2
# print(init_tuple)   #TypeError: 'tuple' object does not support item assignment because we cannot change the value of tuple

#Q-7.

init_tuple=((1,2),)*7
print(init_tuple)   
print(len(init_tuple[3:8]))   #4

#=====================================================================================================

