struct Solution;
// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

use std::collections::HashSet;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut need: HashSet<i32> = (1..=k).collect();
        for i in (0..nums.len()).rev() {
            need.remove(&nums[i]);
            if need.is_empty() {
                return (nums.len() - i) as i32;
            }
        }
        nums.len() as i32
    }
}

fn main() {}
