// LeetCode 1027 - Longest Arithmetic Subsequence
// https://leetcode.com/problems/longest-arithmetic-subsequence/

use std::collections::HashMap;

impl Solution {
    pub fn longest_arith_seq_length(nums: Vec<i32>) -> i32 {
        let mut dp: Vec<HashMap<i32, i32>> = vec![HashMap::new(); nums.len()];
        let mut ans = 1;
        for j in 1..nums.len() {
            for i in 0..j {
                let d = nums[j] - nums[i];
                let prev = dp[i].get(&d).copied().unwrap_or(1);
                let cur = prev + 1;
                dp[j].insert(d, cur);
                ans = ans.max(cur);
            }
        }
        ans
    }
}
