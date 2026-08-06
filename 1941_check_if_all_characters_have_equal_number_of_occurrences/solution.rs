// LeetCode 1941 - Check if All Characters Have Equal Number of Occurrences
// https://leetcode.com/problems/check-if-all-characters-have-equal-number-of-occurrences/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn are_occurrences_equal(s: String) -> bool {
        let mut freq: HashMap<char, i32> = HashMap::new();
        for c in s.chars() {
            *freq.entry(c).or_insert(0) += 1;
        }
        let vals: HashSet<i32> = freq.values().copied().collect();
        vals.len() == 1
    }
}
