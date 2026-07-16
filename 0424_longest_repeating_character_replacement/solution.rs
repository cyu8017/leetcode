// LeetCode 0424 - Longest Repeating Character Replacement
// https://leetcode.com/problems/longest-repeating-character-replacement/

use std::collections::HashMap;

impl Solution {
    pub fn character_replacement(s: String, k: i32) -> i32 {
        let bytes = s.as_bytes();
        let mut counts: HashMap<u8, i32> = HashMap::new();
        let mut left = 0;
        let mut best = 0;
        let mut max_count = 0;

        for right in 0..bytes.len() {
            let ch = bytes[right];
            let count = counts.entry(ch).or_insert(0);
            *count += 1;
            max_count = max_count.max(*count);

            while (right as i32 - left as i32 + 1) - max_count > k {
                let left_ch = bytes[left];
                if let Some(value) = counts.get_mut(&left_ch) {
                    *value -= 1;
                }
                left += 1;
            }

            best = best.max(right as i32 - left as i32 + 1);
        }

        best
    }
}
