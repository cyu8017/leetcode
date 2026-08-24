struct Solution;
// LeetCode 2506 - Count Pairs Of Similar Strings
// https://leetcode.com/problems/count-pairs-of-similar-strings/

use std::collections::HashMap;

impl Solution {
    pub fn similar_pairs(words: Vec<String>) -> i32 {
        let mut freq: HashMap<u32, i32> = HashMap::new();
        let mut ans = 0;
        for w in words {
            let mut mask = 0u32;
            for c in w.bytes() {
                mask |= 1 << (c - b'a');
            }
            ans += *freq.get(&mask).unwrap_or(&0);
            *freq.entry(mask).or_insert(0) += 1;
        }
        ans
    }
}

fn main() {}
