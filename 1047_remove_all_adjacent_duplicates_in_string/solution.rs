// LeetCode 1047 - Remove All Adjacent Duplicates In String
// https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/

impl Solution {
    pub fn remove_duplicates(s: String) -> String {
        let mut stack = String::new();
        for ch in s.chars() {
            if stack.chars().last() == Some(ch) {
                stack.pop();
            } else {
                stack.push(ch);
            }
        }
        stack
    }
}
