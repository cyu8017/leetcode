// LeetCode 2229 - Check if an Array Is Consecutive
// https://leetcode.com/problems/check-if-an-array-is-consecutive/

use std::collections::HashSet;

impl Solution {
    pub fn is_consecutive(nums: Vec<i32>) -> bool {
        let mut mn = nums[0];
        let mut mx = nums[0];
        let mut seen = HashSet::new();
        for x in &nums {
            if !seen.insert(*x) {
                return false;
            }
            mn = mn.min(*x);
            mx = mx.max(*x);
        }
        mx - mn + 1 == nums.len() as i32
    }
}
