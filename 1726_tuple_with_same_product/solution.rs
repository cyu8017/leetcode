// LeetCode 1726 - Tuple with Same Product
// https://leetcode.com/problems/tuple-with-same-product/

use std::collections::HashMap;

impl Solution {
    pub fn tuple_same_product(nums: Vec<i32>) -> i32 {
        let mut counts: HashMap<i64, i64> = HashMap::new();
        for i in 0..nums.len() {
            for j in (i + 1)..nums.len() {
                *counts.entry(nums[i] as i64 * nums[j] as i64).or_insert(0) += 1;
            }
        }
        counts.values().map(|&count| count * (count - 1) * 4).sum::<i64>() as i32
    }
}
