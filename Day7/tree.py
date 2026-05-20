#Tree is represent by using linkedlist and array
#python list(Array)

class Tree:
    def __init__(self, data):
        self.data = data
        self.child = []

    def addChild(self, obj):
        self.child.append(obj)
        print("Tree Node added")

    # custom recursive function
    def display(self, level=0):
        ret = "  " * level + str(self.data) + "\n"

        for ch in self.child:
            ret += ch.display(level + 1)

        return ret

    # string method
    def __str__(self):
        return self.display()


rootNode = Tree("Drinks")

Hot = Tree("Hot")
Cold = Tree("Cold")

Tea = Tree("Tea")
Coffee = Tree("Coffee")

NonAlcolic = Tree("NonAlcholic")
Alcolic = Tree("Alcholic")


rootNode.addChild(Hot)
rootNode.addChild(Cold)

Hot.addChild(Tea)
Hot.addChild(Coffee)

Cold.addChild(NonAlcolic)
Cold.addChild(Alcolic)


print(rootNode)

#print kroge tho yeh string method call honga

#====================================================================================
#                                 Time Complexity     Space Complexity
# Creation                             o(1)                 O(1)
# Insertion                            o(n)                 O(1)
# Searching                            o(n)                 O(1)
# Traversing                           o(n)                 O(1)
# Deletion of a node                   o(n)                 O(1)
# deletion ofd linked list             o(1)                 O(1)