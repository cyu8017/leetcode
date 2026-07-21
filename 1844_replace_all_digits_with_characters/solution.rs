// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

impl Solution {
    pub fn replace_digits(s: String) -> String {
        let mut chars: Vec<u8> = s.into_bytes();
        let mut i = 1;
        while i < chars.len() {
            chars[i] = chars[i - 1] + (chars[i] - b'0');
            i += 2;
        }
        String::from_utf8(chars).unwrap()
    }
}
