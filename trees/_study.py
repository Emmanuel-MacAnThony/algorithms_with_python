from typing import List

class RootNode(object):
    
    def __init__(self, rootObj, left=None, right=None):
        self.key = rootObj
        self.leftChild = left
        self.rightChild = right
        
    def insertLeft(self, newNode):
        
        if self.leftChild == None:
            self.leftChild = RootNode(newNode)
        else:
            t = RootNode(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = RootNode(newNode)
        else:
            t = RootNode(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
            
    def getRightChild(self):
        return self.rightChild
    
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRootVal(self, obj):
        self.key = obj
        
    def getRootVal(self):
        return self.key
    
        
# representing a tree as a list of lists

def BinaryTree(r):
    return [r, [], []]


def inserLeft(root: List[list & any], newBranch):
    
    t = root.pop(1)
    
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    
    else:
        root.insert(1, [newBranch, [], []])
    
    return root


def inserRight(root: List[list | any], newBranch):
    
    t = root.pop(2)
    
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    
    else:
        root.insert(2, [newBranch, [], []])
    
    
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root, newVal):
    root[0] = newVal
    
def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

