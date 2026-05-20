#=======================================================================================

# #Linked List
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
# 
# class Linkedlist:
#     def __init__(self):
#         self.head = None
# 
# linkedlist = Linkedlist()
# 
# linkedlist.head = Node(5)
# second = Node(10)
# third = Node(15)
# fourth = Node(20)
# 
# #Connecting nodes
# linkedlist.head.next = second
# second.next = third
# third.next = fourth
# 
# #display linkedlist
# while linkedlist.head != None:
#     print(linkedlist.head.data, "|",linkedlist.head.next,"->",end=" ")
#     linkedlist.head = linkedlist.head.next

#=======================================================================================

class Node:
    def __init__(self, data):
        self.data = data #instance variable
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, value):
        self.node =Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.tail.next = self.node
            self.tail = self.node

    def addnodeBegeinning(self, value):
        print(" Add Node to Begeinning : ")
        self.node = Node(value)
        if self.head is None:
            self.head = self.node
            self.tail = self.node
        else:
            self.node.next = self.head
            self.head = self.node

    def addNodeBetween(self, index, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        elif index == 0:
            node.next = self.head
            self.head = node
        else:
            temp = self.head
            for _ in range(index-1):
                temp = temp.next
            node.next = temp.next
            temp.next = node


    def DisplayNode(self):
        while self.head is not None:
            print(self.head.data, '|' , self.head.next, '->',end = ' ')
            self.head =self.head.next


if __name__ == '__main__':
    object = LinkedList() #Linked list object created
    while True:
        print("1. Add Node LinkedList : ")
        print("2. Add Node in Begining : ")
        print("3. Add Node in Between : ")
        print("4. Add Node in End : ")
        print("5. Display LinkedList : ")
        print("6. Exit : ")
        ch = int(input("Enter Your Choice : "))
        if ch == 1:
            value = int(input("Enter value for node : "))
            object.addNode(value)
            print("Node added Successfully in single LinkedList")
        elif ch == 2:
            value = int(input("Enter value for Node : "))
            object.addnodeBegeinning(value)
            print("Node added Successfully in single LinkedList")
        elif ch == 5:
            object.DisplayNode()
