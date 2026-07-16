// LeetCode 0139 - Word Break
use std::collections::HashSet;
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> bool {
        let words: HashSet<&str> = word_dict.iter().map(String::as_str).collect();
        let mut dp = vec![false; s.len() + 1]; dp[0] = true;
        for i in 1..=s.len() {
            for j in 0..i {
                if dp[j] && words.contains(&s[j..i]) { dp[i] = true; break; }
            }
        }
        dp[s.len()]
    }
}