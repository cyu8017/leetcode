// LeetCode 2006 - Count Number of Pairs With Absolute Difference K
// https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

use std::collections::HashMap;

impl Solution {
    pub fn count_k_difference(nums: Vec<i32>, k: i32) -> i32 {
        let mut freq = HashMap::new();
        let mut ans = 0;
        for x in nums {
            ans += freq.get(&(x - k)).unwrap_or(&0) + freq.get(&(x + k)).unwrap_or(&0);
            *freq.entry(x).or_insert(0) += 1;
        }
        ans
    }
}
