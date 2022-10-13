def findBall(self, grid):
        #one ball a time - how would I logically tackle this problem 
        #its a tree so based on the first grid value it goes to the next and check until its hit the final row value or 
        
        #ways to get down -> check for the line next to it on the left if the value -1 -> if that is 1 then set that value to -1 
        
        #if it does all this and it reaches len[grid] then return the column number
        flag = True
        n=len(grid[0]) # no of cols
        m=len(grid) # no of rows
        res=[-1 for _ in range(n)] 

        for a in range(n):
                i=a
                f=True   
                for j in range(m):
                        if grid[j][i]==1:
                                if i+1>=n: 
                                        flag=False
                                        break
                                if i+1<n and grid[j][i+1]==-1: 
                                        flag=False
                                        break
                                i+=1
                        else:
                                if i-1<0:
                                        flag=False
                                        break
                                if i-1>=0 and grid[j][i-1]==1: 
                                        flag=False
                                        break
                                i-=1
                if flag: 
                        res[a]=i
                else : res[a]=-1
        return res
    
