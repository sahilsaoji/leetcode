def longestCommonPrefix(self, strs):
    #how to find the common prefix among the input strings 
    #create a variable prefix 
    #assign it to the first word - and then cut if the characters are not in the word

    #edge cases
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    
    #sort the list first
    strs.sort()

    #create a minimum amount of length for the amount a prefix can be
    end = min(len(strs[0]),len(strs[len(strs)-1]))
    
    i = 0
    #find a value less than n and that would work for a comparison 
    while(i < end and strs[0][i] == strs[len(strs) - 1][i]):
        i += 1
    
    #find the prefix that works for that
    pre = strs[0][0:i]
    
    return pre
    
    
    
    
    """
    :type strs: List[str]
    :rtype: str
    """
    
