class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""
Given the root of a binary tree, return its maximum depth.
A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""
def maxDepth(root: TreeNode):
    
    maxdepth = 1
    
    if root == None:
        return 0
    
    else:
        leftDepth = 1 + maxDepth(root.left)
        rightDepth = 1 + maxDepth(root.right)
        maxdepth = max(leftDepth, rightDepth)
        
    return maxdepth