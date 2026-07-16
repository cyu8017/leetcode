// LeetCode 0227 - Basic Calculator II
// https://leetcode.com/problems/basic-calculator-ii/

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut stack: Vec<i32> = Vec::new();
        let mut number = 0;
        let mut operator = b'+';

        for index in 0..bytes.len() {
            let ch = bytes[index];
            if ch.is_ascii_digit() {
                number = number * 10 + (ch - b'0') as i32;
            }
            if ch == b'+' || ch == b'-' || ch == b'*' || ch == b'/' || index == bytes.len() - 1 {
                match operator {
                    b'+' => stack.push(number),
                    b'-' => stack.push(-number),
                    b'*' => {
                        let prev = stack.pop().unwrap();
                        stack.push(prev * number);
                    }
                    b'/' => {
                        let prev = stack.pop().unwrap();
                        stack.push(prev / number);
                    }
                    _ => {}
                }
                operator = ch;
                number = 0;
            }
        }

        stack.iter().sum()
    }
}
