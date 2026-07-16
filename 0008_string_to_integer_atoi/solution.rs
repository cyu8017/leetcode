// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

impl Solution {
    pub fn my_atoi(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut i = 0usize;

        while i < bytes.len() && bytes[i] == b' ' {
            i += 1;
        }
        if i >= bytes.len() {
            return 0;
        }

        let mut sign = 1i32;
        if bytes[i] == b'-' {
            sign = -1;
            i += 1;
        } else if bytes[i] == b'+' {
            i += 1;
        }

        let mut result = 0i32;
        while i < bytes.len() && bytes[i].is_ascii_digit() {
            let digit = (bytes[i] - b'0') as i32;
            if result > (i32::MAX - digit) / 10 {
                return if sign == -1 { i32::MIN } else { i32::MAX };
            }
            result = result * 10 + digit;
            i += 1;
        }

        sign * result
    }
}
