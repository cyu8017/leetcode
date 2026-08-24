struct Solution;
fn main() {}

// LeetCode 2770 - Maximum Number of Jumps to Reach the Last Index
// https://leetcode.com/problems/maximum-number-of-jumps-to-reach-the-last-index/

impl Solution {
    pub fn maximum_jumps(nums: Vec<i32>, target: i32) -> i32 {
        let n = nums.len();
        let mut dp = vec![-1; n];
        dp[0] = 0;
        for i in 0..n {
            if dp[i] < 0 {
                continue;
            }
            for j in i + 1..n {
                if (nums[j] - nums[i]).abs() <= target {
                    dp[j] = dp[j].max(dp[i] + 1);
                }
            }
        }
        dp[n - 1]
    }
}
