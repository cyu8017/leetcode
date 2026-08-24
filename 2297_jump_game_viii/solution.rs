// LeetCode 2297 - Jump Game VIII
// https://leetcode.com/problems/jump-game-viii/

impl Solution {
    pub fn min_cost(nums: Vec<i32>, costs: Vec<i32>) -> i64 {
        let n = nums.len();
        let mut dp = vec![i64::MAX / 4; n];
        dp[0] = 0;
        let mut stack1: Vec<usize> = Vec::new();
        let mut stack2: Vec<usize> = Vec::new();
        for i in 0..n {
            while !stack1.is_empty() && nums[*stack1.last().unwrap()] <= nums[i] {
                let j = stack1.pop().unwrap();
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            while !stack2.is_empty() && nums[*stack2.last().unwrap()] > nums[i] {
                let j = stack2.pop().unwrap();
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            if let Some(&j) = stack1.last() {
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            if let Some(&j) = stack2.last() {
                dp[i] = dp[i].min(dp[j] + costs[i] as i64);
            }
            stack1.push(i);
            stack2.push(i);
        }
        dp[n - 1]
    }
}
