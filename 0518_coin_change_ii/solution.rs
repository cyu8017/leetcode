// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

impl Solution {
    pub fn change(amount: i32, coins: Vec<i32>) -> i32 {
        let amount = amount as usize;
        let mut dp = vec![0i64; amount + 1];
        dp[0] = 1;
        for coin in coins {
            let coin = coin as usize;
            for value in coin..=amount {
                dp[value] += dp[value - coin];
            }
        }
        dp[amount] as i32
    }
}
