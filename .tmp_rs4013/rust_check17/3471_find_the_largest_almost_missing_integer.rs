struct Solution;
// LeetCode 3471 - Find the Largest Almost Missing Integer
// https://leetcode.com/problems/find-the-largest-almost-missing-integer/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn largest_integer(nums: Vec<i32>, k: i32) -> i32 {
        let n = nums.len();
        let k = k as usize;
        let mut cnt = HashMap::new();
        for i in 0..=n.saturating_sub(k) {
            let mut seen = HashSet::new();
            for j in i..i + k {
                seen.insert(nums[j]);
            }
            for x in seen {
                *cnt.entry(x).or_insert(0) += 1;
            }
        }
        let mut ans = -1;
        for (x, c) in cnt {
            if c == 1 && x > ans {
                ans = x;
            }
        }
        ans
    }
}

fn main() {}
