struct Solution;
// LeetCode 3375 - Minimum Operations to Make Array Values Equal to K
// https://leetcode.com/problems/minimum-operations-to-make-array-values-equal-to-k/

use std::collections::HashSet;

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut seen = HashSet::new();
        for x in nums {
            if x < k {
                return -1;
            }
            if x > k {
                seen.insert(x);
            }
        }
        seen.len() as i32
    }
}

fn main() {}
