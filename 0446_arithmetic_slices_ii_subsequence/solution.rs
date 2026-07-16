// LeetCode 0446 - Arithmetic Slices II - Subsequence
// https://leetcode.com/problems/arithmetic-slices-ii-subsequence/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_arithmetic_slices(nums: Vec<i32>) -> i32 {
        let mut total = 0;
        let mut differences: Vec<HashMap<i64, i32>> = vec![HashMap::new(); nums.len()];

        for (index, &value) in nums.iter().enumerate() {
            for previous in 0..index {
                let diff = i64::from(value) - i64::from(nums[previous]);
                total += *differences[previous].get(&diff).unwrap_or(&0);
                let entry = differences[index].entry(diff).or_insert(0);
                *entry += differences[previous].get(&diff).unwrap_or(&0) + 1;
            }
        }
        total
    }
}
