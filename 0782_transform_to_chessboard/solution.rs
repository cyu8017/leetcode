// LeetCode 0782 - Transform to Chessboard
// https://leetcode.com/problems/transform-to-chessboard/

impl Solution {
    pub fn moves_to_chessboard(board: Vec<Vec<i32>>) -> i32 {
        let n = board.len();
        for i in 0..n {
            for j in 0..n {
                if (board[0][0] ^ board[i][0] ^ board[0][j] ^ board[i][j]) != 0 {
                    return -1;
                }
            }
        }
        let mut row_sum = 0;
        let mut col_sum = 0;
        for i in 0..n {
            row_sum += board[0][i];
            col_sum += board[i][0];
        }
        let n_i = n as i32;
        if !(n_i / 2 <= row_sum && row_sum <= (n_i + 1) / 2) {
            return -1;
        }
        if !(n_i / 2 <= col_sum && col_sum <= (n_i + 1) / 2) {
            return -1;
        }
        let mut row_swap = 0;
        let mut col_swap = 0;
        for i in 0..n {
            if board[0][i] != (i % 2) as i32 {
                row_swap += 1;
            }
            if board[i][0] != (i % 2) as i32 {
                col_swap += 1;
            }
        }
        if n % 2 == 1 {
            if row_swap % 2 == 1 {
                row_swap = n_i - row_swap;
            }
            if col_swap % 2 == 1 {
                col_swap = n_i - col_swap;
            }
        } else {
            row_swap = row_swap.min(n_i - row_swap);
            col_swap = col_swap.min(n_i - col_swap);
        }
        (row_swap + col_swap) / 2
    }
}
