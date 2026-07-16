// LeetCode 0166 - Fraction to Recurring Decimal
use std::collections::HashMap;
impl Solution {
    pub fn fraction_to_decimal(numerator: i32, denominator: i32) -> String {
        if numerator == 0 { return "0".to_string(); }
        let (mut n, mut d) = (numerator as i64, denominator as i64);
        let mut result = if (n < 0) != (d < 0) { "-".to_string() } else { String::new() };
        n = n.abs(); d = d.abs();
        result.push_str(&(n / d).to_string());
        let mut remainder = n % d;
        if remainder == 0 { return result; }
        result.push('.');
        let mut seen = HashMap::new();
        while remainder != 0 {
            if let Some(&position) = seen.get(&remainder) {
                result.insert(position, '('); result.push(')'); break;
            }
            seen.insert(remainder, result.len());
            remainder *= 10;
            result.push(char::from(b'0' + (remainder / d) as u8));
            remainder %= d;
        }
        result
    }
}