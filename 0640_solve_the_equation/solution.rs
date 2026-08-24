// LeetCode 0640 - Solve the Equation
// https://leetcode.com/problems/solve-the-equation/

impl Solution {
    fn parse(expr: &str) -> (i32, i32) {
        let chars: Vec<char> = expr.chars().collect();
        let mut coef = 0;
        let mut constant = 0;
        let mut i = 0;
        while i < chars.len() {
            let mut sign = 1;
            if chars[i] == '+' || chars[i] == '-' {
                sign = if chars[i] == '-' { -1 } else { 1 };
                i += 1;
            }
            let mut value = 0;
            let mut has_digit = false;
            while i < chars.len() && chars[i].is_ascii_digit() {
                has_digit = true;
                value = value * 10 + (chars[i] as i32 - '0' as i32);
                i += 1;
            }
            if i < chars.len() && chars[i] == 'x' {
                coef += sign * if has_digit { value } else { 1 };
                i += 1;
            } else {
                constant += sign * value;
            }
        }
        (coef, constant)
    }

    pub fn solve_equation(equation: String) -> String {
        let eq = equation.find('=').unwrap();
        let (left_coef, left_const) = Self::parse(&equation[..eq]);
        let (right_coef, right_const) = Self::parse(&equation[eq + 1..]);
        let coef = left_coef - right_coef;
        let constant = right_const - left_const;
        if coef == 0 {
            return if constant == 0 {
                "Infinite solutions".to_string()
            } else {
                "No solution".to_string()
            };
        }
        format!("x={}", constant / coef)
    }
}
