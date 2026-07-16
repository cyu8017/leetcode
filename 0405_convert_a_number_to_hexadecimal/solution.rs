// LeetCode 0405 - Convert a Number to Hexadecimal
// https://leetcode.com/problems/convert-a-number-to-hexadecimal/

impl Solution {
    pub fn to_hex(num: i32) -> String {
        if num == 0 {
            return "0".to_string();
        }

        const DIGITS: &[u8; 16] = b"0123456789abcdef";
        let mut value = num as u32;
        let mut result = Vec::new();

        while value > 0 {
            result.push(DIGITS[(value & 15) as usize]);
            value >>= 4;
        }

        result.reverse();
        String::from_utf8(result).unwrap()
    }
}
