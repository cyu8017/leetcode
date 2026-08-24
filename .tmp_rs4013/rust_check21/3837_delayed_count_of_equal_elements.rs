struct Solution;
// LeetCode 3837 - Delayed Count of Equal Elements
// https://leetcode.com/problems/delayed-count-of-equal-elements/

use std::collections::HashMap;

impl Solution {
    pub fn delayed_count(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let n = nums.len();
        let k = k as usize;
        let mut cnt = HashMap::new();
        let mut ans = vec![0; n];
        if n >= k + 2 {
            for i in (0..=n - k - 2).rev() {
                *cnt.entry(nums[i + k + 1]).or_insert(0) += 1;
                ans[i] = *cnt.get(&nums[i]).unwrap_or(&0);
            }
        }
        ans
    }
}
