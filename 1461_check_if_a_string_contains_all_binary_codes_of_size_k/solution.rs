// LeetCode 1461 - Check If a String Contains All Binary Codes of Size K
// https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

use std::collections::HashSet;

impl Solution {
    pub fn has_all_codes(s: String, k: i32) -> bool {
        let k = k as usize;
        if s.len() < k {
            return false;
        }
        let set: HashSet<&str> = (0..=s.len() - k).map(|i| &s[i..i + k]).collect();
        set.len() == (1 << k)
    }
}
