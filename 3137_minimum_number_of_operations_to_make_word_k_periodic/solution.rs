// LeetCode 3137 - Minimum Number of Operations to Make Word K-Periodic
// https://leetcode.com/problems/minimum-number-of-operations-to-make-word-k-periodic/

use std::collections::HashMap;

impl Solution {
    pub fn minimum_operations_to_make_k_periodic(word: String, k: i32) -> i32 {
        let k = k as usize;
        let n = word.len();
        let mut cnt: HashMap<&str, i32> = HashMap::new();
        let mut mx = 0;
        let mut i = 0;
        while i < n {
            let s = &word[i..i + k];
            let e = cnt.entry(s).or_insert(0);
            *e += 1;
            mx = mx.max(*e);
            i += k;
        }
        n as i32 / k as i32 - mx
    }
}
