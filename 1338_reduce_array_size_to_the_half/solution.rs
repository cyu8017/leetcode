// LeetCode 1338 - Reduce Array Size to The Half
// https://leetcode.com/problems/reduce-array-size-to-the-half/

use std::collections::HashMap;

impl Solution {
    pub fn min_set_size(arr: Vec<i32>) -> i32 {
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for v in &arr {
            *counts.entry(*v).or_insert(0) += 1;
        }
        let mut freqs: Vec<i32> = counts.values().copied().collect();
        freqs.sort_unstable_by(|a, b| b.cmp(a));
        let mut removed = 0;
        for (count, frequency) in freqs.into_iter().enumerate() {
            removed += frequency;
            if removed * 2 >= arr.len() as i32 {
                return count as i32 + 1;
            }
        }
        0
    }
}
