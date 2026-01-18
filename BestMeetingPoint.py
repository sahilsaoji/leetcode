class Solution(object):
    def minTotalDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        #This problem works by solving the median for all points
        #if this was one dimensional, we would just find the median of all the x values and that would be the best meeting point
        #But because this is two dimensional and we're using manhattan distance, we just have to treat the rows and columns seperately and find the median for each and the (xMedian, yMedian) is the perfect median point 
        
        #finding the row value and column value for each house
        rowVals = []
        columnVals = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    rowVals.append(row)
                    columnVals.append(col)
        
        #finding the median of the rows
        rowVals.sort()
        m = len(rowVals) // 2
        rowMedian = rowVals[m]

        #finding the median of the rows
        columnVals.sort()
        n = len(columnVals) // 2
        colMedian = columnVals[n]
        
        #calculating distance to this median point
        distance = 0
        for i in range(len(rowVals)):
            distance += abs(rowVals[i] - rowMedian)
            distance += abs(columnVals[i] - colMedian)

        return distance
        


