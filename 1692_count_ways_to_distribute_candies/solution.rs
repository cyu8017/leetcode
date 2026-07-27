// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

impl Solution {
    pub fn ways_to_distribute(n: i32, k: i32) -> i32 {
        const MOD: i64 = 1_000_000_007;
        let n = n as usize;
        let k = k as usize;
        let mut dp = vec![0i64; k + 1];
        dp[0] = 1;
        for i in 1..=n {
            for j in (1..=i.min(k)).rev() {
                dp[j] = (dp[j - 1] + j as i64 * dp[j]) % MOD;
            }
            dp[0] = 0;
        }
        dp[k] as i32
    }
}
