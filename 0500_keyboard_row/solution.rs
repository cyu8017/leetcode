// LeetCode 0500 - Keyboard Row
// https://leetcode.com/problems/keyboard-row/

use std::collections::HashSet;

impl Solution {
    pub fn find_words(words: Vec<String>) -> Vec<String> {
        let rows = [
            "qwertyuiop".chars().collect::<HashSet<char>>(),
            "asdfghjkl".chars().collect::<HashSet<char>>(),
            "zxcvbnm".chars().collect::<HashSet<char>>(),
        ];
        words
            .into_iter()
            .filter(|word| {
                let letters: HashSet<char> = word
                    .chars()
                    .filter(|ch| ch.is_ascii_alphabetic())
                    .map(|ch| ch.to_ascii_lowercase())
                    .collect();
                rows.iter().any(|row| letters.iter().all(|ch| row.contains(ch)))
            })
            .collect()
    }
}
