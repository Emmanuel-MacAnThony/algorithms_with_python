class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
"""Given the root of a binary tree, invert the tree, and return its root."""
def inver_binary_tree(root: TreeNode):
    
    if root == None:
        return ;
    
    root.left, root.right = root.right, root.left
    
    inver_binary_tree(root.left)
    inver_binary_tree(root.right)
    
    return root