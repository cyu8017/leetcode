// LeetCode 2190 - Most Frequent Number Following Key In an Array
// https://leetcode.com/problems/most-frequent-number-following-key-in-an-array/

use std::collections::HashMap;

impl Solution {
    pub fn most_frequent(nums: Vec<i32>, key: i32) -> i32 {
        let mut freq = HashMap::new();
        let mut best = 0;
        let mut ans = 0;
        for i in 0..nums.len().saturating_sub(1) {
            if nums[i] == key {
                let e = freq.entry(nums[i + 1]).or_insert(0);
                *e += 1;
                if *e > best {
                    best = *e;
                    ans = nums[i + 1];
                }
            }
        }
        ans
    }
}
