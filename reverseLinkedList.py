# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #creating a prev pointer
        prev = None
        #creating a copy of the linkedlist
        curr = head
        while(curr):
            #create a tempvariable that is the pointer to the next in list
            next = curr.next
            #Make the actual current next that into a previous pointer 
            curr.next = prev
            #that way previous value is new head and the current is the next 
            prev = curr
            curr = next
        return prev
        #     push(backwardlist, current_node.val)
        #     #backwardlist.insert(0,current_node.val)
        #     current_node = current_node.next
        # return backwardlist
        