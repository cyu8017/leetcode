// LeetCode 0400 - Nth Digit
// https://leetcode.com/problems/nth-digit/

impl Solution {
    pub fn find_nth_digit(n: i32) -> i32 {
        let mut n = n as i64;
        let mut digits = 1;
        let mut count = 9_i64;
        let mut start = 1_i64;

        while n > digits as i64 * count {
            n -= digits as i64 * count;
            digits += 1;
            count *= 10;
            start *= 10;
        }

        let number = start + (n - 1) / digits as i64;
        let text = number.to_string();
        (text.as_bytes()[((n - 1) % digits as i64) as usize] - b'0') as i32
    }
}
