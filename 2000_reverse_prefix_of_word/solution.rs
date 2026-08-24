// LeetCode 2000 - Reverse Prefix of Word
// https://leetcode.com/problems/reverse-prefix-of-word/

impl Solution {
    pub fn reverse_prefix(word: String, ch: char) -> String {
        let bytes = word.as_bytes();
        if let Some(pos) = bytes.iter().position(|&c| c == ch as u8) {
            let mut v = word.into_bytes();
            v[..=pos].reverse();
            String::from_utf8(v).unwrap()
        } else {
            word
        }
    }
}
