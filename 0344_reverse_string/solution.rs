// LeetCode 0344 - Reverse String
// https://leetcode.com/problems/reverse-string/

impl Solution {
    pub fn reverse_string(s: &mut Vec<char>) {
        let mut left = 0;
        let mut right = s.len().saturating_sub(1);
        while left < right {
            s.swap(left, right);
            left += 1;
            right -= 1;
        }
    }
}
