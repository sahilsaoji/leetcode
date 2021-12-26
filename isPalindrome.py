class Solution(object):
    def isPalindrome(self, x):
        if x>0:
            number = x 
            reverseX = "" 
            while(x>0):
                temporary = x%10
                reverseX = reverseX + str(temporary)
                #print(reverseX)
                x = x//10
            if int(reverseX) == number:
                return True
            else:
                return False
        elif (x==0):
            return True
        else:
            return False

        """
        :type x: int
        :rtype: bool
        """
        
