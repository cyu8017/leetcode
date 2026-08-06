// LeetCode 1155 - Number of Dice Rolls With Target Sum
// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

impl Solution {
    pub fn num_rolls_to_target(n: i32, k: i32, target: i32) -> i32 {
        const MOD: i32 = 1_000_000_007;
        let target = target as usize;
        let mut dp = vec![0; target + 1];
        dp[0] = 1;
        for _ in 0..n {
            let mut new_dp = vec![0; target + 1];
            for s in 0..=target {
                if dp[s] == 0 {
                    continue;
                }
                for face in 1..=k as usize {
                    if s + face <= target {
                        new_dp[s + face] = (new_dp[s + face] + dp[s]) % MOD;
                    }
                }
            }
            dp = new_dp;
        }
        dp[target]
    }
}
