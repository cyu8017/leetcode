// LeetCode 1930 - Unique Length-3 Palindromic Subsequences
// https://leetcode.com/problems/unique-length-3-palindromic-subsequences/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn count_palindromic_subsequence(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut first = HashMap::new();
        let mut last = HashMap::new();
        for (i, &c) in bytes.iter().enumerate() {
            first.entry(c).or_insert(i);
            last.insert(c, i);
        }
        let mut ans = 0;
        for (&c, &fi) in &first {
            let li = last[&c];
            if li - fi > 1 {
                let mid: HashSet<u8> = bytes[fi + 1..li].iter().copied().collect();
                ans += mid.len() as i32;
            }
        }
        ans
    }
}
