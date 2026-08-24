// LeetCode 0625 - Minimum Factorization
// https://leetcode.com/problems/minimum-factorization/

impl Solution {
    pub fn smallest_factorization(mut num: i32) -> i32 {
        if num < 10 {
            return num;
        }
        let mut digits = Vec::new();
        for digit in (2..=9).rev() {
            while num % digit == 0 {
                digits.push(digit);
                num /= digit;
            }
        }
        if num != 1 {
            return 0;
        }
        let mut result = 0i64;
        for &d in digits.iter().rev() {
            result = result * 10 + d as i64;
            if result > i32::MAX as i64 {
                return 0;
            }
        }
        result as i32
    }
}
