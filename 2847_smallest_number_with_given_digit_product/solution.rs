// LeetCode 2847 - Smallest Number With Given Digit Product
// https://leetcode.com/problems/smallest-number-with-given-digit-product/

impl Solution {
    pub fn smallest_number(n: i64) -> String {
        if n == 0 {
            return "0".to_string();
        }
        if n == 1 {
            return "1".to_string();
        }
        let mut n = n;
        let mut digits = String::new();
        for d in (2..=9).rev() {
            while n % d == 0 {
                digits.push(char::from(b'0' + d as u8));
                n /= d;
            }
        }
        if n > 1 {
            return "-1".to_string();
        }
        digits.chars().rev().collect()
    }
}
