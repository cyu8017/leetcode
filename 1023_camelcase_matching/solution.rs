// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

impl Solution {
    pub fn camel_match(queries: Vec<String>, pattern: String) -> Vec<bool> {
        let pat: Vec<char> = pattern.chars().collect();
        queries
            .into_iter()
            .map(|q| {
                let mut i = 0;
                for ch in q.chars() {
                    if i < pat.len() && ch == pat[i] {
                        i += 1;
                    } else if ch.is_ascii_uppercase() {
                        return false;
                    }
                }
                i == pat.len()
            })
            .collect()
    }
}
