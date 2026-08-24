struct Solution;

// LeetCode 2568 - Minimum Impossible OR
// https://leetcode.com/problems/minimum-impossible-or/

use std::collections::HashSet;

impl Solution {
    pub fn min_impossible_or(nums: Vec<i32>) -> i32 {
        let set: HashSet<i32> = nums.into_iter().collect();
        let mut i = 1;
        loop {
            if !set.contains(&i) {
                return i;
            }
            i <<= 1;
        }
    }
}

fn main() {}
