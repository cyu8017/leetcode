// LeetCode 0030 - Substring with Concatenation of All Words
// https://leetcode.com/problems/substring-with-concatenation-of-all-words/

use std::collections::HashMap;

impl Solution {
    pub fn find_substring(s: String, words: Vec<String>) -> Vec<i32> {
        if words.is_empty() || s.is_empty() {
            return Vec::new();
        }

        let word_len = words[0].len();
        let word_count = words.len();
        let mut need = HashMap::new();
        for word in &words {
            *need.entry(word.as_str()).or_insert(0) += 1;
        }

        let mut result = Vec::new();
        let bytes = s.as_bytes();

        for start in 0..word_len {
            let mut left = start;
            let mut counts: HashMap<&str, i32> = HashMap::new();
            let mut used = 0;

            let mut right = start;
            while right + word_len <= bytes.len() {
                let word = std::str::from_utf8(&bytes[right..right + word_len]).unwrap();
                if !need.contains_key(word) {
                    counts.clear();
                    used = 0;
                    left = right + word_len;
                    right = left;
                    continue;
                }

                *counts.entry(word).or_insert(0) += 1;
                used += 1;
                while counts[word] > *need.get(word).unwrap_or(&0) {
                    let left_word =
                        std::str::from_utf8(&bytes[left..left + word_len]).unwrap();
                    *counts.get_mut(left_word).unwrap() -= 1;
                    used -= 1;
                    left += word_len;
                }

                if used == word_count as i32 {
                    result.push(left as i32);
                }
                right += word_len;
            }
        }

        result.sort_unstable();
        result
    }
}
