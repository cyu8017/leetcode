// LeetCode 0961 - N-Repeated Element in Size 2N Array
// https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

use std::collections::HashSet;

impl Solution {
    pub fn repeated_n_times(nums: Vec<i32>) -> i32 {
        let mut seen = HashSet::new();
        for x in nums {
            if !seen.insert(x) {
                return x;
            }
        }
        -1
    }
}
