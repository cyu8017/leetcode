// LeetCode 0560 - Subarray Sum Equals K
// https://leetcode.com/problems/subarray-sum-equals-k/

use std::collections::HashMap;

impl Solution {
    pub fn subarray_sum(nums: Vec<i32>, k: i32) -> i32 {
        let mut counts = HashMap::new();
        counts.insert(0, 1);
        let mut prefix = 0;
        let mut answer = 0;
        for num in nums {
            prefix += num;
            if let Some(&count) = counts.get(&(prefix - k)) {
                answer += count;
            }
            *counts.entry(prefix).or_insert(0) += 1;
        }
        answer
    }
}
