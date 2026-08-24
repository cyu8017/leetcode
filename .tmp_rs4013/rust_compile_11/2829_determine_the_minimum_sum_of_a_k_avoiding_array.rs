struct Solution;
fn main() {}

// LeetCode 2829 - Determine the Minimum Sum of a k-avoiding Array
// https://leetcode.com/problems/determine-the-minimum-sum-of-a-k-avoiding-array/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_sum(n: i32, k: i32) -> i32 {
        let mut used = HashSet::new();
        let mut sum = 0;
        let mut x = 1;
        while used.len() < n as usize {
            if !used.contains(&(k - x)) {
                used.insert(x);
                sum += x;
            }
            x += 1;
        }
        sum
    }
}
