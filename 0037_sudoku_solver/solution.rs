// LeetCode 0037 - Sudoku Solver
// https://leetcode.com/problems/sudoku-solver/

impl Solution {
    pub fn solve_sudoku(board: &mut Vec<Vec<char>>) {
        let mut rows = [[false; 9]; 9];
        let mut cols = [[false; 9]; 9];
        let mut boxes = [[false; 9]; 9];
        let mut empty = Vec::new();

        for r in 0..9 {
            for c in 0..9 {
                let ch = board[r][c];
                if ch == '.' {
                    empty.push((r, c));
                    continue;
                }
                let digit = (ch as u8 - b'1') as usize;
                let box_idx = (r / 3) * 3 + c / 3;
                rows[r][digit] = true;
                cols[c][digit] = true;
                boxes[box_idx][digit] = true;
            }
        }

        fn backtrack(
            board: &mut Vec<Vec<char>>,
            rows: &mut [[bool; 9]; 9],
            cols: &mut [[bool; 9]; 9],
            boxes: &mut [[bool; 9]; 9],
            empty: &[(usize, usize)],
            index: usize,
        ) -> bool {
            if index == empty.len() {
                return true;
            }

            let (r, c) = empty[index];
            let box_idx = (r / 3) * 3 + c / 3;
            for digit in b'1'..=b'9' {
                let d = (digit - b'1') as usize;
                if rows[r][d] || cols[c][d] || boxes[box_idx][d] {
                    continue;
                }

                board[r][c] = digit as char;
                rows[r][d] = true;
                cols[c][d] = true;
                boxes[box_idx][d] = true;

                if backtrack(board, rows, cols, boxes, empty, index + 1) {
                    return true;
                }

                board[r][c] = '.';
                rows[r][d] = false;
                cols[c][d] = false;
                boxes[box_idx][d] = false;
            }

            false
        }

        backtrack(board, &mut rows, &mut cols, &mut boxes, &empty, 0);
    }
}
