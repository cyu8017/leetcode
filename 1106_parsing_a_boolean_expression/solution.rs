// LeetCode 1106 - Parsing A Boolean Expression
// https://leetcode.com/problems/parsing-a-boolean-expression/

impl Solution {
    pub fn parse_bool_expr(expression: String) -> bool {
        let mut stack: Vec<u8> = Vec::new();
        for &ch in expression.as_bytes() {
            if ch == b')' {
                let mut values = Vec::new();
                while let Some(&top) = stack.last() {
                    if top == b'&' || top == b'|' || top == b'!' {
                        break;
                    }
                    let token = stack.pop().unwrap();
                    if token == b't' || token == b'f' {
                        values.push(token == b't');
                    }
                }
                let op = stack.pop().unwrap();
                let result = match op {
                    b'!' => !values[0],
                    b'&' => values.iter().all(|&v| v),
                    _ => values.iter().any(|&v| v),
                };
                stack.push(if result { b't' } else { b'f' });
            } else if ch != b',' {
                stack.push(ch);
            }
        }
        stack.last() == Some(&b't')
    }
}
