// LeetCode 2870 - Minimum Number of Operations to Make Array Empty
// https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

use std::collections::HashMap;

impl Solution {
    pub fn min_operations(nums: Vec<i32>) -> i32 {
        let mut freq: HashMap<i32, i32> = HashMap::new();
        for v in nums {
            *freq.entry(v).or_insert(0) += 1;
        }
        let mut ans = 0;
        for c in freq.values() {
            if *c == 1 {
                return -1;
            }
            ans += (*c + 2) / 3;
        }
        ans
    }
}
