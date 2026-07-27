// LeetCode 1694 - Reformat Phone Number
// https://leetcode.com/problems/reformat-phone-number/

impl Solution {
    pub fn reformat_number(number: String) -> String {
        let mut s: String = number.chars().filter(|c| c.is_ascii_digit()).collect();
        let mut out = Vec::new();
        while s.len() > 4 {
            out.push(s[..3].to_string());
            s = s[3..].to_string();
        }
        if s.len() == 4 {
            out.push(s[..2].to_string());
            out.push(s[2..].to_string());
        } else if !s.is_empty() {
            out.push(s);
        }
        out.join("-")
    }
}
