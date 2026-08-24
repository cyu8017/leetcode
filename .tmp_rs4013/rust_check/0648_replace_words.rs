struct Solution;
// LeetCode 0648 - Replace Words
// https://leetcode.com/problems/replace-words/

use std::collections::HashSet;

impl Solution {
    pub fn replace_words(dictionary: Vec<String>, sentence: String) -> String {
        let roots: HashSet<String> = dictionary.into_iter().collect();
        sentence
            .split_whitespace()
            .map(|word| {
                for i in 1..=word.len() {
                    if roots.contains(&word[..i]) {
                        return word[..i].to_string();
                    }
                }
                word.to_string()
            })
            .collect::<Vec<_>>()
            .join(" ")
    }
}

fn main() {}
