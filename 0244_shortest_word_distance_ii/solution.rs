// LeetCode 0244 - Shortest Word Distance II
// https://leetcode.com/problems/shortest-word-distance-ii/

use std::collections::HashMap;

struct WordDistance {
    positions: HashMap<String, Vec<i32>>,
}

impl WordDistance {
    fn new(words_dict: Vec<String>) -> Self {
        let mut positions: HashMap<String, Vec<i32>> = HashMap::new();
        for (index, word) in words_dict.into_iter().enumerate() {
            positions.entry(word).or_default().push(index as i32);
        }
        Self { positions }
    }

    fn shortest(&self, word1: String, word2: String) -> i32 {
        let left = &self.positions[&word1];
        let right = &self.positions[&word2];
        let mut i = 0usize;
        let mut j = 0usize;
        let mut best = i32::MAX;
        while i < left.len() && j < right.len() {
            best = best.min((left[i] - right[j]).abs());
            if left[i] <= right[j] {
                i += 1;
            } else {
                j += 1;
            }
        }
        best
    }
}
