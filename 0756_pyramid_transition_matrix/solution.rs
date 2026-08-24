// LeetCode 0756 - Pyramid Transition Matrix
// https://leetcode.com/problems/pyramid-transition-matrix/

use std::collections::HashMap;

impl Solution {
    pub fn pyramid_transition(bottom: String, allowed: Vec<String>) -> bool {
        let mut transitions: HashMap<String, Vec<char>> = HashMap::new();
        for triple in allowed {
            transitions
                .entry(triple[..2].to_string())
                .or_default()
                .push(triple.chars().nth(2).unwrap());
        }
        let mut memo = HashMap::new();
        Self::dfs(&bottom, &transitions, &mut memo)
    }

    fn dfs(
        row: &str,
        transitions: &HashMap<String, Vec<char>>,
        memo: &mut HashMap<String, bool>,
    ) -> bool {
        if row.len() == 1 {
            return true;
        }
        if let Some(&cached) = memo.get(row) {
            return cached;
        }
        let mut options = Vec::new();
        for i in 0..row.len() - 1 {
            let key = &row[i..i + 2];
            match transitions.get(key) {
                Some(found) => options.push(found.clone()),
                None => {
                    memo.insert(row.to_string(), false);
                    return false;
                }
            }
        }
        let mut path = String::new();
        let ok = Self::build(0, &options, &mut path, transitions, memo);
        memo.insert(row.to_string(), ok);
        ok
    }

    fn build(
        index: usize,
        options: &[Vec<char>],
        path: &mut String,
        transitions: &HashMap<String, Vec<char>>,
        memo: &mut HashMap<String, bool>,
    ) -> bool {
        if index == options.len() {
            return Self::dfs(path, transitions, memo);
        }
        for &ch in &options[index] {
            path.push(ch);
            if Self::build(index + 1, options, path, transitions, memo) {
                return true;
            }
            path.pop();
        }
        false
    }
}
