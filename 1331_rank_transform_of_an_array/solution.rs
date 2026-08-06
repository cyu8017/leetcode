// LeetCode 1331 - Rank Transform of an Array
// https://leetcode.com/problems/rank-transform-of-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn array_rank_transform(arr: Vec<i32>) -> Vec<i32> {
        let mut sorted: Vec<i32> = arr.clone();
        sorted.sort_unstable();
        sorted.dedup();
        let rank: HashMap<i32, i32> = sorted
            .into_iter()
            .enumerate()
            .map(|(i, v)| (v, i as i32 + 1))
            .collect();
        arr.into_iter().map(|v| rank[&v]).collect()
    }
}
