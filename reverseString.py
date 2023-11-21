class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        #iterate through the array and create a temporary value for the current value, then find the backend value for it at the end and substitute it in 
        # if len(s)%2 == 0:
        #     backwardpointer = len(s)-1
        #     for i in range(len(s)/2):
        #         temp = s[i]
        #         s[i] = s[backwardpointer]
        #         s[backwardpointer] = temp
        #         backwardpointer-=1
        #         print(s)
        #     return s
        # else:
        #     backwardpointer = len(s)-1
        #     for i in range(len(s)/2-1):
        #         temp = s[i]
        #         s[i] = s[backwardpointer]
        #         s[backwardpointer] = temp
        #         backwardpointer-=1
        #         print(s)
        #     return s

#Hello is len(5)
#H[0] will swap with o[4]
#e[1] will swap with l[3]
#l[2] will swap with l[2]

        i = 0 
        j = len(s) - 1
        while i < j:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i+=1
            j-=1