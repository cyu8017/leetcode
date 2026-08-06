// LeetCode 1328 - Break a Palindrome
// https://leetcode.com/problems/break-a-palindrome/

impl Solution {
    pub fn break_palindrome(palindrome: String) -> String {
        let mut chars: Vec<char> = palindrome.chars().collect();
        if chars.len() == 1 {
            return String::new();
        }
        for i in 0..chars.len() / 2 {
            if chars[i] != 'a' {
                chars[i] = 'a';
                return chars.into_iter().collect();
            }
        }
        let last = chars.len() - 1;
        chars[last] = 'b';
        chars.into_iter().collect()
    }
}
