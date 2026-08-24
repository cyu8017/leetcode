// LeetCode 2537 - Count the Number of Good Subarrays
// https://leetcode.com/problems/count-the-number-of-good-subarrays/

use std::collections::HashMap;

impl Solution {
    pub fn count_good(nums: Vec<i32>, k: i32) -> i64 {
        let mut freq = HashMap::new();
        let mut pairs = 0i64;
        let mut ans = 0i64;
        let mut left = 0;
        let n = nums.len();
        for right in 0..n {
            pairs += *freq.get(&nums[right]).unwrap_or(&0);
            *freq.entry(nums[right]).or_insert(0) += 1;
            while pairs >= k as i64 {
                ans += (n - right) as i64;
                *freq.get_mut(&nums[left]).unwrap() -= 1;
                pairs -= freq[&nums[left]];
                left += 1;
            }
        }
        ans
    }
}
