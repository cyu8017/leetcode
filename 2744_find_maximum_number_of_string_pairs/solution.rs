// LeetCode 2744 - Find Maximum Number of String Pairs
// https://leetcode.com/problems/find-maximum-number-of-string-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_number_of_string_pairs(words: Vec<String>) -> i32 {
        let mut freq: HashMap<String, i32> = HashMap::new();
        let mut ans = 0;
        for w in words {
            let rev: String = w.chars().rev().collect();
            if let Some(c) = freq.get_mut(&rev) {
                if *c > 0 {
                    *c -= 1;
                    ans += 1;
                    continue;
                }
            }
            *freq.entry(w).or_insert(0) += 1;
        }
        ans
    }
}
