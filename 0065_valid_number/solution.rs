// LeetCode 0065 - Valid Number
// https://leetcode.com/problems/valid-number/

impl Solution {
    pub fn is_number(s: String) -> bool {
        let bytes = s.as_bytes();
        let mut seen_digit = false;
        let mut seen_dot = false;
        let mut seen_exp = false;

        for (i, &ch) in bytes.iter().enumerate() {
            match ch {
                b'0'..=b'9' => seen_digit = true,
                b'+' | b'-' => {
                    if i > 0 && bytes[i - 1] != b'e' && bytes[i - 1] != b'E' {
                        return false;
                    }
                }
                b'e' | b'E' => {
                    if seen_exp || !seen_digit {
                        return false;
                    }
                    seen_exp = true;
                    seen_digit = false;
                    seen_dot = false;
                }
                b'.' => {
                    if seen_dot || seen_exp {
                        return false;
                    }
                    seen_dot = true;
                }
                _ => return false,
            }
        }

        seen_digit
    }
}
