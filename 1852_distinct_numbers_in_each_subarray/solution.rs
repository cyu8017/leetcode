// LeetCode 1852 - Distinct Numbers in Each Subarray
// https://leetcode.com/problems/distinct-numbers-in-each-subarray/

use std::collections::HashMap;

impl Solution {
    pub fn distinct_numbers(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for &num in &nums[..k] {
            *counts.entry(num).or_insert(0) += 1;
        }
        let mut result = vec![counts.len() as i32];
        let mut left = 0usize;
        for right in k..nums.len() {
            *counts.entry(nums[right]).or_insert(0) += 1;
            let outgoing = nums[left];
            if let Some(c) = counts.get_mut(&outgoing) {
                *c -= 1;
                if *c == 0 {
                    counts.remove(&outgoing);
                }
            }
            left += 1;
            result.push(counts.len() as i32);
        }
        result
    }
}
