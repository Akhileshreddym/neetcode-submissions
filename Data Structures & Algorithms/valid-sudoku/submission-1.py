class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #For Rows First
        for i in range(9):
            seen = set()
            for j in range(9):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        
        #For Columns:
        for i in range(9):
            seen = set()
            for j in range(9):
                if (board[j][i] == "."):
                    continue
                if (board[j][i] in seen):
                    return False
                    break
                seen.add(board[j][i])
        
        #For Sub Boxes:
        for rows in range(0,9,3):
            for columns in range(0,9,3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        row = rows + i
                        col = columns + j
                        if (board[row][col] == "."):
                            continue
                        if (board[row][col] in seen):
                            return False
                            break
                        seen.add(board[row][col])
        return True
        
