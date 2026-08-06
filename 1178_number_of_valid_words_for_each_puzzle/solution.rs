// LeetCode 1178 - Number of Valid Words for Each Puzzle
// https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/

use std::collections::HashMap;

impl Solution {
    pub fn find_num_of_valid_words(words: Vec<String>, puzzles: Vec<String>) -> Vec<i32> {
        fn mask_of(s: &str) -> i32 {
            let mut mask = 0;
            for b in s.bytes() {
                mask |= 1 << (b - b'a');
            }
            mask
        }
        let mut freq = HashMap::new();
        for w in &words {
            *freq.entry(mask_of(w)).or_insert(0) += 1;
        }
        puzzles
            .iter()
            .map(|puzzle| {
                let first = 1 << (puzzle.as_bytes()[0] - b'a');
                let full = mask_of(puzzle);
                let mut sub = full;
                let mut total = 0;
                loop {
                    if sub & first != 0 {
                        total += freq.get(&sub).copied().unwrap_or(0);
                    }
                    if sub == 0 {
                        break;
                    }
                    sub = (sub - 1) & full;
                }
                total
            })
            .collect()
    }
}
