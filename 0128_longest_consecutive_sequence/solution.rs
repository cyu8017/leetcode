// LeetCode 0128 - Longest Consecutive Sequence
// https://leetcode.com/problems/longest-consecutive-sequence/

use std::collections::HashSet;
impl Solution { pub fn longest_consecutive(nums: Vec<i32>) -> i32 { let values:HashSet<i32>=nums.into_iter().collect();let mut best=0;for &value in &values{if !values.contains(&(value-1)){let mut length=1;while values.contains(&(value+length)){length+=1;}best=best.max(length);}}best } }