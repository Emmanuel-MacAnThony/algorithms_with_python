class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

def isValidBST(root: TreeNode) -> bool:
    
    def valid(node: TreeNode, left, right):
        
        if node == None:
            return True
        
        if not ( left < node.val < right):
            return False
        
        return valid(node.right, node.val, right) and valid(node.left, left,   node.val )
    
    
    return valid(root, float("-inf"), float("inf"))