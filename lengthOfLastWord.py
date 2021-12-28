class Solution(object):
    def lengthOfLastWord(self, s):
        listS = s.split()
        counter = 0
        for i in listS[len(listS)-1]:
            #print(i)
            counter+=1
        return counter
        #for i in s.split():
            
            
        """
        :type s: str
        :rtype: int
        """
        
