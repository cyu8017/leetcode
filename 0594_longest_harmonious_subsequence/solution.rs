// LeetCode 0594 - Longest Harmonious Subsequence
// https://leetcode.com/problems/longest-harmonious-subsequence/

use std::collections::HashMap;

impl Solution {
    pub fn find_lhs(nums: Vec<i32>) -> i32 {
        let mut counts = HashMap::new();
        for num in nums {
            *counts.entry(num).or_insert(0) += 1;
        }
        let mut best = 0;
        for (&value, &count) in &counts {
            if let Some(&next) = counts.get(&(value + 1)) {
                best = best.max(count + next);
            }
        }
        best
    }
}
