// LeetCode 1297 - Maximum Number of Occurrences of a Substring
// https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn max_freq(s: String, max_letters: i32, min_size: i32, _max_size: i32) -> i32 {
        let min_size = min_size as usize;
        let bytes = s.as_bytes();
        let mut counts = HashMap::new();
        let mut best = 0;
        for i in 0..=bytes.len().saturating_sub(min_size) {
            let sub = &bytes[i..i + min_size];
            let seen: HashSet<_> = sub.iter().copied().collect();
            if seen.len() as i32 <= max_letters {
                let key = String::from_utf8(sub.to_vec()).unwrap();
                let e = counts.entry(key).or_insert(0);
                *e += 1;
                best = best.max(*e);
            }
        }
        best
    }
}
