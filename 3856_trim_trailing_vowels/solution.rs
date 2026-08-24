// LeetCode 3856 - Trim Trailing Vowels
// https://leetcode.com/problems/trim-trailing-vowels/

impl Solution {
    pub fn trim_trailing_vowels(s: String) -> String {
        let bytes = s.as_bytes();
        let mut i = bytes.len() as i32 - 1;
        let is_vowel = |c: u8| matches!(c, b'a' | b'e' | b'i' | b'o' | b'u');
        while i >= 0 && is_vowel(bytes[i as usize]) {
            i -= 1;
        }
        s[..(i + 1) as usize].to_string()
    }
}
