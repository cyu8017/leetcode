// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

impl Solution {
    pub fn rearrange_sticks(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let k = k as usize;
        if k == 0 || k > n {
            return 0;
        }
        let mut dp = vec![vec![0i64; n + 1]; n + 1];
        dp[1][1] = 1;
        for sticks in 2..=n {
            dp[sticks][1] = ((sticks as i64 - 1) * dp[sticks - 1][1]) % MOD;
            for visible in 2..=sticks {
                dp[sticks][visible] = (dp[sticks - 1][visible - 1]
                    + (sticks as i64 - 1) * dp[sticks - 1][visible])
                    % MOD;
            }
        }
        dp[n][k] as i32
    }
}
