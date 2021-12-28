class Solution(object):
    def addBinary(self, a, b):
        a = int(a,2)
        b = int(b,2)
        sum = bin(a+b)
        return sum[2:]
        """
        :type a: str
        :type b: str
        :rtype: str
        """ 
        
