// LeetCode 0844 - Backspace String Compare
// https://leetcode.com/problems/backspace-string-compare/

impl Solution {
    pub fn backspace_compare(s: String, t: String) -> bool {
        fn build(text: &str) -> String {
            let mut stack = String::new();
            for ch in text.chars() {
                if ch == '#' {
                    stack.pop();
                } else {
                    stack.push(ch);
                }
            }
            stack
        }
        build(&s) == build(&t)
    }
}
