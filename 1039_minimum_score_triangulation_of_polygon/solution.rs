// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

impl Solution {
    pub fn min_score_triangulation(values: Vec<i32>) -> i32 {
        let n = values.len();
        let mut dp = vec![vec![0; n]; n];
        for length in 2..n {
            for i in 0..n - length {
                let j = i + length;
                let mut best = i32::MAX;
                for k in i + 1..j {
                    best = best.min(dp[i][k] + values[i] * values[k] * values[j] + dp[k][j]);
                }
                dp[i][j] = best;
            }
        }
        dp[0][n - 1]
    }
}
