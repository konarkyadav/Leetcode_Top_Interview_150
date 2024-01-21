# Reference: https://www.youtube.com/watch?v=fei4bJQdBUQ&ab_channel=NeetCode
class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def count(r,c): 
            cnt = 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if ((i==r and j==c) or
                        i==rows or j==cols or i<0 or j<0  
                       ):
                        continue 
                    if board[i][j] == 1 or board[i][j] == 3: 
                        cnt+=1 
            return cnt
        rows, cols = len(board),len(board[0]) 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1: 
                    neighbours = count(i,j) 
                    if neighbours < 2 or neighbours > 3 : 
                        board[i][j] = 3 
                if board[i][j] == 0:
                    neighbours = count(i,j) 
                    if neighbours == 3:
                        board[i][j] = 2 
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 2: 
                    board[i][j] = 1 
                if board[i][j] == 3:
                    board[i][j] = 0

