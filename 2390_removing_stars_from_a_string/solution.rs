// LeetCode 2390 - Removing Stars From a String
// https://leetcode.com/problems/removing-stars-from-a-string/

impl Solution {
    pub fn remove_stars(s: String) -> String {
        let mut stack = String::new();
        for c in s.chars() {
            if c == '*' {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        stack
    }
}
