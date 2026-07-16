// LeetCode 0375 - Guess Number Higher or Lower II
// https://leetcode.com/problems/guess-number-higher-or-lower-ii/

impl Solution {
    pub fn get_money_amount(n: i32) -> i32 {
        let n = n as usize;
        let mut dp = vec![vec![0; n + 2]; n + 2];

        for length in 2..=n {
            for left in 1..=n - length + 1 {
                let right = left + length - 1;
                dp[left][right] = i32::MAX;
                for guess in left..right {
                    let cost = guess as i32 + dp[left][guess - 1].max(dp[guess + 1][right]);
                    dp[left][right] = dp[left][right].min(cost);
                }
            }
        }

        dp[1][n]
    }
}
