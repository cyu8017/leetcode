// LeetCode 0974 - Subarray Sums Divisible by K
// https://leetcode.com/problems/subarray-sums-divisible-by-k/

use std::collections::HashMap;

impl Solution {
    pub fn subarrays_div_by_k(nums: Vec<i32>, k: i32) -> i32 {
        let mut count = HashMap::new();
        count.insert(0, 1);
        let mut prefix = 0;
        let mut ans = 0;
        for x in nums {
            prefix = ((prefix + x) % k + k) % k;
            ans += count.get(&prefix).copied().unwrap_or(0);
            *count.entry(prefix).or_insert(0) += 1;
        }
        ans
    }
}
