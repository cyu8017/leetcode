// LeetCode 0051 - N-Queens
// https://leetcode.com/problems/n-queens/

use std::collections::HashSet;

impl Solution {
    pub fn solve_n_queens(n: i32) -> Vec<Vec<String>> {
        let n = n as usize;
        let mut result = Vec::new();
        let mut cols = HashSet::new();
        let mut diag1 = HashSet::new();
        let mut diag2 = HashSet::new();
        let mut board = vec![".".repeat(n); n];

        fn backtrack(
            row: usize,
            n: usize,
            board: &mut [String],
            cols: &mut HashSet<usize>,
            diag1: &mut HashSet<usize>,
            diag2: &mut HashSet<isize>,
            result: &mut Vec<Vec<String>>,
        ) {
            if row == n {
                result.push(board.to_vec());
                return;
            }

            for col in 0..n {
                if cols.contains(&col)
                    || diag1.contains(&(row + col))
                    || diag2.contains(&((row as isize) - (col as isize)))
                {
                    continue;
                }

                cols.insert(col);
                diag1.insert(row + col);
                diag2.insert((row as isize) - (col as isize));

                let mut row_chars: Vec<char> = board[row].chars().collect();
                row_chars[col] = 'Q';
                board[row] = row_chars.into_iter().collect();

                backtrack(row + 1, n, board, cols, diag1, diag2, result);

                cols.remove(&col);
                diag1.remove(&(row + col));
                diag2.remove(&((row as isize) - (col as isize)));
                board[row] = ".".repeat(n);
            }
        }

        backtrack(0, n, &mut board, &mut cols, &mut diag1, &mut diag2, &mut result);
        result
    }
}
