// LeetCode 1636 - Sort Array by Increasing Frequency
// https://leetcode.com/problems/sort-array-by-increasing-frequency/

use std::collections::HashMap;

impl Solution {
    pub fn frequency_sort(mut nums: Vec<i32>) -> Vec<i32> {
        let mut count = HashMap::new();
        for &x in &nums {
            *count.entry(x).or_insert(0) += 1;
        }
        nums.sort_by(|a, b| {
            let ca = count[a];
            let cb = count[b];
            ca.cmp(&cb).then(b.cmp(a))
        });
        nums
    }
}
