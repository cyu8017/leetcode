// LeetCode 2588 - Count the Number of Beautiful Subarrays
// https://leetcode.com/problems/count-the-number-of-beautiful-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn beautiful_subarrays(nums: Vec<i32>) -> i64 {
        let mut freq = HashMap::from([(0, 1)]);
        let mut xorv = 0;
        let mut ans = 0i64;
        for x in nums {
            xorv ^= x;
            ans += *freq.get(&xorv).unwrap_or(&0);
            *freq.entry(xorv).or_insert(0) += 1;
        }
        ans
    }
}
