// LeetCode 0504 - Base 7
// https://leetcode.com/problems/base-7/

impl Solution {
    pub fn convert_to_base7(mut num: i32) -> String {
        if num == 0 {
            return "0".to_string();
        }
        let negative = num < 0;
        if negative {
            num = -num;
        }
        let mut digits = Vec::new();
        while num > 0 {
            digits.push((num % 7) as u8 + b'0');
            num /= 7;
        }
        digits.reverse();
        let mut result = String::from_utf8(digits).unwrap();
        if negative {
            result.insert(0, '-');
        }
        result
    }
}
