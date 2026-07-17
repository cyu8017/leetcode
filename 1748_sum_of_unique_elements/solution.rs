// LeetCode 1748 - Sum of Unique Elements
// https://leetcode.com/problems/sum-of-unique-elements/

use std::collections::HashMap;

impl Solution {
    pub fn sum_of_unique(nums: Vec<i32>) -> i32 {
        let mut counts: HashMap<i32, i32> = HashMap::new();
        for &value in &nums {
            *counts.entry(value).or_insert(0) += 1;
        }
        counts
            .iter()
            .filter(|&(_, &count)| count == 1)
            .map(|(&value, _)| value)
            .sum()
    }
}
