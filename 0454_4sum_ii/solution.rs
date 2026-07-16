// LeetCode 0454 - 4Sum II
// https://leetcode.com/problems/4sum-ii/

use std::collections::HashMap;

impl Solution {
    pub fn four_sum_count(nums1: Vec<i32>, nums2: Vec<i32>, nums3: Vec<i32>, nums4: Vec<i32>) -> i32 {
        let mut pair_sums: HashMap<i32, i32> = HashMap::new();
        for a in &nums1 {
            for b in &nums2 {
                *pair_sums.entry(a + b).or_insert(0) += 1;
            }
        }

        let mut total = 0;
        for c in &nums3 {
            for d in &nums4 {
                total += pair_sums.get(&(-(c + d))).copied().unwrap_or(0);
            }
        }
        total
    }
}
