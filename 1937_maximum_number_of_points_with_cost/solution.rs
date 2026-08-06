// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

impl Solution {
    pub fn max_points(points: Vec<Vec<i32>>) -> i64 {
        let m = points.len();
        let n = points[0].len();
        let mut dp: Vec<i64> = points[0].iter().map(|&x| x as i64).collect();
        for r in 1..m {
            let mut left = vec![0i64; n];
            let mut right = vec![0i64; n];
            left[0] = dp[0];
            for c in 1..n {
                left[c] = (left[c - 1] - 1).max(dp[c]);
            }
            right[n - 1] = dp[n - 1];
            for c in (0..n - 1).rev() {
                right[c] = (right[c + 1] - 1).max(dp[c]);
            }
            dp = (0..n)
                .map(|c| points[r][c] as i64 + left[c].max(right[c]))
                .collect();
        }
        *dp.iter().max().unwrap()
    }
}
