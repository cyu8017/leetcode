// LeetCode 2364 - Count Number of Bad Pairs
// https://leetcode.com/problems/count-number-of-bad-pairs/

use std::collections::HashMap;

impl Solution {
    pub fn count_bad_pairs(nums: Vec<i32>) -> i64 {
        let n = nums.len() as i64;
        let total = n * (n - 1) / 2;
        let mut freq = HashMap::new();
        let mut good = 0i64;
        for (i, &x) in nums.iter().enumerate() {
            let key = x - i as i32;
            good += *freq.get(&key).unwrap_or(&0);
            *freq.entry(key).or_insert(0) += 1;
        }
        total - good
    }
}
