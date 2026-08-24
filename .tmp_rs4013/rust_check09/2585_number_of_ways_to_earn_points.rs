struct Solution;

// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

impl Solution {
    pub fn ways_to_reach_target(target: i32, types: Vec<Vec<i32>>) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let target = target as usize;
        let mut dp = vec![0; target + 1];
        dp[0] = 1;
        for t in types {
            let count = t[0];
            let marks = t[1] as usize;
            for s in (0..=target).rev() {
                let mut k = 1;
                while k <= count && s >= k as usize * marks {
                    dp[s] = (dp[s] + dp[s - k as usize * marks]) % MOD;
                    k += 1;
                }
            }
        }
        dp[target]
    }
}

fn main() {}
