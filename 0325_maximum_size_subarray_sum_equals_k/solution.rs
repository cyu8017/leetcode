// LeetCode 0325 - Maximum Size Subarray Sum Equals k
// https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/

use std::collections::HashMap;

impl Solution {
    pub fn max_sub_array_len(nums: Vec<i32>, k: i32) -> i32 {
        let mut prefix_index = HashMap::new();
        prefix_index.insert(0, -1);
        let mut prefix = 0;
        let mut best = 0;
        for (index, num) in nums.iter().enumerate() {
            prefix += num;
            if let Some(&start_index) = prefix_index.get(&(prefix - k)) {
                best = best.max(index as i32 - start_index);
            }
            prefix_index.entry(prefix).or_insert(index as i32);
        }
        best
    }
}
