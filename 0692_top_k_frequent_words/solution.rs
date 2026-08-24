// LeetCode 0692 - Top K Frequent Words
// https://leetcode.com/problems/top-k-frequent-words/

use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(words: Vec<String>, k: i32) -> Vec<String> {
        let mut counts = HashMap::new();
        for word in words {
            *counts.entry(word).or_insert(0) += 1;
        }
        let mut ordered: Vec<String> = counts.keys().cloned().collect();
        ordered.sort_by(|a, b| {
            let ca = counts[a];
            let cb = counts[b];
            if ca != cb {
                cb.cmp(&ca)
            } else {
                a.cmp(b)
            }
        });
        ordered.truncate(k as usize);
        ordered
    }
}
