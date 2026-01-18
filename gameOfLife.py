class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # 8 possible directions
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]
        #Rules 
        #To die -> if cell is 1 and in all directions if there is less than 2 cells with 1, you mark it as 0
        #To live -> if cell is 0 and in all directions there is exactly three live neighbors they are marked it as 1
        #how to do live translations -> we need a copy of the live board and the new board?


        for row in range(len(board)):
            for column in range(len(board[row])):
                liveNeighborCount = 0
                for dr, dc in directions:
                    r = row + dr
                    c = column + dc

                    if 0 <= r < len(board) and 0 <= c < len(board[0]):
                        if board[r][c] == 1 or board[r][c] == -1:
                            liveNeighborCount += 1

                if board[row][column] == 1 and liveNeighborCount < 2:
                    board[row][column] = -1
                elif board[row][column] == 1 and liveNeighborCount > 3:
                    board[row][column] = -1
                elif board[row][column] == 0 and liveNeighborCount == 3:
                    board[row][column] = 2
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == -1:
                    board[r][c] = 0
                elif board[r][c] == 2:
                    board[r][c] = 1
                        