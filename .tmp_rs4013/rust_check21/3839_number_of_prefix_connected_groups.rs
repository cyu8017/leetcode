struct Solution;
// LeetCode 3839 - Number of Prefix Connected Groups
// https://leetcode.com/problems/number-of-prefix-connected-groups/

use std::collections::HashMap;

impl Solution {
    pub fn prefix_connected(words: Vec<String>, k: i32) -> i32 {
        let k = k as usize;
        let mut cnt = HashMap::new();
        for w in words {
            if w.len() >= k {
                *cnt.entry(w[..k].to_string()).or_insert(0) += 1;
            }
        }
        cnt.values().filter(|&&v| v > 1).count() as i32
    }
}
