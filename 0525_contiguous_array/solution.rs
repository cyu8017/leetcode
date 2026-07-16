// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

use std::collections::HashMap;

impl Solution {
    pub fn find_max_length(nums: Vec<i32>) -> i32 {
        let mut counts = HashMap::from([(0, -1)]);
        let mut balance = 0;
        let mut best = 0;

        for (index, num) in nums.iter().enumerate() {
            balance += if *num == 1 { 1 } else { -1 };
            if let Some(&prev) = counts.get(&balance) {
                best = best.max((index as i32) - prev);
            } else {
                counts.insert(balance, index as i32);
            }
        }
        best
    }
}
