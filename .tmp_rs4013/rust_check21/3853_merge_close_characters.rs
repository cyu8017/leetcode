struct Solution;
// LeetCode 3853 - Merge Close Characters
// https://leetcode.com/problems/merge-close-characters/

use std::collections::HashMap;

impl Solution {
    pub fn merge_characters(s: String, k: i32) -> String {
        let mut last = HashMap::new();
        let mut ans = String::new();
        for c in s.chars() {
            let cur = ans.len() as i32;
            if let Some(&prev) = last.get(&c) {
                if cur - prev <= k {
                    continue;
                }
            }
            ans.push(c);
            last.insert(c, cur);
        }
        ans
    }
}
