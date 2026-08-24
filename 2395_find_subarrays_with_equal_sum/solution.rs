// LeetCode 2395 - Find Subarrays With Equal Sum
// https://leetcode.com/problems/find-subarrays-with-equal-sum/

use std::collections::HashSet;

impl Solution {
    pub fn find_subarrays(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();
        for i in 0..nums.len().saturating_sub(1) {
            let s = nums[i] + nums[i + 1];
            if !seen.insert(s) {
                return true;
            }
        }
        false
    }
}
