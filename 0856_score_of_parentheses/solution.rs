// LeetCode 0856 - Score of Parentheses
// https://leetcode.com/problems/score-of-parentheses/

impl Solution {
    pub fn score_of_parentheses(s: String) -> i32 {
        let mut stack = vec![0];
        for ch in s.chars() {
            if ch == '(' {
                stack.push(0);
            } else {
                let val = stack.pop().unwrap();
                *stack.last_mut().unwrap() += (2 * val).max(1);
            }
        }
        stack[0]
    }
}
