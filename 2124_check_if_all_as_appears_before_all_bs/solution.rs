// LeetCode 2124 - Check if All A's Appears Before All B's
// https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/

impl Solution {
    pub fn check_string(s: String) -> bool {
        let mut seen_b = false;
        for c in s.chars() {
            if c == 'b' {
                seen_b = true;
            } else if seen_b {
                return false;
            }
        }
        true
    }
}
