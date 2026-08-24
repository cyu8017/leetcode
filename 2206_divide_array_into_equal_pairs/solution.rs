// LeetCode 2206 - Divide Array Into Equal Pairs
// https://leetcode.com/problems/divide-array-into-equal-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut freq = HashMap::new();
        for x in nums {
            *freq.entry(x).or_insert(0) += 1;
        }
        freq.values().all(|&c| c % 2 == 0)
    }
}
