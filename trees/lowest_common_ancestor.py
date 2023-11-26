class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
        
"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.
According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
def lowest_common_ancestor(root: TreeNode, p:TreeNode, q: TreeNode):
    
    while True:
        
        if root.val > p.val and root.val > q.val:
            root = root.left
            
        elif root.val < p.val and root.val < q.val:
            root = root.right

        else:
            return root