// LeetCode 2116 - Check if a Parentheses String Can Be Valid
// https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/

impl Solution {
    pub fn can_be_valid(s: String, locked: String) -> bool {
        let n = s.len();
        if n % 2 == 1 {
            return false;
        }
        let s = s.as_bytes();
        let locked = locked.as_bytes();
        let mut bal = 0i32;
        for i in 0..n {
            if locked[i] == b'0' || s[i] == b'(' {
                bal += 1;
            } else {
                bal -= 1;
            }
            if bal < 0 {
                return false;
            }
        }
        bal = 0;
        for i in (0..n).rev() {
            if locked[i] == b'0' || s[i] == b')' {
                bal += 1;
            } else {
                bal -= 1;
            }
            if bal < 0 {
                return false;
            }
        }
        true
    }
}
