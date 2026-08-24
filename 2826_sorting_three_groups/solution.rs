// LeetCode 2826 - Sorting Three Groups
// https://leetcode.com/problems/sorting-three-groups/

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        const INF: i32 = 1 << 30;
        let mut dp = vec![[INF; 4]; n + 1];
        dp[0][1] = 0;
        dp[0][2] = 0;
        dp[0][3] = 0;
        for i in 1..=n {
            let v = nums[i - 1];
            for g in 1..=3 {
                let cost = if v != g { 1 } else { 0 };
                for prev in 1..=g {
                    dp[i][g as usize] = dp[i][g as usize].min(dp[i - 1][prev as usize] + cost);
                }
            }
        }
        dp[n][1].min(dp[n][2]).min(dp[n][3])
    }
}
