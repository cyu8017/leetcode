// LeetCode 0290 - Word Pattern
// https://leetcode.com/problems/word-pattern/

use std::collections::HashMap;

impl Solution {
    pub fn word_pattern(pattern: String, s: String) -> bool {
        let words: Vec<&str> = s.split_whitespace().collect();
        if pattern.len() != words.len() {
            return false;
        }

        let mut char_to_word: HashMap<char, &str> = HashMap::new();
        let mut word_to_char: HashMap<&str, char> = HashMap::new();
        for (ch, word) in pattern.chars().zip(words.iter()) {
            if let Some(mapped) = char_to_word.get(&ch) {
                if *mapped != *word {
                    return false;
                }
            } else if word_to_char.contains_key(word) {
                return false;
            } else {
                char_to_word.insert(ch, word);
                word_to_char.insert(word, ch);
            }
        }
        true
    }
}
