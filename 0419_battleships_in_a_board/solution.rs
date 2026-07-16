// LeetCode 0419 - Battleships in a Board
// https://leetcode.com/problems/battleships-in-a-board/

impl Solution {
    pub fn count_battleships(board: Vec<Vec<char>>) -> i32 {
        let rows = board.len();
        let cols = board[0].len();
        let mut count = 0;

        for row in 0..rows {
            for col in 0..cols {
                if board[row][col] != 'X' {
                    continue;
                }
                if row > 0 && board[row - 1][col] == 'X' {
                    continue;
                }
                if col > 0 && board[row][col - 1] == 'X' {
                    continue;
                }
                count += 1;
            }
        }

        count
    }
}
