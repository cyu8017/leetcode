// LeetCode 1207 - Unique Number of Occurrences
// https://leetcode.com/problems/unique-number-of-occurrences/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn unique_occurrences(arr: Vec<i32>) -> bool {
        let mut count = HashMap::new();
        for x in arr {
            *count.entry(x).or_insert(0) += 1;
        }
        let freqs: HashSet<_> = count.values().copied().collect();
        freqs.len() == count.len()
    }
}
