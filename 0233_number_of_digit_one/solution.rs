// LeetCode 0233 - Number of Digit One
// https://leetcode.com/problems/number-of-digit-one/

impl Solution {
    pub fn count_digit_one(n: i32) -> i32 {
        let mut count: i64 = 0;
        let mut factor: i64 = 1;
        let mut value = n as i64;
        while factor <= value {
            let lower = value % factor;
            let current = (value / factor) % 10;
            let higher = value / (factor * 10);
            count += match current {
                0 => higher * factor,
                1 => higher * factor + lower + 1,
                _ => (higher + 1) * factor,
            };
            factor *= 10;
        }
        count as i32
    }
}
