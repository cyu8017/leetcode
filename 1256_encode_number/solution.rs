// LeetCode 1256 - Encode Number
// https://leetcode.com/problems/encode-number/

impl Solution {
    pub fn encode(mut num: i32) -> String {
        num += 1;
        let mut bits = String::new();
        while num > 0 {
            bits.insert(0, char::from(b'0' + (num % 2) as u8));
            num /= 2;
        }
        if bits.len() <= 1 {
            String::new()
        } else {
            bits[1..].to_string()
        }
    }
}
