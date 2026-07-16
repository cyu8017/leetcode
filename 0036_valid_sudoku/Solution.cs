// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

public class Solution {
    public bool IsValidSudoku(char[][] board) {
        var rows = new HashSet<char>[9];
        var cols = new HashSet<char>[9];
        var boxes = new HashSet<char>[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<char>();
            cols[i] = new HashSet<char>();
            boxes[i] = new HashSet<char>();
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char value = board[r][c];
                if (value == '.') {
                    continue;
                }

                int box = (r / 3) * 3 + c / 3;
                if (rows[r].Contains(value) || cols[c].Contains(value) || boxes[box].Contains(value)) {
                    return false;
                }

                rows[r].Add(value);
                cols[c].Add(value);
                boxes[box].Add(value);
            }
        }

        return true;
    }
}
