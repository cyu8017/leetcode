// LeetCode 1858 - Longest Word With All Prefixes
// https://leetcode.com/problems/longest-word-with-all-prefixes/

use std::collections::HashSet;

impl Solution {
    pub fn longest_word(words: Vec<String>) -> String {
        let word_set: HashSet<&str> = words.iter().map(|w| w.as_str()).collect();
        let mut best = String::new();
        for word in &words {
            let mut valid = true;
            for end in 1..=word.len() {
                if !word_set.contains(&word[..end]) {
                    valid = false;
                    break;
                }
            }
            if valid
                && (word.len() > best.len()
                    || (word.len() == best.len() && word.as_str() < best.as_str()))
            {
                best = word.clone();
            }
        }
        best
    }
}
