// LeetCode 0377 - Combination Sum IV
// https://leetcode.com/problems/combination-sum-iv/

impl Solution {
    pub fn combination_sum4(nums: Vec<i32>, target: i32) -> i32 {
        let target = target as usize;
        let mut dp = vec![0u32; target + 1];
        dp[0] = 1;

        for amount in 1..=target {
            for num in &nums {
                if amount >= *num as usize {
                    dp[amount] += dp[amount - *num as usize];
                }
            }
        }

        dp[target] as i32
    }
}
