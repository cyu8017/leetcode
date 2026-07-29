// LeetCode 1048 - Longest String Chain
// https://leetcode.com/problems/longest-string-chain/

use std::collections::HashMap;

impl Solution {
    pub fn longest_str_chain(mut words: Vec<String>) -> i32 {
        words.sort_unstable_by_key(|w| w.len());
        let mut dp: HashMap<String, i32> = HashMap::new();
        let mut ans = 1;
        for w in words {
            let mut best = 1;
            let bytes = w.as_bytes();
            for i in 0..bytes.len() {
                let mut prev = String::with_capacity(bytes.len() - 1);
                prev.push_str(std::str::from_utf8(&bytes[..i]).unwrap());
                prev.push_str(std::str::from_utf8(&bytes[i + 1..]).unwrap());
                if let Some(&v) = dp.get(&prev) {
                    best = best.max(v + 1);
                }
            }
            dp.insert(w, best);
            ans = ans.max(best);
        }
        ans
    }
}
