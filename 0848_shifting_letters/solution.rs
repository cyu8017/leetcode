// LeetCode 0848 - Shifting Letters
// https://leetcode.com/problems/shifting-letters/

impl Solution {
    pub fn shifting_letters(s: String, shifts: Vec<i32>) -> String {
        let mut bytes = s.into_bytes();
        let mut total = 0i32;
        for i in (0..bytes.len()).rev() {
            total = (total + shifts[i]) % 26;
            bytes[i] = ((bytes[i] - b'a' + total as u8) % 26) + b'a';
        }
        String::from_utf8(bytes).unwrap()
    }
}
