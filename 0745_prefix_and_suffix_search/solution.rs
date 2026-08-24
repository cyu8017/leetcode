// LeetCode 0745 - Prefix and Suffix Search
// https://leetcode.com/problems/prefix-and-suffix-search/

use std::collections::HashMap;

pub struct WordFilter {
    lookup: HashMap<String, i32>,
}

impl WordFilter {
    pub fn new(words: Vec<String>) -> Self {
        let mut lookup = HashMap::new();
        for (index, word) in words.into_iter().enumerate() {
            let size = word.len();
            for i in 0..=size {
                for j in 0..=size {
                    lookup.insert(format!("{}#{}", &word[..i], &word[j..]), index as i32);
                }
            }
        }
        Self { lookup }
    }

    pub fn f(&self, pref: String, suff: String) -> i32 {
        *self.lookup.get(&format!("{}#{}", pref, suff)).unwrap_or(&-1)
    }
}
