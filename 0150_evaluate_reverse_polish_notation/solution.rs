// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

// LeetCode 0150 - Evaluate Reverse Polish Notation
// https://leetcode.com/problems/evaluate-reverse-polish-notation/

impl Solution {
    pub fn eval_rpn(tokens: Vec<String>) -> i32 {
        let mut stack = Vec::new();
        for token in tokens {
            match token.as_str() {
                "+" | "-" | "*" | "/" => {
                    let right = stack.pop().unwrap();
                    let left = stack.pop().unwrap();
                    stack.push(match token.as_str() {
                        "+" => left + right,
                        "-" => left - right,
                        "*" => left * right,
                        _ => left / right,
                    });
                }
                _ => stack.push(token.parse().unwrap()),
            }
        }
        stack[0]
    }
}