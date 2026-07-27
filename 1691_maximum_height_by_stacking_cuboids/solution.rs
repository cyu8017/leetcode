// LeetCode 1691 - Maximum Height by Stacking Cuboids
// https://leetcode.com/problems/maximum-height-by-stacking-cuboids/

impl Solution {
    pub fn max_height(mut cuboids: Vec<Vec<i32>>) -> i32 {
        for c in &mut cuboids {
            c.sort_unstable();
        }
        cuboids.sort_unstable();
        let n = cuboids.len();
        let mut dp = vec![0i32; n];
        let mut best = 0;
        for i in 0..n {
            dp[i] = cuboids[i][2];
            for j in 0..i {
                if (0..3).all(|d| cuboids[j][d] <= cuboids[i][d]) {
                    dp[i] = dp[i].max(dp[j] + cuboids[i][2]);
                }
            }
            best = best.max(dp[i]);
        }
        best
    }
}
