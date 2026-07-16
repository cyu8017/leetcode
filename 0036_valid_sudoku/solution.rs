// LeetCode 0036 - Valid Sudoku
// https://leetcode.com/problems/valid-sudoku/

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        let mut rows = [[false; 9]; 9];
        let mut cols = [[false; 9]; 9];
        let mut boxes = [[false; 9]; 9];

        for r in 0..9 {
            for c in 0..9 {
                let ch = board[r][c];
                if ch == '.' {
                    continue;
                }

                let digit = (ch as u8 - b'1') as usize;
                let box_idx = (r / 3) * 3 + c / 3;
                if rows[r][digit] || cols[c][digit] || boxes[box_idx][digit] {
                    return false;
                }

                rows[r][digit] = true;
                cols[c][digit] = true;
                boxes[box_idx][digit] = true;
            }
        }

        true
    }
}
