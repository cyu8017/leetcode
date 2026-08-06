// LeetCode 1910 - Remove All Occurrences of a Substring
// https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

impl Solution {
    pub fn remove_occurrences(s: String, part: String) -> String {
        let mut stack = String::new();
        let m = part.len();
        for ch in s.chars() {
            stack.push(ch);
            if stack.len() >= m && stack.ends_with(&part) {
                stack.truncate(stack.len() - m);
            }
        }
        stack
    }
}
