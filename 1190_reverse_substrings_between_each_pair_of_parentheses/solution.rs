// LeetCode 1190 - Reverse Substrings Between Each Pair of Parentheses
// https://leetcode.com/problems/reverse-substrings-between-each-pair-of-parentheses/

impl Solution {
    pub fn reverse_parentheses(s: String) -> String {
        let mut stack: Vec<u8> = Vec::new();
        for &ch in s.as_bytes() {
            if ch == b')' {
                let mut chunk = Vec::new();
                while stack.last() != Some(&b'(') {
                    chunk.push(stack.pop().unwrap());
                }
                stack.pop();
                stack.extend(chunk);
            } else {
                stack.push(ch);
            }
        }
        String::from_utf8(stack).unwrap()
    }
}
