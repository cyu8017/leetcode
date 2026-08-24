struct Solution;
fn main() {}

// LeetCode 2788 - Split Strings by Separator
// https://leetcode.com/problems/split-strings-by-separator/

impl Solution {
    pub fn split_words_by_separator(words: Vec<String>, separator: char) -> Vec<String> {
        let mut ans = Vec::new();
        for w in words {
            let b = w.as_bytes();
            let mut start = 0;
            for i in 0..=b.len() {
                if i == b.len() || b[i] == separator as u8 {
                    if i > start {
                        ans.push(w[start..i].to_string());
                    }
                    start = i + 1;
                }
            }
        }
        ans
    }
}
