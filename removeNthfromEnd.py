def removeNthFromEnd(self, head, n):
    i = 0 
    temp1 = head 
    while head:
        i+=1
        head = head.next
    
    head = temp1 
    
    
    
    if n == i:
        head = head.next
        return head
    
    nodeNum = i-n 
    target_length = 1
    
    while target_length < nodeNum:
        target_length += 1
        head = head.next
    
    if head:
        head.next = head.next.next
    
    return temp1
    
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    
