// LeetCode 0241 - Different Ways to Add Parentheses
// https://leetcode.com/problems/different-ways-to-add-parentheses/

impl Solution {
    pub fn diff_ways_to_compute(expression: String) -> Vec<i32> {
        if expression.chars().all(|ch| ch.is_ascii_digit()) {
            return vec![expression.parse().unwrap()];
        }
        let mut result = Vec::new();
        let bytes = expression.as_bytes();
        for index in 0..bytes.len() {
            let operator = bytes[index] as char;
            if operator != '+' && operator != '-' && operator != '*' {
                continue;
            }
            let left = Self::diff_ways_to_compute(expression[..index].to_string());
            let right = Self::diff_ways_to_compute(expression[index + 1..].to_string());
            for &left_value in &left {
                for &right_value in &right {
                    result.push(match operator {
                        '+' => left_value + right_value,
                        '-' => left_value - right_value,
                        _ => left_value * right_value,
                    });
                }
            }
        }
        result
    }
}
