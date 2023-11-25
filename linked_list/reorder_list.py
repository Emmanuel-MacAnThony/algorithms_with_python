"""
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
"""

class ListNode(object):
    
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        
        
def reorder_list(head: ListNode):
    
    current = head
    listmap = {}
    count = 0
    
    while current:
        listmap[count] = current
        count += 1
        current = current.next
        
    divider = count // 2
    marker = 0
    
    # set middle node
    if count % 2:
        midnode = listmap[divider]
    else:
        midnode = None
    
        
    while marker < divider:
        listmap[marker].next = listmap[count - marker - 1]
        listmap[count - marker - 1].next = listmap[marker + 1]
        marker += 1
        
    if count == 1:
        return listmap[0]
    
    # make sure  the midnode is the tail
    marker -= 1
    listmap[count - marker - 1].next = midnode
    
    if count % 2:
        midnode.next = None
        
    return listmap[0]
    
    
    