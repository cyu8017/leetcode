// LeetCode 1614 - Maximum Nesting Depth of the Parentheses
// https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/

impl Solution {
    pub fn max_depth(s: String) -> i32 {
        let mut depth = 0;
        let mut ans = 0;
        for ch in s.bytes() {
            if ch == b'(' {
                depth += 1;
                ans = ans.max(depth);
            } else if ch == b')' {
                depth -= 1;
            }
        }
        ans
    }
}
