// LeetCode 1945 - Sum of Digits of String After Convert
// https://leetcode.com/problems/sum-of-digits-of-string-after-convert/

impl Solution {
    pub fn get_lucky(s: String, k: i32) -> i32 {
        let mut num: String = s
            .chars()
            .map(|c| (c as u8 - b'a' + 1).to_string())
            .collect();
        for _ in 0..k {
            let sum: u32 = num.chars().map(|d| d.to_digit(10).unwrap()).sum();
            num = sum.to_string();
        }
        num.parse().unwrap()
    }
}
