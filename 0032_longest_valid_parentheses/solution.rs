// LeetCode 0032 - Longest Valid Parentheses
// https://leetcode.com/problems/longest-valid-parentheses/

impl Solution {
    pub fn longest_valid_parentheses(&self, s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut stack = vec![-1];
        let mut best = 0;

        for (i, &ch) in bytes.iter().enumerate() {
            if ch == b'(' {
                stack.push(i as i32);
            } else {
                stack.pop();
                if stack.is_empty() {
                    stack.push(i as i32);
                } else {
                    best = best.max(i as i32 - *stack.last().unwrap());
                }
            }
        }

        best
    }
}
