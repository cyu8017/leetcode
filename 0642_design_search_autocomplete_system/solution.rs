// LeetCode 0642 - Design Search Autocomplete System
// https://leetcode.com/problems/design-search-autocomplete-system/

use std::collections::HashMap;

pub struct AutocompleteSystem {
    counts: HashMap<String, i32>,
    current: String,
}

impl AutocompleteSystem {
    pub fn new(sentences: Vec<String>, times: Vec<i32>) -> Self {
        let mut counts = HashMap::new();
        for (sentence, time) in sentences.into_iter().zip(times) {
            *counts.entry(sentence).or_insert(0) += time;
        }
        Self {
            counts,
            current: String::new(),
        }
    }

    pub fn input(&mut self, c: char) -> Vec<String> {
        if c == '#' {
            *self.counts.entry(self.current.clone()).or_insert(0) += 1;
            self.current.clear();
            return Vec::new();
        }
        self.current.push(c);
        let mut matches: Vec<String> = self
            .counts
            .keys()
            .filter(|s| s.starts_with(&self.current))
            .cloned()
            .collect();
        matches.sort_by(|a, b| {
            let ca = self.counts[a];
            let cb = self.counts[b];
            if ca != cb {
                cb.cmp(&ca)
            } else {
                a.cmp(b)
            }
        });
        matches.truncate(3);
        matches
    }
}
