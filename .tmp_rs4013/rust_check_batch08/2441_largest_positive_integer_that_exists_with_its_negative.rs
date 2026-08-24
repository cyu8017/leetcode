struct Solution;
// LeetCode 2441 - Largest Positive Integer That Exists With Its Negative
// https://leetcode.com/problems/largest-positive-integer-that-exists-with-its-negative/

use std::collections::HashSet;

impl Solution {
    pub fn find_max_k(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        let mut ans = -1;
        for x in nums {
            seen.insert(x);
            if x > 0 && seen.contains(&(-x)) && x > ans {
                ans = x;
            }
            if x < 0 && seen.contains(&(-x)) && -x > ans {
                ans = -x;
            }
        }
        ans
    }
}

fn main() {}
