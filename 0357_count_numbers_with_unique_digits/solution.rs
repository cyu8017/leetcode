// LeetCode 0357 - Count Numbers with Unique Digits
// https://leetcode.com/problems/count-numbers-with-unique-digits/

impl Solution {
    pub fn count_numbers_with_unique_digits(n: i32) -> i32 {
        if n == 0 {
            return 1;
        }

        let mut total = 10;
        let mut unique = 9;
        let mut available = 9;

        for _ in 2..=n {
            unique *= available;
            available -= 1;
            total += unique;
        }

        total
    }
}
