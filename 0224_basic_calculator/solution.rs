// LeetCode 0224 - Basic Calculator
// https://leetcode.com/problems/basic-calculator/

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let mut stack: Vec<i32> = Vec::new();
        let mut result = 0;
        let mut number = 0;
        let mut sign = 1;
        for ch in s.chars() {
            if ch.is_ascii_digit() {
                number = number * 10 + (ch as i32 - '0' as i32);
            } else if ch == '+' || ch == '-' {
                result += sign * number;
                number = 0;
                sign = if ch == '+' { 1 } else { -1 };
            } else if ch == '(' {
                stack.push(result);
                stack.push(sign);
                result = 0;
                sign = 1;
            } else if ch == ')' {
                result += sign * number;
                number = 0;
                result *= stack.pop().unwrap();
                result += stack.pop().unwrap();
            }
        }
        result + sign * number
    }
}
