// LeetCode 0340 - Longest Substring with At Most K Distinct Characters
// https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring_k_distinct(s: String, k: i32) -> i32 {
        if k == 0 {
            return 0;
        }

        let bytes = s.as_bytes();
        let mut counts: HashMap<u8, i32> = HashMap::new();
        let mut left = 0;
        let mut best = 0;

        for right in 0..bytes.len() {
            *counts.entry(bytes[right]).or_insert(0) += 1;
            while counts.len() as i32 > k {
                let left_char = bytes[left];
                if let Some(value) = counts.get_mut(&left_char) {
                    *value -= 1;
                    if *value == 0 {
                        counts.remove(&left_char);
                    }
                }
                left += 1;
            }
            best = best.max((right - left + 1) as i32);
        }

        best
    }
}
