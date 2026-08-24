// LeetCode 2299 - Strong Password Checker II
// https://leetcode.com/problems/strong-password-checker-ii/

impl Solution {
    pub fn strong_password_checker_ii(password: String) -> bool {
        if password.len() < 8 {
            return false;
        }
        let special = "!@#$%^&*()-+";
        let mut has_lower = false;
        let mut has_upper = false;
        let mut has_digit = false;
        let mut has_special = false;
        let bytes = password.as_bytes();
        for i in 0..bytes.len() {
            let c = bytes[i] as char;
            if i > 0 && c == bytes[i - 1] as char {
                return false;
            }
            if c.is_ascii_lowercase() {
                has_lower = true;
            } else if c.is_ascii_uppercase() {
                has_upper = true;
            } else if c.is_ascii_digit() {
                has_digit = true;
            } else if special.contains(c) {
                has_special = true;
            }
        }
        has_lower && has_upper && has_digit && has_special
    }
}
