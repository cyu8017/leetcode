// LeetCode 0420 - Strong Password Checker
// https://leetcode.com/problems/strong-password-checker/

impl Solution {
    pub fn strong_password_checker(password: String) -> i32 {
        let chars: Vec<char> = password.chars().collect();
        let length = chars.len();
        let mut missing = 3;

        let has_lower = chars.iter().any(|ch| ch.is_ascii_lowercase());
        let has_upper = chars.iter().any(|ch| ch.is_ascii_uppercase());
        let has_digit = chars.iter().any(|ch| ch.is_ascii_digit());

        if has_lower {
            missing -= 1;
        }
        if has_upper {
            missing -= 1;
        }
        if has_digit {
            missing -= 1;
        }

        let mut replace = 0;
        let mut one_repeat = 0;
        let mut two_repeat = 0;
        let mut index = 0;
        while index < length {
            let mut run = 1;
            while index + run < length && chars[index + run] == chars[index] {
                run += 1;
            }
            if run >= 3 {
                replace += run / 3;
                match run % 3 {
                    0 => one_repeat += 1,
                    1 => two_repeat += 1,
                    _ => {}
                }
            }
            index += run;
        }

        if length < 6 {
            return (6 - length).max(missing as usize) as i32;
        }
        if length <= 20 {
            return missing.max(replace as i32);
        }

        let mut delete_count = length - 20;
        replace -= delete_count.min(one_repeat);
        delete_count -= delete_count.min(one_repeat);
        replace -= (delete_count / 2).min(two_repeat);
        delete_count -= (delete_count / 2).min(two_repeat) * 2;
        replace -= delete_count / 3;
        (length - 20) as i32 + missing.max(replace as i32)
    }
}
