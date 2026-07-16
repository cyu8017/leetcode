// LeetCode 0029 - Divide Two Integers
// https://leetcode.com/problems/divide-two-integers/

impl Solution {
    pub fn divide(dividend: i32, divisor: i32) -> i32 {
        if dividend == i32::MIN && divisor == -1 {
            return i32::MAX;
        }
        let negative = (dividend < 0) ^ (divisor < 0);
        let mut dividend = dividend.abs() as i64;
        let mut divisor = divisor.abs() as i64;
        let mut quotient = 0i64;

        for i in (0..=31).rev() {
            if (dividend >> i) >= divisor {
                quotient += 1 << i;
                dividend -= divisor << i;
            }
        }

        if negative {
            -quotient as i32
        } else {
            quotient as i32
        }
    }
}
