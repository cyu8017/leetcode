// LeetCode 0880 - Decoded String at Index
// https://leetcode.com/problems/decoded-string-at-index/

impl Solution {
    pub fn decode_at_index(s: String, k: i32) -> String {
        let bytes = s.as_bytes();
        let mut size: i64 = 0;
        for &ch in bytes {
            if ch.is_ascii_digit() {
                size *= (ch - b'0') as i64;
            } else {
                size += 1;
            }
        }
        let mut kk = k as i64;
        for &ch in bytes.iter().rev() {
            kk %= size;
            if kk == 0 && ch.is_ascii_alphabetic() {
                return (ch as char).to_string();
            }
            if ch.is_ascii_digit() {
                size /= (ch - b'0') as i64;
            } else {
                size -= 1;
            }
        }
        String::new()
    }
}
