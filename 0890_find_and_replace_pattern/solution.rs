// LeetCode 0890 - Find and Replace Pattern
// https://leetcode.com/problems/find-and-replace-pattern/

use std::collections::HashMap;

impl Solution {
    pub fn find_and_replace_pattern(words: Vec<String>, pattern: String) -> Vec<String> {
        fn normalize(s: &str) -> Vec<i32> {
            let mut mapping = HashMap::new();
            let mut out = Vec::new();
            for ch in s.chars() {
                let next = mapping.len() as i32;
                let id = *mapping.entry(ch).or_insert(next);
                out.push(id);
            }
            out
        }
        let target = normalize(&pattern);
        words.into_iter().filter(|w| normalize(w) == target).collect()
    }
}
