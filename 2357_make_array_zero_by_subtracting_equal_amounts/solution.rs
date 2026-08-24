// LeetCode 2357 - Make Array Zero by Subtracting Equal Amounts
// https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_operations(nums: Vec<i32>) -> i32 {
        nums.into_iter().filter(|&x| x > 0).collect::<HashSet<_>>().len() as i32
    }
}
