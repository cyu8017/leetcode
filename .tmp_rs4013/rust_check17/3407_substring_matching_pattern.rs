struct Solution;
// LeetCode 3407 - Substring Matching Pattern
// https://leetcode.com/problems/substring-matching-pattern/

impl Solution {
    pub fn has_match(s: String, p: String) -> bool {
        let i = p.find('*').unwrap();
        let left = &p[..i];
        let right = &p[i + 1..];
        if let Some(li) = s.find(left) {
            s[li + left.len()..].contains(right)
        } else {
            false
        }
    }
}

fn main() {}
