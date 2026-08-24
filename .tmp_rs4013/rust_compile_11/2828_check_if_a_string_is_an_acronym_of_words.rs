struct Solution;
fn main() {}

// LeetCode 2828 - Check if a String Is an Acronym of Words
// https://leetcode.com/problems/check-if-a-string-is-an-acronym-of-words/

impl Solution {
    pub fn is_acronym(words: Vec<String>, s: String) -> bool {
        if words.len() != s.len() {
            return false;
        }
        let sb = s.as_bytes();
        for (i, w) in words.iter().enumerate() {
            if w.is_empty() || w.as_bytes()[0] != sb[i] {
                return false;
            }
        }
        true
    }
}
