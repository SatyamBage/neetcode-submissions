from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                items = board[i][j]
                if items in s:
                    return False
                elif items != ".":
                    s.add(items)

        for i in range(9):
            s = set()
            for j in range(9):
                items = board[j][i]
                if items in s:
                    return False
                elif items != ".":
                    s.add(items)

        starts = [(0, 0), (0, 3), (0, 6),
                 (3, 0), (3, 3), (3, 6),
                 (6, 0), (6, 3), (6, 6)]
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    items = board[row][col]
                    if items in s:
                        return False
                    elif items != ".":
                        s.add(items)
        return True
 

        