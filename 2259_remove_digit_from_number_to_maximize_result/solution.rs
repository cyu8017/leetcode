// LeetCode 2259 - Remove Digit From Number to Maximize Result
// https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/

impl Solution {
    pub fn remove_digit(number: String, digit: char) -> String {
        let mut best = String::new();
        let bytes = number.as_bytes();
        for i in 0..bytes.len() {
            if bytes[i] as char == digit {
                let cand = format!("{}{}", &number[..i], &number[i + 1..]);
                if cand > best {
                    best = cand;
                }
            }
        }
        best
    }
}
