// LeetCode 2248 - Intersection of Multiple Arrays
// https://leetcode.com/problems/intersection-of-multiple-arrays/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn intersection(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let m = nums.len() as i32;
        let mut freq = HashMap::new();
        for arr in &nums {
            let mut seen = HashSet::new();
            for &x in arr {
                if seen.insert(x) {
                    *freq.entry(x).or_insert(0) += 1;
                }
            }
        }
        let mut ans: Vec<i32> = freq.into_iter().filter(|(_, c)| *c == m).map(|(x, _)| x).collect();
        ans.sort_unstable();
        ans
    }
}
