// LeetCode 0678 - Valid Parenthesis String
// https://leetcode.com/problems/valid-parenthesis-string/

impl Solution {
    pub fn check_valid_string(s: String) -> bool {
        let mut lo = 0i32;
        let mut hi = 0i32;
        for ch in s.chars() {
            if ch == '(' {
                lo += 1;
                hi += 1;
            } else if ch == ')' {
                lo = (lo - 1).max(0);
                hi -= 1;
                if hi < 0 {
                    return false;
                }
            } else {
                lo = (lo - 1).max(0);
                hi += 1;
            }
        }
        lo == 0
    }
}
