// LeetCode 2762 - Continuous Subarrays
// https://leetcode.com/problems/continuous-subarrays/

use std::collections::BTreeMap;

impl Solution {
    pub fn continuous_subarrays(nums: Vec<i32>) -> i64 {
        let mut ans = 0i64;
        let mut left = 0;
        let mut freq: BTreeMap<i32, i32> = BTreeMap::new();
        for right in 0..nums.len() {
            *freq.entry(nums[right]).or_insert(0) += 1;
            while freq.keys().next_back().unwrap() - freq.keys().next().unwrap() > 2 {
                let e = freq.get_mut(&nums[left]).unwrap();
                *e -= 1;
                if *e == 0 {
                    freq.remove(&nums[left]);
                }
                left += 1;
            }
            ans += (right - left + 1) as i64;
        }
        ans
    }
}
