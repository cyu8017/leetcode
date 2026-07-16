// LeetCode 0239 - Sliding Window Maximum
// https://leetcode.com/problems/sliding-window-maximum/

use std::collections::VecDeque;

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let k = k as usize;
        let mut window = VecDeque::new();
        let mut result = Vec::with_capacity(nums.len().saturating_sub(k - 1));

        for (index, &num) in nums.iter().enumerate() {
            while let Some(&back) = window.back() {
                if nums[back] <= num {
                    window.pop_back();
                } else {
                    break;
                }
            }
            window.push_back(index);
            if window[0] <= index.saturating_sub(k) {
                window.pop_front();
            }
            if index >= k - 1 {
                result.push(nums[window[0]]);
            }
        }

        result
    }
}
