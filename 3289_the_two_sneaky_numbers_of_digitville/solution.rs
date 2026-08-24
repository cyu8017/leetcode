// LeetCode 3289 - The Two Sneaky Numbers of Digitville
// https://leetcode.com/problems/the-two-sneaky-numbers-of-digitville/

use std::collections::HashSet;

impl Solution {
    pub fn get_sneaky_numbers(nums: Vec<i32>) -> Vec<i32> {
        let mut seen = HashSet::new();
        let mut ans = Vec::new();
        for x in nums {
            if !seen.insert(x) {
                ans.push(x);
            }
        }
        ans
    }
}
