"""Given the head of a singly linked list, reverse the list, and return the reversed list."""
class ListNode(object):
    
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next
        
def reverse_linked_list(head: ListNode):
    
    prev = None
    current = head
    
    while current:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
        
    return prev



