struct Solution;
// LeetCode 0592 - Fraction Addition and Subtraction
// https://leetcode.com/problems/fraction-addition-and-subtraction/

impl Solution {
    fn gcd(mut a: i64, mut b: i64) -> i64 {
        a = a.abs();
        b = b.abs();
        while b != 0 {
            let t = a % b;
            a = b;
            b = t;
        }
        a
    }

    pub fn fraction_addition(expression: String) -> String {
        let chars: Vec<char> = expression.chars().collect();
        let mut numerator = 0i64;
        let mut denominator = 1i64;
        let mut i = 0;
        while i < chars.len() {
            let mut sign = 1i64;
            if chars[i] == '+' || chars[i] == '-' {
                if chars[i] == '-' {
                    sign = -1;
                }
                i += 1;
            }
            let mut a = 0i64;
            while i < chars.len() && chars[i].is_ascii_digit() {
                a = a * 10 + (chars[i] as i64 - '0' as i64);
                i += 1;
            }
            a *= sign;
            i += 1;
            let mut b = 0i64;
            while i < chars.len() && chars[i].is_ascii_digit() {
                b = b * 10 + (chars[i] as i64 - '0' as i64);
                i += 1;
            }
            numerator = numerator * b + a * denominator;
            denominator *= b;
            let g = Self::gcd(numerator, denominator);
            numerator /= g;
            denominator /= g;
        }
        format!("{}/{}", numerator, denominator)
    }
}

fn main() {}
