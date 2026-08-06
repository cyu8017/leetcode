// LeetCode 1417 - Reformat The String
// https://leetcode.com/problems/reformat-the-string/

impl Solution {
    pub fn reformat(s: String) -> String {
        let mut letters = Vec::new();
        let mut digits = Vec::new();
        for c in s.chars() {
            if c.is_ascii_alphabetic() {
                letters.push(c);
            } else {
                digits.push(c);
            }
        }
        if (letters.len() as i32 - digits.len() as i32).abs() > 1 {
            return String::new();
        }
        if digits.len() >= letters.len() {
            std::mem::swap(&mut letters, &mut digits);
        }
        let mut answer = String::new();
        for (i, &ch) in letters.iter().enumerate() {
            answer.push(ch);
            if i < digits.len() {
                answer.push(digits[i]);
            }
        }
        answer
    }
}
