// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

impl Solution {
    pub fn minimum_coins(prices: Vec<i32>) -> i32 {
        let n = prices.len();
        let mut dp = vec![1 << 30; n + 1];
        dp[0] = 0;
        for i in 1..=n {
            let mut j = i;
            while j <= n && j <= 2 * i {
                dp[j] = dp[j].min(dp[i - 1] + prices[i - 1]);
                j += 1;
            }
        }
        dp[n]
    }
}
