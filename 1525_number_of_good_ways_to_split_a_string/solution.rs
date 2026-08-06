// LeetCode 1525 - Number of Good Ways to Split a String
// https://leetcode.com/problems/number-of-good-ways-to-split-a-string/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn num_splits(s: String) -> i32 {
        let bytes = s.as_bytes();
        let mut right: HashMap<u8, i32> = HashMap::new();
        for &ch in bytes {
            *right.entry(ch).or_insert(0) += 1;
        }
        let mut left = HashSet::new();
        let mut answer = 0;
        for i in 0..bytes.len() - 1 {
            let ch = bytes[i];
            left.insert(ch);
            let c = right.get_mut(&ch).unwrap();
            *c -= 1;
            if *c == 0 {
                right.remove(&ch);
            }
            if left.len() == right.len() {
                answer += 1;
            }
        }
        answer
    }
}
