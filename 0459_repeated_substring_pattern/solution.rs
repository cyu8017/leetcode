// LeetCode 0459 - Repeated Substring Pattern
// https://leetcode.com/problems/repeated-substring-pattern/

impl Solution {
    pub fn repeated_substring_pattern(s: String) -> bool {
        let doubled = format!("{s}{s}");
        doubled[1..doubled.len() - 1].contains(&s)
    }
}
