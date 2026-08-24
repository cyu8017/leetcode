// LeetCode 3718 - Smallest Missing Multiple of K
// https://leetcode.com/problems/smallest-missing-multiple-of-k/

use std::collections::HashSet;

impl Solution {
    pub fn missing_multiple(nums: Vec<i32>, k: i32) -> i32 {
        let s: HashSet<i32> = nums.into_iter().collect();
        let mut i = 1;
        loop {
            let x = k * i;
            if !s.contains(&x) {
                return x;
            }
            i += 1;
        }
    }
}
