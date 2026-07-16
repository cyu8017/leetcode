// LeetCode 0214 - Shortest Palindrome
// https://leetcode.com/problems/shortest-palindrome/

impl Solution {
    pub fn shortest_palindrome(s: String) -> String {
        if s.is_empty() {
            return String::new();
        }
        let reversed: String = s.chars().rev().collect();
        let combined = format!("{s}#{reversed}");
        let mut pi = vec![0; combined.len()];
        let bytes = combined.as_bytes();
        let mut lps = 0usize;
        for i in 1..bytes.len() {
            while lps > 0 && bytes[i] != bytes[lps] {
                lps = pi[lps - 1];
            }
            if bytes[i] == bytes[lps] {
                lps += 1;
            }
            pi[i] = lps;
        }
        let prefix_len = pi[combined.len() - 1];
        format!("{}{}", &reversed[..s.len() - prefix_len], s)
    }
}
