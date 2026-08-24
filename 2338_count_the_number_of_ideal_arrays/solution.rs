// LeetCode 2338 - Count the Number of Ideal Arrays
// https://leetcode.com/problems/count-the-number-of-ideal-arrays/

impl Solution {
    pub fn ideal_arrays(n: i32, max_value: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        const MAX_LEN: usize = 14;
        let n = n as usize;
        let max_value = max_value as usize;
        let mut comb = vec![vec![0i64; MAX_LEN + 1]; n + 1];
        for i in 0..=n {
            comb[i][0] = 1;
            let mut j = 1;
            while j <= MAX_LEN && j <= i {
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD;
                j += 1;
            }
        }
        let mut dp = vec![vec![0i64; MAX_LEN + 1]; max_value + 1];
        for i in 1..=max_value {
            dp[i][1] = 1;
        }
        for len in 2..=MAX_LEN {
            for v in 1..=max_value {
                let mut m = 2 * v;
                while m <= max_value {
                    dp[m][len] = (dp[m][len] + dp[v][len - 1]) % MOD;
                    m += v;
                }
            }
        }
        let mut ans = 0i64;
        for v in 1..=max_value {
            for len in 1..=MAX_LEN.min(n) {
                ans = (ans + dp[v][len] * comb[n - 1][len - 1] % MOD) % MOD;
            }
        }
        ans as i32
    }
}
