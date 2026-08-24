// LeetCode 0966 - Vowel Spellchecker
// https://leetcode.com/problems/vowel-spellchecker/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn spellchecker(wordlist: Vec<String>, queries: Vec<String>) -> Vec<String> {
        fn lower(w: &str) -> String {
            w.to_ascii_lowercase()
        }
        fn devowel(w: &str) -> String {
            lower(w)
                .chars()
                .map(|c| match c {
                    'a' | 'e' | 'i' | 'o' | 'u' => '*',
                    _ => c,
                })
                .collect()
        }
        let exact: HashSet<String> = wordlist.iter().cloned().collect();
        let mut lower_map = HashMap::new();
        let mut vowel_map = HashMap::new();
        for w in &wordlist {
            let low = lower(w);
            lower_map.entry(low).or_insert_with(|| w.clone());
            let dv = devowel(w);
            vowel_map.entry(dv).or_insert_with(|| w.clone());
        }
        queries
            .into_iter()
            .map(|q| {
                if exact.contains(&q) {
                    q
                } else if let Some(w) = lower_map.get(&lower(&q)) {
                    w.clone()
                } else if let Some(w) = vowel_map.get(&devowel(&q)) {
                    w.clone()
                } else {
                    String::new()
                }
            })
            .collect()
    }
}
