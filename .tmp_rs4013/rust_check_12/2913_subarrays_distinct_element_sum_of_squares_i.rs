struct Solution;
// LeetCode 2913 - Subarrays Distinct Element Sum of Squares I
// https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

use std::collections::HashSet;

impl Solution {
    pub fn sum_counts(nums: Vec<i32>) -> i32 {
        let n = nums.len();
        let mut ans = 0;
        for i in 0..n {
            let mut seen = HashSet::new();
            for j in i..n {
                seen.insert(nums[j]);
                let d = seen.len() as i32;
                ans += d * d;
            }
        }
        ans
    }
}

fn main() {}
