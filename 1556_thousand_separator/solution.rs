// LeetCode 1556 - Thousand Separator
// https://leetcode.com/problems/thousand-separator/

impl Solution {
    pub fn thousand_separator(n: i32) -> String {
        let mut s = n.to_string();
        let mut parts = Vec::new();
        while !s.is_empty() {
            let start = s.len().saturating_sub(3);
            parts.push(s[start..].to_string());
            s.truncate(start);
        }
        parts.reverse();
        parts.join(".")
    }
}
