// LeetCode 1455 - Check If a Word Occurs As a Prefix of Any Word in a Sentence
// https://leetcode.com/problems/check-if-a-word-occurs-as-a-prefix-of-any-word-in-a-sentence/

impl Solution {
    pub fn is_prefix_of_word(sentence: String, search_word: String) -> i32 {
        sentence
            .split_whitespace()
            .enumerate()
            .find(|(_, w)| w.starts_with(&search_word))
            .map(|(i, _)| i as i32 + 1)
            .unwrap_or(-1)
    }
}
