class Node(object):
    def __init__(self,data):
        self.data=data
        self.leftChild=None
        self.rightChild=None

class BinarySearchTree(object):
    def __init__(self):
        self.root=None

    def insert(self,data):
        if not self.root:
            self.root=Node(data)
        else:
            self,insertNode(data,self.root)
    #O(logN)  if the tree is balanced; if the tree is not balanced  --->  O(N)  , AVL RBT are needed
    def insertNode(self,data,node):
        if data<node.data:
            if node.leftChild:
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild=Node(data)

        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild=Node(data)


