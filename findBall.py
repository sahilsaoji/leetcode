def findBall(self, grid):
        #one ball a time - how would I logically tackle this problem 
        #its a tree so based on the first grid value it goes to the next and check until its hit the final row value or 
        
        #ways to get down -> check for the line next to it on the left if the value -1 -> if that is 1 then set that value to -1 
        
        #if it does all this and it reaches len[grid] then return the column number
        m = len(grid)
        n = len(grid[0])
        res = [-1] * n
        for col in range(n):
            i = col
            row = 0
            # the ball falling process simulation
            while row < m:
                val = grid[row][col]
                col += val
                # the ball gets stuck at the left or at the right border
                if not 0 <= col < n:
                    break
                # the ball gets stuck at a "V" shaped pattern
                if grid[row][col] != val:
                    break
                # the ball falls to the next row
                row += 1
            if row == m: res[i] = col
        return res
    
