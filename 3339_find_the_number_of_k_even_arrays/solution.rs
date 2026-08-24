// LeetCode 3339 - Find the Number of K-Even Arrays
// https://leetcode.com/problems/find-the-number-of-k-even-arrays/

impl Solution {
    pub fn count_of_arrays(n: i32, m: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let even = m / 2;
        let odd = m - even;
        let n = n as usize;
        let k = k as usize;
        let mut dp = vec![vec![[0i32; 2]; k + 1]; n + 1];
        dp[1][0][0] = odd;
        dp[1][0][1] = even;
        for i in 1..n {
            for j in 0..=k {
                dp[i + 1][j][0] = ((dp[i + 1][j][0] as i64
                    + ((dp[i][j][0] as i64 + dp[i][j][1] as i64) % MOD) * odd as i64 % MOD)
                    % MOD) as i32;
                dp[i + 1][j][1] = ((dp[i + 1][j][1] as i64 + dp[i][j][0] as i64 * even as i64 % MOD) % MOD) as i32;
                if j < k {
                    dp[i + 1][j + 1][1] =
                        ((dp[i + 1][j + 1][1] as i64 + dp[i][j][1] as i64 * even as i64 % MOD) % MOD) as i32;
                }
            }
        }
        ((dp[n][k][0] as i64 + dp[n][k][1] as i64) % MOD) as i32
    }
}
