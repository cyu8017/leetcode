// LeetCode 2114 - Maximum Number of Words Found in Sentences
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

impl Solution {
    pub fn most_words_found(sentences: Vec<String>) -> i32 {
        sentences
            .iter()
            .map(|s| s.bytes().filter(|&c| c == b' ').count() as i32 + 1)
            .max()
            .unwrap_or(0)
    }
}
