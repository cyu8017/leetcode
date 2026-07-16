// LeetCode 0076 - Minimum Window Substring
// https://leetcode.com/problems/minimum-window-substring/

use std::collections::HashMap;
use std::i32;

impl Solution {
    pub fn min_window(s: String, t: String) -> String {
        if t.is_empty() {
            return String::new();
        }

        let mut need: HashMap<u8, i32> = HashMap::new();
        for &ch in t.as_bytes() {
            *need.entry(ch).or_insert(0) += 1;
        }

        let required = need.len() as i32;
        let mut formed = 0;
        let mut window: HashMap<u8, i32> = HashMap::new();
        let bytes = s.as_bytes();
        let mut left = 0;
        let mut best_len = i32::MAX;
        let mut best_left = 0;

        for right in 0..bytes.len() {
            let ch = bytes[right];
            *window.entry(ch).or_insert(0) += 1;
            if let Some(&count) = need.get(&ch) {
                if window[&ch] == count {
                    formed += 1;
                }
            }

            while formed == required {
                let window_len = (right - left + 1) as i32;
                if window_len < best_len {
                    best_len = window_len;
                    best_left = left;
                }

                let left_ch = bytes[left];
                if let Some(entry) = window.get_mut(&left_ch) {
                    *entry -= 1;
                    if let Some(&count) = need.get(&left_ch) {
                        if *entry < count {
                            formed -= 1;
                        }
                    }
                }
                left += 1;
            }
        }

        if best_len == i32::MAX {
            return String::new();
        }

        String::from_utf8(bytes[best_left..best_left + best_len as usize].to_vec()).unwrap()
    }
}
