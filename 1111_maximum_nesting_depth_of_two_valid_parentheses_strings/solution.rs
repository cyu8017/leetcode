// LeetCode 1111 - Maximum Nesting Depth of Two Valid Parentheses Strings
// https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/

impl Solution {
    pub fn max_depth_after_split(seq: String) -> Vec<i32> {
        let mut depth = 0;
        let mut ans = Vec::with_capacity(seq.len());
        for ch in seq.bytes() {
            if ch == b'(' {
                ans.push(depth % 2);
                depth += 1;
            } else {
                depth -= 1;
                ans.push(depth % 2);
            }
        }
        ans
    }
}
