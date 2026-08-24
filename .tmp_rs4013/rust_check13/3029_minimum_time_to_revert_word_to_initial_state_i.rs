#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 3029 - Minimum Time to Revert Word to Initial State I
// https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-i/

impl Solution {
    pub fn minimum_time_to_initial_state(word: String, k: i32) -> i32 {
        let n = word.len();
        let k = k as usize;
        let mut i = k;
        while i < n {
            if &word[i..] == &word[..n - i] {
                return (i / k) as i32;
            }
            i += k;
        }
        ((n + k - 1) / k) as i32
    }
}
