// LeetCode 1695 - Maximum Erasure Value
// https://leetcode.com/problems/maximum-erasure-value/

use std::collections::HashMap;

impl Solution {
    pub fn maximum_unique_subarray(nums: Vec<i32>) -> i32 {
        let mut seen: HashMap<i32, usize> = HashMap::new();
        let mut left = 0usize;
        let mut cur = 0i32;
        let mut best = 0i32;
        for (right, &x) in nums.iter().enumerate() {
            if let Some(&prev) = seen.get(&x) {
                if prev >= left {
                    while left <= prev {
                        cur -= nums[left];
                        left += 1;
                    }
                }
            }
            seen.insert(x, right);
            cur += x;
            best = best.max(cur);
        }
        best
    }
}
