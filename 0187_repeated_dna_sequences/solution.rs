// LeetCode 0187 - Repeated DNA Sequences
// https://leetcode.com/problems/repeated-dna-sequences/

use std::collections::HashSet;

impl Solution {
    pub fn find_repeated_dna_sequences(s: String) -> Vec<String> {
        let mut seen = HashSet::new();
        let mut repeated = HashSet::new();
        for i in 0..s.len().saturating_sub(9) {
            let sequence = &s[i..i + 10];
            if !seen.insert(sequence) {
                repeated.insert(sequence.to_string());
            }
        }
        repeated.into_iter().collect()
    }
}