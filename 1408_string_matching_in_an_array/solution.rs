// LeetCode 1408 - String Matching in an Array
// https://leetcode.com/problems/string-matching-in-an-array/

impl Solution {
    pub fn string_matching(words: Vec<String>) -> Vec<String> {
        words
            .iter()
            .enumerate()
            .filter(|(i, word)| {
                words
                    .iter()
                    .enumerate()
                    .any(|(j, other)| i != &j && other.contains(word.as_str()))
            })
            .map(|(_, w)| w.clone())
            .collect()
    }
}
