def minimumAbsDifference(arr):
    minimum = float('inf')
    arr.sort()
    for i in range(len(arr)-1):
        minimum = min(minimum, arr[i+1] - arr[i])
    newList = []
    for i in range(len(arr)-1):
        j=i+1
        if arr[j]-arr[i] == minimum:
            newList.append([arr[i],arr[j]])
    
    #newList.sort()
    
    return(newList)
    
    
    
    #for i in range(len(arr)-1):
        #diff = i[1]-i[0]
        
    #return(newNewList)
    
    

    """
    :type arr: List[int]
    :rtype: List[List[int]]
    """
    
print(minimumAbsDifference([3,4,5,1]))
