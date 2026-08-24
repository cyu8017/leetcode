// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

impl Solution {
    pub fn repeated_character(s: String) -> char {
        let mut seen = [false; 26];
        for c in s.chars() {
            let i = (c as u8 - b'a') as usize;
            if seen[i] {
                return c;
            }
            seen[i] = true;
        }
        '\0'
    }
}
