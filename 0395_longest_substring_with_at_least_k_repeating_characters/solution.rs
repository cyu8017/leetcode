// LeetCode 0395 - Longest Substring with At Least K Repeating Characters
// https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/

use std::collections::HashMap;

impl Solution {
    pub fn longest_substring(s: String, k: i32) -> i32 {
        if s.is_empty() {
            return 0;
        }

        let bytes = s.as_bytes();
        let mut counts: HashMap<u8, i32> = HashMap::new();
        for &ch in bytes {
            *counts.entry(ch).or_insert(0) += 1;
        }

        for (&ch, &count) in counts.iter() {
            if count < k {
                let mut best = 0;
                let mut part = Vec::new();
                for &value in bytes {
                    if value == ch {
                        best = best.max(Self::longest_substring(
                            String::from_utf8(part.clone()).unwrap(),
                            k,
                        ));
                        part.clear();
                    } else {
                        part.push(value);
                    }
                }
                best = best.max(Self::longest_substring(
                    String::from_utf8(part).unwrap(),
                    k,
                ));
                return best;
            }
        }

        bytes.len() as i32
    }
}
