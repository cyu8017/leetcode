// LeetCode 0221 - Maximal Square
// https://leetcode.com/problems/maximal-square/

impl Solution {
    pub fn maximal_square(matrix: Vec<Vec<char>>) -> i32 {
        if matrix.is_empty() {
            return 0;
        }
        let rows = matrix.len();
        let cols = matrix[0].len();
        let mut dp = vec![0; cols + 1];
        let mut max_side = 0;
        let mut prev = 0;
        for row in 1..=rows {
            for col in 1..=cols {
                let temp = dp[col];
                if matrix[row - 1][col - 1] == '1' {
                    dp[col] = dp[col].min(dp[col - 1]).min(prev) + 1;
                    max_side = max_side.max(dp[col]);
                } else {
                    dp[col] = 0;
                }
                prev = temp;
            }
        }
        max_side * max_side
    }
}
