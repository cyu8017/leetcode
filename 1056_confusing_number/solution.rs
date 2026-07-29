// LeetCode 1056 - Confusing Number
// https://leetcode.com/problems/confusing-number/

impl Solution {
    pub fn confusing_number(n: i32) -> bool {
        let rotate = |ch: u8| -> Option<u8> {
            match ch {
                b'0' => Some(b'0'),
                b'1' => Some(b'1'),
                b'6' => Some(b'9'),
                b'8' => Some(b'8'),
                b'9' => Some(b'6'),
                _ => None,
            }
        };
        let s = n.to_string();
        let mut rotated = Vec::with_capacity(s.len());
        for ch in s.bytes().rev() {
            match rotate(ch) {
                Some(r) => rotated.push(r),
                None => return false,
            }
        }
        rotated != s.as_bytes()
    }
}
