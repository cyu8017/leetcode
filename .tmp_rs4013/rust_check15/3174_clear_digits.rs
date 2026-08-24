struct Solution;
// LeetCode 3174 - Clear Digits
// https://leetcode.com/problems/clear-digits/

impl Solution {
    pub fn clear_digits(s: String) -> String {
        let mut stk = String::new();
        for c in s.chars() {
            if c.is_ascii_digit() {
                stk.pop();
            } else {
                stk.push(c);
            }
        }
        stk
    }
}

fn main() {}
