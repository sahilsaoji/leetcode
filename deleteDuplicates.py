# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        #print(head)
        #print(head.val)
        #print(head.next)
        #print(head.next.val)
        
        
        currentVal = head 
        prev = currentVal 
        currentVal = currentVal.next
        while currentVal:
            if prev.val == currentVal.val:
                prev.next = currentVal.next
                currentVal = currentVal.next
            else:
                prev = currentVal
                currentVal = currentVal.next
        return head

    
    
    
    
    
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
