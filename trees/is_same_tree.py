class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
"""
def is_same_tree(p:TreeNode, q:TreeNode):
    if p == None and q == None:
        return True
    
    if p and q and p.val == q.val:
        return is_same_tree(p.right, q.right) and is_same_tree(p.left, q.left)
    else:
        return False
    
    
