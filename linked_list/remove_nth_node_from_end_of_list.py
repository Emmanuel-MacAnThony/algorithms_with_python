from typing import Dict, Optional

"""Given the head of a linked list, remove the nth node from the end of the list and return its head."""
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
def removeNthFromEnd(self, head: ListNode, n: int):
    
    """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
    """
    
    listmap: Dict[int, Optional[ListNode]] = {}
    listmap[-1] = ListNode() # dummy node
    count = 0
    current = head
    
    while current:
        listmap[count] = current
        count += 1
        current = current.next
        
    lengthOfList = count
    indexOfNodeToBeDeleted = lengthOfList - 1
    
    listmap[indexOfNodeToBeDeleted - 1].next = listmap[indexOfNodeToBeDeleted].next
    listmap[indexOfNodeToBeDeleted] = None
    
    if listmap[0] == None:
        listmap[1] = listmap.get(1, None)
        return listmap[1]
    
    else:
        return listmap[0]
    
        
    
    
    
    
    