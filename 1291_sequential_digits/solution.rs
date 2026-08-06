// LeetCode 1291 - Sequential Digits
// https://leetcode.com/problems/sequential-digits/

impl Solution {
    pub fn sequential_digits(low: i32, high: i32) -> Vec<i32> {
        let digits = b"123456789";
        let mut answer = Vec::new();
        for length in 2..=9 {
            for start in 0..=9 - length {
                let mut value = 0;
                for i in start..start + length {
                    value = value * 10 + (digits[i] - b'0') as i32;
                }
                if value >= low && value <= high {
                    answer.push(value);
                }
            }
        }
        answer
    }
}
