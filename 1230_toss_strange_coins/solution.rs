// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

impl Solution {
    pub fn probability_of_heads(prob: Vec<f64>, target: i32) -> f64 {
        let target = target as usize;
        let mut dp = vec![0.0; target + 1];
        dp[0] = 1.0;
        for p in prob {
            for heads in (0..=target).rev() {
                let mut v = dp[heads] * (1.0 - p);
                if heads > 0 {
                    v += dp[heads - 1] * p;
                }
                dp[heads] = v;
            }
        }
        dp[target]
    }
}
