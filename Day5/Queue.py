#Queue DS:-
# 1. EnQueue
# 2. DeQueue
# 3. 

#=======================================================================================

import sys
class Queue:
    def __init__(self, size):
        self.myQueue = [] #Creating Stack
        self.queueSize = size # Stack size defined

    def isFull(self):
        if len(self.myQueue) == size:
            return True
        else:
            return False
    
    def enQueue(self, value):
        if self.isFull():
            print("Queue is Full ")
        else:
            self.myQueue.append(value)
            print(value ," is Append")

    def display(self):
        print(self.myQueue)
    
    def isEmpty(self):
        if self.myQueue == []:
            return True
        else:
            return False
        
    def deQueue(self):
        if self.isEmpty():
            print("Deletion Not Possible Because Queue is Empty !!!")
        else:
            self.myQueue.pop(0)
            print("Element deleted ")

    def peek(self):
        if self.isEmpty():
            print("Queue is Empty !!!")
        else:
            print(self.myQueue[0])

    def deleteQueue(self):
        self.myQueue = None

size = int(input("Enter the Size of Queue : "))
obj =Queue(size)
print("Queue has Created : ")
while(True):
    print("==========================Queue=============================")
    print("1. EnQueue Operation :")
    print("2. Display Queue :")
    print("3. DeQueue Operation :")  #DeQueue - delete element
    print("4. Peek Operation :")
    print("5. Delete Queue :")
    print("6. Exist ")
    print("=============================================================")
    choice = int(input("Enter Your Choice : "))
    if choice == 1:
        value = int(input("Enter the value to add in Queue : "))
        obj.enQueue(value)
        
    elif choice == 2:
        obj.display()

    elif choice == 3:
        obj.deQueue()

    elif choice == 4:
        obj.peek()
    
    elif choice == 5:
        obj.deleteQueue()
        print("Queue is Deleted !!!!!!!!!!")


#===================================================================================

#                          time complexity     Space Complexity
#Create Queue                   O(1)                O(1)
#EnQueue                     O(1)/ O(n)             O(1)
#DeQueue                     O(1)/ O(n)             O(1)
#peek                           O(1)                O(1)
#isEmpty                        O(1)                O(1)
#Delete Entire Queue            O(1)                O(1)

#===================================================================================

#Queue using LinkedList
# - Fast performance
# - Implementation is not Easy

#Queue using List
# - Easy to implement
# - Speed problem when it grows