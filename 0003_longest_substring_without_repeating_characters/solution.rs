// LeetCode 0003 - Longest Substring Without Repeating Characters
// https://leetcode.com/problems/longest-substring-without-repeating-characters/

use std::collections::HashMap;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut last: HashMap<u8, i32> = HashMap::new();
        let mut best = 0;
        let mut start = 0;

        for (i, &ch) in bytes.iter().enumerate() {
            if let Some(&prev) = last.get(&ch) {
                if prev >= start {
                    start = prev + 1;
                }
            }
            last.insert(ch, i as i32);
            best = best.max(i as i32 - start + 1);
        }

        best
    }
}
