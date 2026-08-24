// LeetCode 0824 - Goat Latin
// https://leetcode.com/problems/goat-latin/

use std::collections::HashSet;

impl Solution {
    pub fn to_goat_latin(sentence: String) -> String {
        let vowels: HashSet<char> = "aeiouAEIOU".chars().collect();
        let mut out = String::new();
        for (i, word) in sentence.split_whitespace().enumerate() {
            if !out.is_empty() {
                out.push(' ');
            }
            let mut goat = if vowels.contains(&word.chars().next().unwrap()) {
                format!("{word}ma")
            } else {
                let mut chars = word.chars();
                let first = chars.next().unwrap();
                format!("{}{first}ma", chars.as_str())
            };
            goat.push_str(&"a".repeat(i + 1));
            out.push_str(&goat);
        }
        out
    }
}
