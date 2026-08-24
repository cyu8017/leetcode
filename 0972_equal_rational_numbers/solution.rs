// LeetCode 0972 - Equal Rational Numbers
// https://leetcode.com/problems/equal-rational-numbers/

impl Solution {
    pub fn is_rational_equal(s: String, t: String) -> bool {
        fn parse(x: &str) -> f64 {
            if !x.contains('(') {
                return if x.is_empty() { 0.0 } else { x.parse().unwrap_or(0.0) };
            }
            let lp = x.find('(').unwrap();
            let mut non_rep = x[..lp].to_string();
            let rep = &x[lp + 1..x.len() - 1];
            if !non_rep.contains('.') {
                non_rep.push('.');
            }
            let dot = non_rep.find('.').unwrap();
            let integer = &non_rep[..dot];
            let frac = &non_rep[dot + 1..];
            let mut base: f64 = if integer.is_empty() {
                0.0
            } else {
                integer.parse().unwrap()
            };
            if !frac.is_empty() {
                let mut denom = 1.0;
                for _ in 0..frac.len() {
                    denom *= 10.0;
                }
                base += frac.parse::<f64>().unwrap() / denom;
            }
            if !rep.is_empty() {
                let rep_val: f64 = rep.parse().unwrap();
                let mut cycle = 1.0;
                for _ in 0..rep.len() {
                    cycle *= 10.0;
                }
                let mut denom = cycle - 1.0;
                for _ in 0..frac.len() {
                    denom *= 10.0;
                }
                base += rep_val / denom;
            }
            base
        }
        (parse(&s) - parse(&t)).abs() < 1e-12
    }
}
