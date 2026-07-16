// LeetCode 0472 - Concatenated Words
// https://leetcode.com/problems/concatenated-words/

use std::collections::HashSet;

impl Solution {
    fn can_form(word: &str, dictionary: &HashSet<String>) -> bool {
        if word.is_empty() {
            return true;
        }
        let length = word.len();
        let mut dp = vec![false; length + 1];
        dp[0] = true;
        for end in 1..=length {
            for start in 0..end {
                if dp[start] && dictionary.contains(&word[start..end]) {
                    dp[end] = true;
                    break;
                }
            }
        }
        dp[length]
    }

    pub fn find_all_concatenated_words_in_a_dict(words: Vec<String>) -> Vec<String> {
        let mut words = words;
        words.sort_by_key(|word| word.len());

        let mut word_set: HashSet<String> = words.iter().cloned().collect();
        let mut result = Vec::new();
        for word in &words {
            word_set.remove(word);
            if Self::can_form(word, &word_set) {
                result.push(word.clone());
            }
            word_set.insert(word.clone());
        }
        result
    }
}
