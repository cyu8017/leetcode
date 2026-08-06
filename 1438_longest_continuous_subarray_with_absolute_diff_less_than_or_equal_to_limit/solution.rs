// LeetCode 1438 - Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit
// https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

use std::collections::VecDeque;

impl Solution {
    pub fn longest_subarray(nums: Vec<i32>, limit: i32) -> i32 {
        let mut low = VecDeque::new();
        let mut high = VecDeque::new();
        let mut left = 0usize;
        let mut answer = 0;
        for (right, &value) in nums.iter().enumerate() {
            while low.back().map(|&i| nums[i] > value).unwrap_or(false) {
                low.pop_back();
            }
            while high.back().map(|&i| nums[i] < value).unwrap_or(false) {
                high.pop_back();
            }
            low.push_back(right);
            high.push_back(right);
            while nums[*high.front().unwrap()] - nums[*low.front().unwrap()] > limit {
                left += 1;
                if *low.front().unwrap() < left {
                    low.pop_front();
                }
                if *high.front().unwrap() < left {
                    high.pop_front();
                }
            }
            answer = answer.max(right - left + 1);
        }
        answer as i32
    }
}
