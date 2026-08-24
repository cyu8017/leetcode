// LeetCode 3852 - Smallest Pair With Different Frequencies
// https://leetcode.com/problems/smallest-pair-with-different-frequencies/

use std::collections::HashMap;

impl Solution {
    pub fn min_distinct_freq_pair(nums: Vec<i32>) -> Vec<i32> {
        let mut cnt = HashMap::new();
        for &v in &nums {
            *cnt.entry(v).or_insert(0) += 1;
        }
        let x = *nums.iter().min().unwrap();
        let mut min_y = i32::MAX;
        for (&y, _) in &cnt {
            if y < min_y && cnt[&x] != cnt[&y] {
                min_y = y;
            }
        }
        if min_y == i32::MAX {
            return vec![-1, -1];
        }
        vec![x, min_y]
    }
}
