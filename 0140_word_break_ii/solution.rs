// LeetCode 0140 - Word Break II
use std::collections::{HashMap, HashSet};
impl Solution {
    pub fn word_break(s: String, word_dict: Vec<String>) -> Vec<String> {
        fn dfs(start: usize, s: &str, words: &HashSet<&str>, memo: &mut HashMap<usize, Vec<String>>) -> Vec<String> {
            if let Some(result) = memo.get(&start) { return result.clone(); }
            if start == s.len() { return vec![String::new()]; }
            let mut result = Vec::new();
            for end in start + 1..=s.len() {
                let word = &s[start..end];
                if !words.contains(word) { continue; }
                for tail in dfs(end, s, words, memo) {
                    result.push(if tail.is_empty() { word.to_string() } else { format!("{word} {tail}") });
                }
            }
            memo.insert(start, result.clone());
            result
        }
        let words: HashSet<&str> = word_dict.iter().map(String::as_str).collect();
        dfs(0, &s, &words, &mut HashMap::new())
    }
}