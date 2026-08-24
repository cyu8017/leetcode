// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

impl Solution {
    pub fn process_str(s: String) -> String {
        let mut result = String::new();
        for c in s.chars() {
            if c.is_ascii_alphabetic() {
                result.push(c);
            } else if c == '*' {
                result.pop();
            } else if c == '#' {
                result.push_str(&result.clone());
            } else if c == '%' {
                result = result.chars().rev().collect();
            }
        }
        result
    }
}
