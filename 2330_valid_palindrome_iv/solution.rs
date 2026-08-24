// LeetCode 2330 - Valid Palindrome IV
// https://leetcode.com/problems/valid-palindrome-iv/

impl Solution {
    pub fn make_palindrome(s: String) -> bool {
        let b = s.as_bytes();
        let mut diff = 0;
        let mut i = 0;
        let mut j = b.len() as i32 - 1;
        while i < j {
            if b[i as usize] != b[j as usize] {
                diff += 1;
                if diff > 2 {
                    return false;
                }
            }
            i += 1;
            j -= 1;
        }
        true
    }
}
