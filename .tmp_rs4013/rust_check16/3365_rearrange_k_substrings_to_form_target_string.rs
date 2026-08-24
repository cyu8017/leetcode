struct Solution;
// LeetCode 3365 - Rearrange K Substrings to Form Target String
// https://leetcode.com/problems/rearrange-k-substrings-to-form-target-string/

use std::collections::HashMap;

impl Solution {
    pub fn is_possible_to_rearrange(s: String, t: String, k: i32) -> bool {
        let n = s.len();
        let sz = n / k as usize;
        let mut cnt: HashMap<String, i32> = HashMap::new();
        let mut i = 0;
        while i < n {
            *cnt.entry(s[i..i + sz].to_string()).or_insert(0) += 1;
            *cnt.entry(t[i..i + sz].to_string()).or_insert(0) -= 1;
            i += sz;
        }
        cnt.values().all(|&v| v == 0)
    }
}

fn main() {}
