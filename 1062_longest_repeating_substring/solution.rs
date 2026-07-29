// LeetCode 1062 - Longest Repeating Substring
// https://leetcode.com/problems/longest-repeating-substring/

use std::collections::HashSet;

impl Solution {
    pub fn longest_repeating_substring(s: String) -> i32 {
        let n = s.len();
        let bytes = s.as_bytes();

        let has_dup = |length: usize| -> bool {
            let mut seen = HashSet::new();
            for i in 0..=n - length {
                let sub = &bytes[i..i + length];
                if !seen.insert(sub) {
                    return true;
                }
            }
            false
        };

        let mut lo = 1usize;
        let mut hi = n.saturating_sub(1);
        let mut ans = 0i32;
        while lo <= hi {
            let mid = (lo + hi) / 2;
            if has_dup(mid) {
                ans = mid as i32;
                lo = mid + 1;
            } else {
                if mid == 0 {
                    break;
                }
                hi = mid - 1;
            }
        }
        ans
    }
}
