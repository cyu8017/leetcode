// LeetCode 1940 - Longest Common Subsequence Between Sorted Arrays
// https://leetcode.com/problems/longest-common-subsequence-between-sorted-arrays/

use std::collections::HashMap;

impl Solution {
    pub fn longest_common_subsequence(arrays: Vec<Vec<i32>>) -> Vec<i32> {
        let mut cnt: HashMap<i32, i32> = HashMap::new();
        for arr in &arrays {
            for &x in arr {
                *cnt.entry(x).or_insert(0) += 1;
            }
        }
        let m = arrays.len() as i32;
        arrays[0]
            .iter()
            .copied()
            .filter(|&x| cnt.get(&x).copied().unwrap_or(0) == m)
            .collect()
    }
}
