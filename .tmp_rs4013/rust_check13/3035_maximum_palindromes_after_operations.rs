#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3035 - Maximum Palindromes After Operations
// https://leetcode.com/problems/maximum-palindromes-after-operations/

impl Solution {
    pub fn max_palindromes_after_operations(mut words: Vec<String>) -> i32 {
        let mut s = 0i32;
        let mut mask = 0u32;
        for w in &words {
            s += w.len() as i32;
            for c in w.bytes() {
                mask ^= 1 << (c - b'a');
            }
        }
        s -= mask.count_ones() as i32;
        words.sort_by_key(|w| w.len());
        let mut ans = 0;
        for w in &words {
            s -= (w.len() as i32 / 2) * 2;
            if s < 0 {
                break;
            }
            ans += 1;
        }
        ans
    }
}
