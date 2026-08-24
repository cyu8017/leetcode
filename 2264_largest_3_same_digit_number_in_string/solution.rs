// LeetCode 2264 - Largest 3-Same-Digit Number in String
// https://leetcode.com/problems/largest-3-same-digit-number-in-string/

impl Solution {
    pub fn largest_good_integer(num: String) -> String {
        let mut best = String::new();
        let bytes = num.as_bytes();
        for i in 0..bytes.len().saturating_sub(2) {
            if bytes[i] == bytes[i + 1] && bytes[i] == bytes[i + 2] {
                let cand = &num[i..i + 3];
                if cand > best.as_str() {
                    best = cand.to_string();
                }
            }
        }
        best
    }
}
