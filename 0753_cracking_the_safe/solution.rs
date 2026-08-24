// LeetCode 0753 - Cracking the Safe
// https://leetcode.com/problems/cracking-the-safe/

use std::collections::HashSet;

impl Solution {
    pub fn crack_safe(n: i32, k: i32) -> String {
        let mut seen = HashSet::new();
        let mut path = Vec::new();
        let start = "0".repeat((n - 1) as usize);
        Self::dfs(&start, k, &mut seen, &mut path);
        let mut result: String = path.into_iter().collect();
        result.push_str(&start);
        result
    }

    fn dfs(node: &str, k: i32, seen: &mut HashSet<String>, path: &mut Vec<char>) {
        for d in 0..k {
            let digit = (b'0' + d as u8) as char;
            let edge = format!("{}{}", node, digit);
            if seen.insert(edge.clone()) {
                Self::dfs(&edge[1..], k, seen, path);
                path.push(digit);
            }
        }
    }
}
