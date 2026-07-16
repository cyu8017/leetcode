// LeetCode 0532 - K-diff Pairs in an Array
// https://leetcode.com/problems/k-diff-pairs-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn find_pairs(nums: Vec<i32>, k: i32) -> i32 {
        if k < 0 {
            return 0;
        }

        let mut freq = HashMap::new();
        for num in nums {
            *freq.entry(num).or_insert(0) += 1;
        }

        let mut pairs = 0;
        for (&num, &count) in &freq {
            if k == 0 {
                if count > 1 {
                    pairs += 1;
                }
            } else if freq.contains_key(&(num + k)) {
                pairs += 1;
            }
        }
        pairs
    }
}
