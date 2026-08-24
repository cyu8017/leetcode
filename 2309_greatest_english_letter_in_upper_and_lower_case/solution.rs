// LeetCode 2309 - Greatest English Letter in Upper and Lower Case
// https://leetcode.com/problems/greatest-english-letter-in-upper-and-lower-case/

impl Solution {
    pub fn greatest_letter(s: String) -> String {
        let mut lower = [false; 26];
        let mut upper = [false; 26];
        for c in s.chars() {
            if c.is_ascii_lowercase() {
                lower[(c as u8 - b'a') as usize] = true;
            } else if c.is_ascii_uppercase() {
                upper[(c as u8 - b'A') as usize] = true;
            }
        }
        for i in (0..26).rev() {
            if lower[i] && upper[i] {
                return ((b'A' + i as u8) as char).to_string();
            }
        }
        String::new()
    }
}
