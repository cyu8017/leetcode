// LeetCode 3136 - Valid Word
// https://leetcode.com/problems/valid-word/

impl Solution {
    pub fn is_valid(word: String) -> bool {
        if word.len() < 3 {
            return false;
        }
        let mut has_vowel = false;
        let mut has_consonant = false;
        let mut vs = [false; 26];
        for c in b"aeiou" {
            vs[(c - b'a') as usize] = true;
        }
        for c in word.bytes() {
            if c.is_ascii_alphabetic() {
                let lower = c.to_ascii_lowercase();
                if vs[(lower - b'a') as usize] {
                    has_vowel = true;
                } else {
                    has_consonant = true;
                }
            } else if !c.is_ascii_digit() {
                return false;
            }
        }
        has_vowel && has_consonant
    }
}
