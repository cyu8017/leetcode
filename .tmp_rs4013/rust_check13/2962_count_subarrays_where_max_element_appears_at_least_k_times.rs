#![allow(dead_code, unused_variables, unused_mut, unused_assignments, unused_imports)]
struct Solution;
// LeetCode 2962 - Count Subarrays Where Max Element Appears at Least K Times
// https://leetcode.com/problems/count-subarrays-where-max-element-appears-at-least-k-times/

impl Solution {
    pub fn count_subarrays(nums: Vec<i32>, k: i32) -> i64 {
        let mx = *nums.iter().max().unwrap();
        let mut ans = 0i64;
        let mut cnt = 0;
        let mut left = 0;
        for right in 0..nums.len() {
            if nums[right] == mx {
                cnt += 1;
            }
            while cnt >= k {
                if nums[left] == mx {
                    cnt -= 1;
                }
                left += 1;
            }
            ans += left as i64;
        }
        ans
    }
}
