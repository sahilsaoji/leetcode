# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        #compare the head of one list with the other 
        #if the val at that head is less than the other have to push that one after that one by making that the value and then go backward 
        #problem of how do you know which is longer than the other 
        #you have to continue based on whether each has a next node or not
        #if list1 value is greater than list2 value 

        #create a new two pointer list where the head = tail 
        head = ListNode()
        tail = head
        while list1 is not None and list2 is not None:
            #iterates while neither list is done 
            if list1.val < list2.val:
                #does the swap if the value of list2 is greater than the value of list1
                tail.next = list1
                #changes the next of this list to be that of list1 
                list1 = list1.next
                #iterate through the list 
                tail = tail.next
                #iterate through the tail 
            else: #same thing with the list2 value 
                tail.next = list2
                list2 = list2.next
                tail = tail.next

        #this solves any problem with list1 or list2 size problem
        tail.next = list1 if list1 is not None else list2
        return head.next



        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        