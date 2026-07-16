// LeetCode 0409 - Longest Palindrome
// https://leetcode.com/problems/longest-palindrome/

use std::collections::HashMap;

impl Solution {
    pub fn longest_palindrome(s: String) -> i32 {
        let mut counts = HashMap::new();
        for ch in s.bytes() {
            *counts.entry(ch).or_insert(0) += 1;
        }

        let mut length = 0;
        let mut has_odd = false;
        for count in counts.values() {
            length += (count / 2) * 2;
            if count % 2 == 1 {
                has_odd = true;
            }
        }

        length + if has_odd { 1 } else { 0 }
    }
}
