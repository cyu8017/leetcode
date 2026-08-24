// LeetCode 0819 - Most Common Word
// https://leetcode.com/problems/most-common-word/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn most_common_word(paragraph: String, banned: Vec<String>) -> String {
        let banned_set: HashSet<String> = banned.into_iter().collect();
        let mut counts = HashMap::new();
        let mut word = String::new();
        let mut best = String::new();
        let mut best_count = 0;
        let mut flush = |word: &mut String| {
            if !word.is_empty() {
                if !banned_set.contains(word) {
                    let c = counts.entry(word.clone()).or_insert(0);
                    *c += 1;
                    if *c > best_count {
                        best_count = *c;
                        best = word.clone();
                    }
                }
                word.clear();
            }
        };
        for ch in paragraph.chars() {
            if ch.is_ascii_alphabetic() {
                word.push(ch.to_ascii_lowercase());
            } else {
                flush(&mut word);
            }
        }
        flush(&mut word);
        best
    }
}
