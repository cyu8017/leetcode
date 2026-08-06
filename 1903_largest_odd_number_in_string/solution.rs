// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

impl Solution {
    pub fn largest_odd_number(num: String) -> String {
        let bytes = num.as_bytes();
        for i in (0..bytes.len()).rev() {
            if (bytes[i] - b'0') % 2 == 1 {
                return num[..=i].to_string();
            }
        }
        String::new()
    }
}
