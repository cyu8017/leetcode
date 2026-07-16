// LeetCode 0479 - Largest Palindrome Product
// https://leetcode.com/problems/largest-palindrome-product/

impl Solution {
    fn build_palindrome(value: i32) -> i64 {
        let text = value.to_string();
        let reversed: String = text.chars().rev().collect();
        format!("{text}{reversed}").parse::<i64>().unwrap_or(0)
    }

    pub fn largest_palindrome(n: i32) -> i32 {
        if n == 1 {
            return 9;
        }
        let upper = 10_i32.pow(n as u32) - 1;
        let lower = 10_i32.pow((n - 1) as u32);
        for first in (lower..=upper).rev() {
            let candidate = Self::build_palindrome(first);
            let mut factor = upper;
            while i64::from(factor) * i64::from(factor) >= candidate {
                if candidate % i64::from(factor) == 0 {
                    let partner = candidate / i64::from(factor);
                    if partner >= i64::from(lower) && partner <= i64::from(upper) {
                        return (candidate % 1337) as i32;
                    }
                }
                factor -= 1;
            }
        }
        0
    }
}
