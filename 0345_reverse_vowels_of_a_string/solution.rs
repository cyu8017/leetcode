// LeetCode 0345 - Reverse Vowels of a String
// https://leetcode.com/problems/reverse-vowels-of-a-string/

use std::collections::HashSet;

impl Solution {
    pub fn reverse_vowels(s: String) -> String {
        let vowels: HashSet<char> = "aeiouAEIOU".chars().collect();
        let mut chars: Vec<char> = s.chars().collect();
        let mut left = 0;
        let mut right = chars.len().saturating_sub(1);

        while left < right {
            while left < right && !vowels.contains(&chars[left]) {
                left += 1;
            }
            while left < right && !vowels.contains(&chars[right]) {
                right -= 1;
            }
            chars.swap(left, right);
            left += 1;
            right -= 1;
        }

        chars.into_iter().collect()
    }
}
