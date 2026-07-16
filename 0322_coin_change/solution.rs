// LeetCode 0322 - Coin Change
// https://leetcode.com/problems/coin-change/

impl Solution {
    pub fn coin_change(coins: Vec<i32>, amount: i32) -> i32 {
        let amount = amount as usize;
        let max_value = amount + 1;
        let mut dp = vec![max_value; amount + 1];
        dp[0] = 0;
        for coin in coins {
            let coin = coin as usize;
            for value in coin..=amount {
                dp[value] = dp[value].min(dp[value - coin] + 1);
            }
        }
        if dp[amount] == max_value {
            -1
        } else {
            dp[amount] as i32
        }
    }
}
