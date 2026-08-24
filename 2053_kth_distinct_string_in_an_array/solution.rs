// LeetCode 2053 - Kth Distinct String in an Array
// https://leetcode.com/problems/kth-distinct-string-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn kth_distinct(arr: Vec<String>, mut k: i32) -> String {
        let mut freq = HashMap::new();
        for s in &arr {
            *freq.entry(s.clone()).or_insert(0) += 1;
        }
        for s in arr {
            if freq[&s] == 1 {
                k -= 1;
                if k == 0 {
                    return s;
                }
            }
        }
        String::new()
    }
}
