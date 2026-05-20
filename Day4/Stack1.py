#Stack implementation without size limit
# Stack implementation 
# 1. list/array
# 2.linkedlist



import sys
class Stack:
    def __init__(self):
        self.myStack = []  #creating stack

    def push(self,value):
        self.myStack.append(value)
        print("Element Push")

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty !!!!!")
        else:
            print(self.myStack.pop())

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty ")
        else:
            print(self.myStack[-1])

    def deleteStack(self):
        self.myStack = None

    def display(self):
        print(self.myStack)

obj = Stack() 
print("Stack has Created : ")
while True:
    print("1. PUSH Operation : ")
    print("2. Display Stack : ")
    print("3. POP Operation : ")
    print("4. PEEK Operation : ")
    print("5. Delete Operation : ")
    print("7. Exit")
    choice =int(input("Enter Your Choice : "))
    if choice == 1:
        value = int(input("Enter value to push in Stack : "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deleteStack()
    else:
        sys.exit()

#======================================================================================

#Stack implementation with size limit
# Stack implementation 
# 1. list/array
# 2.linkedlist

import sys
class Stack:
    def __init__(self,size):
        self.myStack = []  #creating stack
        self.stackSize = size # Stack size defined

    def isFull(self):
        if len(self.myStack) == self.stackSize:
            return True
        else:
            return False

    def push(self,value):
        if self.isFull():
            print("Stack is Full ")
        else:
            self.myStack.append(value)
            print("Element Push")

    def pop(self):
        if self.isEmpty():
            print("Stack is Empty !!!!!")
        else:
            print(self.myStack.pop())

    def isEmpty(self):
        if self.myStack == []:
            return True
        else:
            return False
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty ")
        else:
            print(self.myStack[-1])

    def deleteStack(self):
        self.myStack = None

    def display(self):
        print(self.myStack)

size=int(input("Enter the Size of Stack : "))
obj = Stack(size) 
print("Stack has Created : ")
while True:
    print("1. PUSH Operation : ")
    print("2. Display Stack : ")
    print("3. POP Operation : ")
    print("4. PEEK Operation : ")
    print("5. Delete Operation : ")
    print("7. Exit")
    choice =int(input("Enter Your Choice : "))
    if choice == 1:
        value = int(input("Enter value to push in Stack : "))
        obj.push(value)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.pop()
    elif choice == 4:
        obj.peek()
    elif choice == 5:
        obj.deleteStack()
    else:
        sys.exit()


