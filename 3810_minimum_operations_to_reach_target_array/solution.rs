// LeetCode 3810 - Minimum Operations To Reach Target Array
// https://leetcode.com/problems/minimum-operations-to-reach-target-array/

use std::collections::HashSet;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, target: Vec<i32>) -> i32 {
        let mut s = HashSet::new();
        for i in 0..nums.len() {
            if nums[i] != target[i] {
                s.insert(nums[i]);
            }
        }
        s.len() as i32
    }
}
