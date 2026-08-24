// LeetCode 0931 - Minimum Falling Path Sum
// https://leetcode.com/problems/minimum-falling-path-sum/

impl Solution {
    pub fn min_falling_path_sum(matrix: Vec<Vec<i32>>) -> i32 {
        let mut dp = matrix[0].clone();
        for r in 1..matrix.len() {
            let mut ndp = vec![0; dp.len()];
            for c in 0..dp.len() {
                let mut best = dp[c];
                if c > 0 {
                    best = best.min(dp[c - 1]);
                }
                if c + 1 < dp.len() {
                    best = best.min(dp[c + 1]);
                }
                ndp[c] = matrix[r][c] + best;
            }
            dp = ndp;
        }
        *dp.iter().min().unwrap()
    }
}
