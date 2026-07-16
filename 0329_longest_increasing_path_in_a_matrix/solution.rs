// LeetCode 0329 - Longest Increasing Path in a Matrix
// https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

impl Solution {
    fn dfs(
        matrix: &[Vec<i32>],
        memo: &mut [Vec<i32>],
        row: usize,
        col: usize,
    ) -> i32 {
        if memo[row][col] != 0 {
            return memo[row][col];
        }
        let mut best = 1;
        let directions = [(1, 0), (-1, 0), (0, 1), (0, -1)];
        for (dr, dc) in directions {
            let next_row = row as i32 + dr;
            let next_col = col as i32 + dc;
            if next_row >= 0
                && next_col >= 0
                && (next_row as usize) < matrix.len()
                && (next_col as usize) < matrix[0].len()
                && matrix[next_row as usize][next_col as usize] > matrix[row][col]
            {
                best = best.max(
                    1 + Self::dfs(
                        matrix,
                        memo,
                        next_row as usize,
                        next_col as usize,
                    ),
                );
            }
        }
        memo[row][col] = best;
        best
    }

    pub fn longest_increasing_path(matrix: Vec<Vec<i32>>) -> i32 {
        if matrix.is_empty() || matrix[0].is_empty() {
            return 0;
        }
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut memo = vec![vec![0; cols]; rows];
        let mut best = 0;
        for row in 0..rows {
            for col in 0..cols {
                best = best.max(Self::dfs(&matrix, &mut memo, row, col));
            }
        }
        best
    }
}
