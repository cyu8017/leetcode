// LeetCode 0527 - Word Abbreviation
// https://leetcode.com/problems/word-abbreviation/

use std::collections::HashMap;

impl Solution {
    pub fn words_abbreviation(words: Vec<String>) -> Vec<String> {
        fn abbreviate(word: &str, prefix: usize) -> String {
            if prefix + 2 >= word.len() {
                return word.to_string();
            }
            let middle = word.len() - prefix - 1;
            let candidate = format!("{}{}{}", &word[..prefix], middle, word.chars().last().unwrap());
            if candidate.len() < word.len() {
                candidate
            } else {
                word.to_string()
            }
        }

        let mut prefixes = vec![1; words.len()];
        let mut changed = true;
        while changed {
            changed = false;
            let mut groups: HashMap<String, Vec<usize>> = HashMap::new();
            for (index, word) in words.iter().enumerate() {
                groups
                    .entry(abbreviate(word, prefixes[index]))
                    .or_default()
                    .push(index);
            }
            for indices in groups.values() {
                if indices.len() > 1 {
                    changed = true;
                    for &index in indices {
                        prefixes[index] += 1;
                    }
                }
            }
        }

        words
            .iter()
            .enumerate()
            .map(|(index, word)| abbreviate(word, prefixes[index]))
            .collect()
    }
}
