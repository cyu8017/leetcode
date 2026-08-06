// LeetCode 1218 - Longest Arithmetic Subsequence of Given Difference
// https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/

use std::collections::HashMap;

impl Solution {
    pub fn longest_subsequence(arr: Vec<i32>, difference: i32) -> i32 {
        let mut dp = HashMap::new();
        let mut best = 0;
        for x in arr {
            let v = dp.get(&(x - difference)).copied().unwrap_or(0) + 1;
            dp.insert(x, v);
            best = best.max(v);
        }
        best
    }
}
