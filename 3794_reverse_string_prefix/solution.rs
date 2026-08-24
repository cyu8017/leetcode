// LeetCode 3794 - Reverse String Prefix
// https://leetcode.com/problems/reverse-string-prefix/

impl Solution {
    pub fn reverse_prefix(s: String, k: i32) -> String {
        let mut bytes = s.into_bytes();
        bytes[..k as usize].reverse();
        String::from_utf8(bytes).unwrap()
    }
}
