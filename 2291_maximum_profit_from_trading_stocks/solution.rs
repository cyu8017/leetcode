// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

impl Solution {
    pub fn maximum_profit(present: Vec<i32>, future: Vec<i32>, budget: i32) -> i32 {
        let n = present.len();
        let budget = budget as usize;
        let mut dp = vec![0; budget + 1];
        for i in 0..n {
            let profit = future[i] - present[i];
            if profit <= 0 {
                continue;
            }
            let cost = present[i] as usize;
            for b in (cost..=budget).rev() {
                dp[b] = dp[b].max(dp[b - cost] + profit);
            }
        }
        dp[budget]
    }
}
