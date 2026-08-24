// LeetCode 2278 - Percentage of Letter in String
// https://leetcode.com/problems/percentage-of-letter-in-string/

impl Solution {
    pub fn percentage_letter(s: String, letter: char) -> i32 {
        let cnt = s.chars().filter(|&c| c == letter).count() as i32;
        cnt * 100 / s.len() as i32
    }
}
