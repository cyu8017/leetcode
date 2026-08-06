// LeetCode 1187 - Make Array Strictly Increasing
// https://leetcode.com/problems/make-array-strictly-increasing/

use std::collections::{HashMap, HashSet};

impl Solution {
    pub fn make_array_increasing(arr1: Vec<i32>, arr2: Vec<i32>) -> i32 {
        let mut uniq: Vec<i32> = arr2.into_iter().collect::<HashSet<_>>().into_iter().collect();
        uniq.sort_unstable();
        let mut dp: HashMap<i32, i32> = HashMap::new();
        dp.insert(-1, 0);
        for num in arr1 {
            let mut new_dp = HashMap::new();
            for (&prev, &ops) in &dp {
                if num > prev {
                    let e = new_dp.entry(num).or_insert(i32::MAX);
                    *e = (*e).min(ops);
                }
                let idx = uniq.partition_point(|&x| x <= prev);
                if idx < uniq.len() {
                    let chosen = uniq[idx];
                    let e = new_dp.entry(chosen).or_insert(i32::MAX);
                    *e = (*e).min(ops + 1);
                }
            }
            dp = new_dp;
            if dp.is_empty() {
                return -1;
            }
        }
        *dp.values().min().unwrap()
    }
}
