// LeetCode 0439 - Ternary Expression Parser
// https://leetcode.com/problems/ternary-expression-parser/

impl Solution {
    pub fn parse_ternary(expression: String) -> String {
        if !expression.contains('?') {
            return expression;
        }

        let bytes = expression.as_bytes();
        let mut separator = 2usize;
        let mut depth = 0;
        for index in 2..bytes.len() {
            match bytes[index] {
                b'?' => depth += 1,
                b':' if depth == 0 => {
                    separator = index;
                    break;
                }
                b':' => depth -= 1,
                _ => {}
            }
        }

        if bytes[0] == b'T' {
            return Self::parse_ternary(expression[2..separator].to_string());
        }
        Self::parse_ternary(expression[separator + 1..].to_string())
    }
}
