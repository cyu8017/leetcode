#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2997 - Minimum Number of Operations to Make Array XOR Equal to K
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-xor-equal-to-k/

impl Solution {
    pub fn min_operations(nums: Vec<i32>, k: i32) -> i32 {
        let mut xorr = 0;
        for v in nums {
            xorr ^= v;
        }
        (xorr ^ k).count_ones() as i32
    }
}
