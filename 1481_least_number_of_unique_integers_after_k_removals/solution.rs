// LeetCode 1481 - Least Number of Unique Integers after K Removals
// https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

use std::collections::HashMap;

impl Solution {
    pub fn find_least_num_of_unique_ints(arr: Vec<i32>, mut k: i32) -> i32 {
        let mut counts = HashMap::new();
        for x in arr {
            *counts.entry(x).or_insert(0) += 1;
        }
        let mut freqs: Vec<i32> = counts.into_values().collect();
        freqs.sort_unstable();
        let mut removed = 0;
        for count in &freqs {
            if k < *count {
                break;
            }
            k -= count;
            removed += 1;
        }
        freqs.len() as i32 - removed
    }
}
