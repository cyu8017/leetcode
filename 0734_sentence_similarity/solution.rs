// LeetCode 0734 - Sentence Similarity
// https://leetcode.com/problems/sentence-similarity/

use std::collections::HashSet;

impl Solution {
    pub fn are_sentences_similar(
        sentence1: Vec<String>,
        sentence2: Vec<String>,
        similar_pairs: Vec<Vec<String>>,
    ) -> bool {
        if sentence1.len() != sentence2.len() {
            return false;
        }
        let mut pairs = HashSet::new();
        for pair in similar_pairs {
            pairs.insert(format!("{}#{}", pair[0], pair[1]));
            pairs.insert(format!("{}#{}", pair[1], pair[0]));
        }
        for (a, b) in sentence1.iter().zip(sentence2.iter()) {
            if a != b && !pairs.contains(&format!("{}#{}", a, b)) {
                return false;
            }
        }
        true
    }
}
