// LeetCode 1713 - Minimum Operations to Make a Subsequence
// https://leetcode.com/problems/minimum-operations-to-make-a-subsequence/

use std::collections::HashMap;

impl Solution {
    pub fn min_operations(target: Vec<i32>, arr: Vec<i32>) -> i32 {
        let pos: HashMap<i32, usize> = target
            .iter()
            .enumerate()
            .map(|(i, &value)| (value, i))
            .collect();
        let mut lis: Vec<usize> = Vec::new();
        for value in arr {
            if let Some(&idx) = pos.get(&value) {
                let place = lis.partition_point(|&x| x < idx);
                if place == lis.len() {
                    lis.push(idx);
                } else {
                    lis[place] = idx;
                }
            }
        }
        (target.len() - lis.len()) as i32
    }
}
