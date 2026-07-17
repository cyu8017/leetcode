// LeetCode 1742 - Maximum Number of Balls in a Box
// https://leetcode.com/problems/maximum-number-of-balls-in-a-box/

use std::collections::HashMap;

impl Solution {
    pub fn count_balls(low_limit: i32, high_limit: i32) -> i32 {
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for value in low_limit..=high_limit {
            let mut box_id = 0;
            let mut v = value;
            while v > 0 {
                box_id += v % 10;
                v /= 10;
            }
            *counts.entry(box_id).or_insert(0) += 1;
        }
        counts.values().copied().max().unwrap_or(0)
    }
}
