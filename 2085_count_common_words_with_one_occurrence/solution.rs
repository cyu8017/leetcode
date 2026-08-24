// LeetCode 2085 - Count Common Words With One Occurrence
// https://leetcode.com/problems/count-common-words-with-one-occurrence/

use std::collections::HashMap;

impl Solution {
    pub fn count_words(words1: Vec<String>, words2: Vec<String>) -> i32 {
        let mut f1 = HashMap::new();
        let mut f2 = HashMap::new();
        for w in words1 {
            *f1.entry(w).or_insert(0) += 1;
        }
        for w in words2 {
            *f2.entry(w).or_insert(0) += 1;
        }
        f1.iter()
            .filter(|(w, &c)| c == 1 && *f2.get(*w).unwrap_or(&0) == 1)
            .count() as i32
    }
}
