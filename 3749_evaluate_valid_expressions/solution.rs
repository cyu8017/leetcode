// LeetCode 3749 - Evaluate Valid Expressions
// https://leetcode.com/problems/evaluate-valid-expressions/

impl Solution {
    pub fn evaluate_expression(expression: String) -> i64 {
        fn parse(i: usize, expression: &[u8]) -> (i64, usize) {
            if expression[i].is_ascii_digit() || expression[i] == b'-' {
                let mut j = i;
                if expression[j] == b'-' {
                    j += 1;
                }
                while j < expression.len() && expression[j].is_ascii_digit() {
                    j += 1;
                }
                let val = std::str::from_utf8(&expression[i..j])
                    .unwrap()
                    .parse::<i64>()
                    .unwrap();
                return (val, j);
            }
            let mut j = i;
            while expression[j] != b'(' {
                j += 1;
            }
            let op = std::str::from_utf8(&expression[i..j]).unwrap();
            j += 1;
            let (val1, next_j1) = parse(j, expression);
            j = next_j1 + 1;
            let (val2, next_j2) = parse(j, expression);
            j = next_j2 + 1;
            let res = match op {
                "add" => val1 + val2,
                "sub" => val1 - val2,
                "mul" => val1 * val2,
                "div" => val1 / val2,
                _ => 0,
            };
            (res, j)
        }
        parse(0, expression.as_bytes()).0
    }
}
