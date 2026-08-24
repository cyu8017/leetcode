// LeetCode 0820 - Short Encoding of Words
// https://leetcode.com/problems/short-encoding-of-words/

use std::collections::HashSet;

impl Solution {
    pub fn minimum_length_encoding(words: Vec<String>) -> i32 {
        let mut good: HashSet<String> = words.iter().cloned().collect();
        for word in &words {
            for i in 1..word.len() {
                good.remove(&word[i..]);
            }
        }
        good.iter().map(|word| word.len() as i32 + 1).sum()
    }
}
