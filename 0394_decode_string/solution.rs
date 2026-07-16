// LeetCode 0394 - Decode String
// https://leetcode.com/problems/decode-string/

impl Solution {
    pub fn decode_string(s: String) -> String {
        let mut stack: Vec<(String, i32)> = Vec::new();
        let mut current = String::new();
        let mut number = 0;

        for ch in s.chars() {
            if ch.is_ascii_digit() {
                number = number * 10 + (ch as i32 - '0' as i32);
            } else if ch == '[' {
                stack.push((current, number));
                current.clear();
                number = 0;
            } else if ch == ']' {
                let (previous, count) = stack.pop().unwrap();
                let repeated = current.repeat(count as usize);
                current = previous + &repeated;
            } else {
                current.push(ch);
            }
        }

        current
    }
}
