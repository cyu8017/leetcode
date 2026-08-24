struct Solution;
fn main() {}

// LeetCode 2780 - Minimum Index of a Valid Split
// https://leetcode.com/problems/minimum-index-of-a-valid-split/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_index(nums: Vec<i32>) -> i32 {
        let mut freq = HashMap::new();
        let mut dom = 0;
        let mut best = 0;
        for &v in &nums {
            let e = freq.entry(v).or_insert(0);
            *e += 1;
            if *e > best {
                best = *e;
                dom = v;
            }
        }
        let mut left = 0;
        let n = nums.len() as i32;
        for i in 0..n - 1 {
            if nums[i as usize] == dom {
                left += 1;
            }
            let right = best - left;
            if left * 2 > i + 1 && right * 2 > n - i - 1 {
                return i;
            }
        }
        -1
    }
}
