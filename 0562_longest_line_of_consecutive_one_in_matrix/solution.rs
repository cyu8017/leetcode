// LeetCode 0562 - Longest Line of Consecutive One in Matrix
// https://leetcode.com/problems/longest-line-of-consecutive-one-in-matrix/

impl Solution {
    pub fn longest_line(mat: Vec<Vec<i32>>) -> i32 {
        if mat.is_empty() || mat[0].is_empty() {
            return 0;
        }
        let rows = mat.len();
        let cols = mat[0].len();
        let mut dp = vec![vec![[0i32; 4]; cols]; rows];
        let mut best = 0;
        for r in 0..rows {
            for c in 0..cols {
                if mat[r][c] == 0 {
                    continue;
                }
                dp[r][c][0] = if c > 0 { dp[r][c - 1][0] } else { 0 } + 1;
                dp[r][c][1] = if r > 0 { dp[r - 1][c][1] } else { 0 } + 1;
                dp[r][c][2] = if r > 0 && c > 0 { dp[r - 1][c - 1][2] } else { 0 } + 1;
                dp[r][c][3] = if r > 0 && c + 1 < cols { dp[r - 1][c + 1][3] } else { 0 } + 1;
                best = best.max(*dp[r][c].iter().max().unwrap());
            }
        }
        best
    }
}
