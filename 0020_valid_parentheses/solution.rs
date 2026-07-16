// LeetCode 0020 - Valid Parentheses
// https://leetcode.com/problems/valid-parentheses/

use std::collections::HashMap;

impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack: Vec<char> = Vec::new();
        let pairs = HashMap::from([(')', '('), (']', '['), ('}', '{')]);

        for ch in s.chars() {
            match ch {
                '(' | '[' | '{' => stack.push(ch),
                _ => {
                    if stack.pop() != pairs.get(&ch).copied() {
                        return false;
                    }
                }
            }
        }

        stack.is_empty()
    }
}
