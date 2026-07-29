// LeetCode 1021 - Remove Outermost Parentheses
// https://leetcode.com/problems/remove-outermost-parentheses/

impl Solution {
    pub fn remove_outer_parentheses(s: String) -> String {
        let mut ans = String::new();
        let mut depth = 0;
        for ch in s.chars() {
            if ch == '(' {
                if depth > 0 {
                    ans.push(ch);
                }
                depth += 1;
            } else {
                depth -= 1;
                if depth > 0 {
                    ans.push(ch);
                }
            }
        }
        ans
    }
}
