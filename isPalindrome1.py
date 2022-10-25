# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
def isPalindrome(self, head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res == res[::-1]

    #need to traverse both sides of the list 
    #so find the middle of the list which is length
    #then make sure its equal 
    """
    :type head: ListNode
    :rtype: bool
    """


