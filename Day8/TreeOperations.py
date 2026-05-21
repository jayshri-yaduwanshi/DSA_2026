#======================================================================================

#Types of Binary Tree
#  |- Full Binary Tree
#          |-Each node has either 0 or 2 children
#          |-No node has a single child
#  |- Complete Binary Tree
#          |- All levels excepts possibly the last are completely filled
#          |- Nodes in the level are filled from left too right
#  |- Perfect Binary Tree
#          |- All internal nodes have exactly two nodes
#          |- All leaf nodes are at the same level
#======================================================================================
#  |- Operations of Tree
#          |- Creation of Tree
#          |- Insertion of a node
#          |- Deletion of a node
#          |- Search for a value
#          |- Traverse all nodes
#               |- Depth first Search
#                    |- Preorder Traversal (root , left , right)
#                    |- Inorder Traversal (left , root, right)
#                    |- Postorder Traversal (left , right, root)
#               |- Breadth first Search
#                    |- level by level Traversal 
#          |- Deletion of Tree

#======================================================================================

#Interview Question
#Why Binary Search Tree??
#  |-Ans: It performs faster than Binary Tree when inserting and deleting node

#======================================================================================

class BSTNode:
    def __init__(self , data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
newBST = BSTNode(None)

def insertNode(rootNode , nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.rightChild, nodeValue)

def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.data, end=" ")
    preOrderTraversal(rootNode.rightChild)
    

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    preOrderTraversal(rootNode.rightChild)
    print(rootNode.data, end=" ")


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("The Value is Found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild.data == nodeValue:
            print("The Value is Found")
        else:
            searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild.data == nodeValue:
            print("The Value is Found")
        else:
            searchNode(rootNode.rightChild, nodeValue)

insertNode(newBST , 70)
insertNode(newBST , 50)
insertNode(newBST , 90)
insertNode(newBST , 30)
insertNode(newBST , 60)
insertNode(newBST , 80)
insertNode(newBST , 100)
insertNode(newBST , 20)
insertNode(newBST , 40)
insertNode(newBST , 10)

print("Preorder Traversal : ")
preOrderTraversal(newBST)
print()
print("Inorder Traversal : ")
inOrderTraversal(newBST)
print()
print("Postorder Traversal : ")
postOrderTraversal(newBST)
print()
value =int(input(("Enter Value to Search : ")))
searchNode(newBST, value)