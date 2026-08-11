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
        seen = set()
        for i in range(3):
            for j in range(3):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(3,6):
            for j in range(3):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(6,9):
            for j in range(3):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(3):
            for j in range(3,6):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(3,6):
            for j in range(3,6):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(6,9):
            for j in range(3,6):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(3):
            for j in range(6,9):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(3,6):
            for j in range(6,9):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        seen = set()
        for i in range(6,9):
            for j in range(6,9):
                if (board[i][j] == "."):
                    continue
                if (board[i][j] in seen):
                    return False
                    break
                seen.add(board[i][j])
        return True
        
