from collections import deque
from typing import Deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
"""Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level)."""

def level_order(root: TreeNode):
    
    q: Deque[TreeNode]  = deque()
    
    res = []
    
    if root:
        q.append(root)
        
    while q:
        
        val = []
        
        for i in range(len(q)):
            
            node = q.popleft()
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
                
            
            val.append(node.val)
            
        res.append(val)
    
    
    return res