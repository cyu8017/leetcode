// LeetCode 0217 - Contains Duplicate
// https://leetcode.com/problems/contains-duplicate/

use std::collections::HashSet;

impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut seen = HashSet::new();
        for num in nums {
            if !seen.insert(num) {
                return true;
            }
        }
        false
    }
}
