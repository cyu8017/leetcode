// LeetCode 1554 - Strings Differ by One Character
// https://leetcode.com/problems/strings-differ-by-one-character/

use std::collections::HashSet;

impl Solution {
    pub fn differ_by_one(dict: Vec<String>) -> bool {
        let mut seen = HashSet::new();
        for word in dict {
            let bytes = word.as_bytes();
            for i in 0..bytes.len() {
                let mut pattern = bytes.to_vec();
                pattern[i] = b'*';
                let key = String::from_utf8(pattern).unwrap();
                if seen.contains(&key) {
                    return true;
                }
                seen.insert(key);
            }
        }
        false
    }
}
