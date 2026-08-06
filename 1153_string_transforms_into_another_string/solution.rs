// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn can_convert(str1: String, str2: String) -> bool {
        if str1 == str2 {
            return true;
        }
        let mut mapping = HashMap::new();
        for (a, b) in str1.bytes().zip(str2.bytes()) {
            if let Some(&v) = mapping.get(&a) {
                if v != b {
                    return false;
                }
            } else {
                mapping.insert(a, b);
            }
        }
        str2.bytes().collect::<HashSet<_>>().len() < 26
    }
}
