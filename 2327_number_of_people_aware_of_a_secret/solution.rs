// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

impl Solution {
    pub fn people_aware_of_secret(n: i32, delay: i32, forget: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let n = n as usize;
        let delay = delay as usize;
        let forget = forget as usize;
        let mut dp = vec![0i32; n + 1];
        dp[1] = 1;
        let mut share = 0i32;
        for day in 2..=n {
            if day >= delay + 1 {
                share = (share + dp[day - delay]) % MOD;
            }
            if day >= forget + 1 {
                share = (share - dp[day - forget] + MOD) % MOD;
            }
            dp[day] = share;
        }
        let mut ans = 0;
        let start = if n + 1 > forget { n - forget + 1 } else { 1 };
        for day in start..=n {
            ans = (ans + dp[day]) % MOD;
        }
        ans
    }
}
