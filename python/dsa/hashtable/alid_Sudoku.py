class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_map, col_map, sub_box_map = defaultdict(set), defaultdict(set), defaultdict(set)

        def valid(row, col):
            value = board[row][col]
            sub_box = (row//3, col//3)
            if value in row_map[row] or value in col_map[col] or value in sub_box_map[sub_box]:
                return False
            
            row_map[row].add(value)
            col_map[col].add(value)
            sub_box_map[sub_box].add(value)
            
            return True
            
        for row in range(0, 9):
            for col in range(0, 9):
                if board[row][col] == ".":
                    continue
                elif not valid(row, col):
                    return False
                
        return True

# TC: O(1)
# SC: O(1)