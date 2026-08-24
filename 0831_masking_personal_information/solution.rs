// LeetCode 0831 - Masking Personal Information
// https://leetcode.com/problems/masking-personal-information/

impl Solution {
    pub fn mask_pii(s: String) -> String {
        if s.contains('@') {
            let s = s.to_ascii_lowercase();
            let at = s.find('@').unwrap();
            let name = &s[..at];
            let domain = &s[at + 1..];
            let first = name.chars().next().unwrap();
            let last = name.chars().last().unwrap();
            format!("{first}*****{last}@{domain}")
        } else {
            let digits: String = s.chars().filter(|ch| ch.is_ascii_digit()).collect();
            let local = &digits[digits.len() - 4..];
            let country = digits.len() as i32 - 10;
            if country == 0 {
                format!("***-***-{local}")
            } else {
                format!("+{}-***-***-{local}", "*".repeat(country as usize))
            }
        }
    }
}
