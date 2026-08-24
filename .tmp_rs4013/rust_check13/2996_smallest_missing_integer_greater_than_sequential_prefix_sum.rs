#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2996 - Smallest Missing Integer Greater Than Sequential Prefix Sum
// https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/

use std::collections::HashSet;

impl Solution {
    pub fn missing_integer(nums: Vec<i32>) -> i32 {
        let mut sum = nums[0];
        let mut i = 1;
        while i < nums.len() && nums[i] == nums[i - 1] + 1 {
            sum += nums[i];
            i += 1;
        }
        let seen: HashSet<i32> = nums.into_iter().collect();
        while seen.contains(&sum) {
            sum += 1;
        }
        sum
    }
}
