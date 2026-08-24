struct Solution;
// LeetCode 2423 - Remove Letter To Equalize Frequency
// https://leetcode.com/problems/remove-letter-to-equalize-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn equal_frequency(word: String) -> bool {
        let b = word.as_bytes();
        for skip in 0..b.len() {
            let mut cnt = [0i32; 26];
            for (i, &ch) in b.iter().enumerate() {
                if i == skip {
                    continue;
                }
                cnt[(ch - b'a') as usize] += 1;
            }
            let mut freq: HashMap<i32, i32> = HashMap::new();
            for c in cnt {
                if c > 0 {
                    *freq.entry(c).or_insert(0) += 1;
                }
            }
            if freq.len() == 1 {
                return true;
            }
        }
        false
    }
}

fn main() {}
