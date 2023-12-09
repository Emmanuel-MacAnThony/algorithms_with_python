from typing import List

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree."""

def kthSmallest(root:TreeNode, k:int) -> int:
    
    stack: List[TreeNode] = []
    curr = root
    
    while curr or stack:
        while curr:
            curr = curr.left
            stack.append(curr)
            
        curr = stack.pop()
        k -= 1
        
        if k == 0:
            return curr.val
        
        curr = curr.right