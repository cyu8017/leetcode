// LeetCode 0720 - Longest Word in Dictionary
// https://leetcode.com/problems/longest-word-in-dictionary/

use std::collections::HashSet;

impl Solution {
    pub fn longest_word(mut words: Vec<String>) -> String {
        words.sort();
        let mut built = HashSet::new();
        built.insert(String::new());
        let mut best = String::new();
        for word in words {
            if built.contains(&word[..word.len() - 1]) {
                if word.len() > best.len() {
                    best = word.clone();
                }
                built.insert(word);
            }
        }
        best
    }
}
