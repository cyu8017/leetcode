// LeetCode 0772 - Basic Calculator III
// https://leetcode.com/problems/basic-calculator-iii/

impl Solution {
    pub fn calculate(s: String) -> i32 {
        let expr: Vec<char> = s.chars().filter(|ch| !ch.is_whitespace()).collect();
        let mut i = 0;
        Self::parse(&expr, &mut i)
    }

    fn parse(expr: &[char], i: &mut usize) -> i32 {
        let mut stack = Vec::new();
        let mut num: i64 = 0;
        let mut sign = '+';
        while *i < expr.len() {
            let ch = expr[*i];
            if ch.is_ascii_digit() {
                num = num * 10 + (ch as i64 - '0' as i64);
            } else if ch == '(' {
                *i += 1;
                num = Self::parse(expr, i) as i64;
            }
            if (!ch.is_ascii_digit() && ch != '(') || *i == expr.len() - 1 {
                if matches!(ch, '+' | '-' | '*' | '/' | ')') || *i == expr.len() - 1 {
                    match sign {
                        '+' => stack.push(num),
                        '-' => stack.push(-num),
                        '*' => {
                            let top = stack.pop().unwrap();
                            stack.push(top * num);
                        }
                        '/' => {
                            let top = stack.pop().unwrap();
                            stack.push(top / num);
                        }
                        _ => {}
                    }
                    if ch == ')' {
                        return stack.iter().sum::<i64>() as i32;
                    }
                    sign = ch;
                    num = 0;
                }
            }
            *i += 1;
        }
        stack.iter().sum::<i64>() as i32
    }
}
