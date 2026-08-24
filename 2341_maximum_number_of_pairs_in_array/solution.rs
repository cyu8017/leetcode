// LeetCode 2341 - Maximum Number of Pairs in Array
// https://leetcode.com/problems/maximum-number-of-pairs-in-array/

use std::collections::HashMap;

impl Solution {
    pub fn number_of_pairs(nums: Vec<i32>) -> Vec<i32> {
        let mut cnt = HashMap::new();
        for x in nums {
            *cnt.entry(x).or_insert(0) += 1;
        }
        let mut pairs = 0;
        let mut left = 0;
        for c in cnt.values() {
            pairs += c / 2;
            left += c % 2;
        }
        vec![pairs, left]
    }
}
