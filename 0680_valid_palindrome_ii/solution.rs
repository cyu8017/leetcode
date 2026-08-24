// LeetCode 0680 - Valid Palindrome II
// https://leetcode.com/problems/valid-palindrome-ii/

impl Solution {
    pub fn valid_palindrome(s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        let mut left = 0usize;
        let mut right = chars.len().saturating_sub(1);
        while left < right {
            if chars[left] != chars[right] {
                return Self::is_palindrome(&chars, left + 1, right)
                    || Self::is_palindrome(&chars, left, right - 1);
            }
            left += 1;
            right -= 1;
        }
        true
    }

    fn is_palindrome(chars: &[char], mut left: usize, mut right: usize) -> bool {
        while left < right {
            if chars[left] != chars[right] {
                return false;
            }
            left += 1;
            right -= 1;
        }
        true
    }
}
