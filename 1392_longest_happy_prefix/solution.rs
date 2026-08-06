// LeetCode 1392 - Longest Happy Prefix
// https://leetcode.com/problems/longest-happy-prefix/

impl Solution {
    pub fn longest_prefix(s: String) -> String {
        let bytes = s.as_bytes();
        if bytes.is_empty() {
            return String::new();
        }
        let mut pi = vec![0; bytes.len()];
        for i in 1..bytes.len() {
            let mut j = pi[i - 1];
            while j > 0 && bytes[i] != bytes[j] {
                j = pi[j - 1];
            }
            if bytes[i] == bytes[j] {
                j += 1;
            }
            pi[i] = j;
        }
        s[..pi[bytes.len() - 1]].to_string()
    }
}
