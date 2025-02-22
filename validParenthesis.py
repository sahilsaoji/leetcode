#Using a stack

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        openList = ["(","[","{"]
        closeList = [")","]","}"]
        for i in s:
            if i in openList:
                stack.append(i)
            elif i in closeList:
                whichIndex = closeList.index(i)
                if ((len(stack)>0) and openList[whichIndex]== stack[len(stack)-1]):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False

        
        