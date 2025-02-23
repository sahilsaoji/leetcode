class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        myStack = []   
        cur = ""
        for i in path + "/":
            if i=="/":
                if cur == "..":
                    if myStack: myStack.pop()
                elif cur != "" and cur != ".":
                    myStack.append(cur)
                cur = ""
            else:
                cur += i
        return "/" + "/".join(myStack)
        