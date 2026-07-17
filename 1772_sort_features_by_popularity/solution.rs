// LeetCode 1772 - Sort Features by Popularity
// https://leetcode.com/problems/sort-features-by-popularity/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn sort_features(features: Vec<String>, responses: Vec<String>) -> Vec<String> {
        let feature_set: HashSet<&String> = features.iter().collect();
        let mut count: HashMap<String, i32> = HashMap::new();
        for response in &responses {
            let mut seen: HashSet<&str> = HashSet::new();
            for word in response.split_whitespace() {
                if feature_set.contains(&word.to_string()) {
                    seen.insert(word);
                }
            }
            for word in seen {
                *count.entry(word.to_string()).or_insert(0) += 1;
            }
        }
        let mut result = features;
        result.sort_by(|a, b| {
            let ca = count.get(a).copied().unwrap_or(0);
            let cb = count.get(b).copied().unwrap_or(0);
            cb.cmp(&ca).then_with(|| a.cmp(b))
        });
        result
    }
}
