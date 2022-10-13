def spiralOrder(self, matrix):
    #edge case
    returnList = []
    if (len(matrix) == 0):
        return returnList

    
    C = len(matrix)
    R = len(matrix[0])
    
    #creating a new matrix of empty see variables
    seen = [[0 for i in range(R)] for j in range(C)]
    
    #traversing values 
    x = 0
    y = 0
    
    #create a set of movements 
    dr = [0,1,0,-1]
    dc = [1, 0, -1, 0]
    
    #what is current direction 
    di = 0 
    
    for i in range(C*R):
        returnList.append(matrix[x][y])
        seen[x][y] = True #will make it so we can check if we saw it                 already
        cr = x + dr[di]
        cc = y + dc[di]
        
        if (0 <= cr and cr < C and 0 <= cc and cc < R and not(seen[cr][cc])):
            x = cr
            y = cc
        else:
            di = (di + 1) % 4
            x += dr[di]
            y += dc[di]
    return returnList
        
    
                
    #starting from the list 
    #see if there is a command for if matrix is empty 
    #check to see if the 
    
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    
