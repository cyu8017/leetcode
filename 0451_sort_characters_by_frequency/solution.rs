// LeetCode 0451 - Sort Characters By Frequency
// https://leetcode.com/problems/sort-characters-by-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn frequency_sort(s: String) -> String {
        let mut counts: HashMap<char, i32> = HashMap::new();
        for ch in s.chars() {
            *counts.entry(ch).or_insert(0) += 1;
        }

        let mut ordered: Vec<(char, i32)> = counts.into_iter().collect();
        ordered.sort_by(|left, right| {
            right
                .1
                .cmp(&left.1)
                .then_with(|| left.0.cmp(&right.0))
        });

        let mut result = String::new();
        for (ch, count) in ordered {
            for _ in 0..count {
                result.push(ch);
            }
        }
        result
    }
}
