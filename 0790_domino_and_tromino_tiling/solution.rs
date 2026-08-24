// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

impl Solution {
    pub fn num_tilings(n: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        if n == 1 {
            return 1;
        }
        if n == 2 {
            return 2;
        }
        let n = n as usize;
        let mut dp = vec![0i64; n + 1];
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 5;
        for i in 4..=n {
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD;
        }
        dp[n] as i32
    }
}
