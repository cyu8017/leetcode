// LeetCode 1332 - Remove Palindromic Subsequences
// https://leetcode.com/problems/remove-palindromic-subsequences/

impl Solution {
    pub fn remove_palindrome_sub(s: String) -> i32 {
        if s.is_empty() {
            return 0;
        }
        if s.chars().eq(s.chars().rev()) {
            1
        } else {
            2
        }
    }
}
