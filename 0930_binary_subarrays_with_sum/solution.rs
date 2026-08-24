// LeetCode 0930 - Binary Subarrays With Sum
// https://leetcode.com/problems/binary-subarrays-with-sum/

use std::collections::HashMap;

impl Solution {
    pub fn num_subarrays_with_sum(nums: Vec<i32>, goal: i32) -> i32 {
        let mut count = HashMap::new();
        count.insert(0, 1);
        let mut prefix = 0;
        let mut ans = 0;
        for x in nums {
            prefix += x;
            ans += count.get(&(prefix - goal)).copied().unwrap_or(0);
            *count.entry(prefix).or_insert(0) += 1;
        }
        ans
    }
}
