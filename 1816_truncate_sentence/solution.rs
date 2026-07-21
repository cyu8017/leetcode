// LeetCode 1816 - Truncate Sentence
// https://leetcode.com/problems/truncate-sentence/

impl Solution {
    pub fn truncate_sentence(s: String, k: i32) -> String {
        s.split_whitespace()
            .take(k as usize)
            .collect::<Vec<_>>()
            .join(" ")
    }
}
