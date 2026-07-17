// LeetCode 1784 - Check if Binary String Has at Most One Segment of Ones
// https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/

impl Solution {
    pub fn check_ones_segment(s: String) -> bool {
        let trimmed = s.trim_matches('0');
        !trimmed.contains("01")
    }
}
