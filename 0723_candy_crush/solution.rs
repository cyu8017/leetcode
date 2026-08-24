// LeetCode 0723 - Candy Crush
// https://leetcode.com/problems/candy-crush/

impl Solution {
    pub fn candy_crush(mut board: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let m = board.len();
        let n = board[0].len();
        let mut stable = false;
        while !stable {
            stable = true;
            for i in 0..m {
                for j in 0..n.saturating_sub(2) {
                    let value = board[i][j].abs();
                    if value != 0
                        && value == board[i][j + 1].abs()
                        && value == board[i][j + 2].abs()
                    {
                        board[i][j] = -value;
                        board[i][j + 1] = -value;
                        board[i][j + 2] = -value;
                        stable = false;
                    }
                }
            }
            for j in 0..n {
                for i in 0..m.saturating_sub(2) {
                    let value = board[i][j].abs();
                    if value != 0
                        && value == board[i + 1][j].abs()
                        && value == board[i + 2][j].abs()
                    {
                        board[i][j] = -value;
                        board[i + 1][j] = -value;
                        board[i + 2][j] = -value;
                        stable = false;
                    }
                }
            }
            for j in 0..n {
                let mut write = m as i32 - 1;
                for i in (0..m).rev() {
                    if board[i][j] > 0 {
                        board[write as usize][j] = board[i][j];
                        write -= 1;
                    }
                }
                for i in (0..=write).rev() {
                    board[i as usize][j] = 0;
                }
            }
        }
        board
    }
}
