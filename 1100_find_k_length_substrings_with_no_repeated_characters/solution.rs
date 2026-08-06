// LeetCode 1100 - Find K-Length Substrings With No Repeated Characters
// https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/

use std::collections::HashMap;

impl Solution {
    pub fn num_k_len_substr_no_repeats(s: String, k: i32) -> i32 {
        let k = k as usize;
        let s = s.as_bytes();
        if k > s.len() {
            return 0;
        }
        let mut window: HashMap<u8, i32> = HashMap::new();
        for i in 0..k {
            *window.entry(s[i]).or_insert(0) += 1;
        }
        let mut ans = if window.len() == k { 1 } else { 0 };
        for i in k..s.len() {
            *window.entry(s[i]).or_insert(0) += 1;
            let left = s[i - k];
            let c = window.get_mut(&left).unwrap();
            *c -= 1;
            if *c == 0 {
                window.remove(&left);
            }
            if window.len() == k {
                ans += 1;
            }
        }
        ans
    }
}
