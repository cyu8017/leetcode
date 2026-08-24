// LeetCode 3396 - Minimum Number of Operations to Make Elements in Array Distinct
// https://leetcode.com/problems/minimum-number-of-operations-to-make-elements-in-array-distinct/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_operations(mut nums: Vec<i32>) -> i32 {
        let mut ops = 0;
        loop {
            let mut seen = HashSet::new();
            let mut dup = false;
            for &x in &nums {
                if !seen.insert(x) {
                    dup = true;
                    break;
                }
            }
            if !dup {
                return ops;
            }
            if nums.len() <= 3 {
                return ops + 1;
            }
            nums.drain(0..3);
            ops += 1;
        }
    }
}
