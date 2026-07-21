// LeetCode 1805 - Number of Different Integers in a String
// https://leetcode.com/problems/number-of-different-integers-in-a-string/

use std::collections::HashSet;

impl Solution {
    pub fn num_different_integers(word: String) -> i32 {
        let mut seen = HashSet::new();
        let bytes = word.as_bytes();
        let mut i = 0;
        while i < bytes.len() {
            if bytes[i].is_ascii_digit() {
                let start = i;
                while i < bytes.len() && bytes[i].is_ascii_digit() {
                    i += 1;
                }
                let digits = &word[start..i];
                let normalized = digits.trim_start_matches('0');
                seen.insert(if normalized.is_empty() {
                    "0".to_string()
                } else {
                    normalized.to_string()
                });
            } else {
                i += 1;
            }
        }
        seen.len() as i32
    }
}
