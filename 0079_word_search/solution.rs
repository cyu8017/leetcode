// LeetCode 0079 - Word Search
// https://leetcode.com/problems/word-search/

impl Solution {
    pub fn exist(board: &mut Vec<Vec<char>>, word: String) -> bool {
        let rows = board.len();
        let cols = board[0].len();
        let bytes = word.as_bytes();

        fn dfs(
            board: &mut Vec<Vec<char>>,
            bytes: &[u8],
            row: usize,
            col: usize,
            index: usize,
        ) -> bool {
            if index == bytes.len() {
                return true;
            }
            if row >= board.len() || col >= board[0].len() || board[row][col] as u8 != bytes[index] {
                return false;
            }

            let temp = board[row][col];
            board[row][col] = '#';

            let found = dfs(board, bytes, row + 1, col, index + 1)
                || (row > 0 && dfs(board, bytes, row - 1, col, index + 1))
                || dfs(board, bytes, row, col + 1, index + 1)
                || (col > 0 && dfs(board, bytes, row, col - 1, index + 1));

            board[row][col] = temp;
            found
        }

        for row in 0..rows {
            for col in 0..cols {
                if dfs(board, bytes, row, col, 0) {
                    return true;
                }
            }
        }

        false
    }
}
