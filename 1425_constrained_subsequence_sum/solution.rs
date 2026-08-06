// LeetCode 1425 - Constrained Subsequence Sum
// https://leetcode.com/problems/constrained-subsequence-sum/

use std::collections::VecDeque;

impl Solution {
    pub fn constrained_subset_sum(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut best = nums.clone();
        let mut queue = VecDeque::new();
        for i in 0..nums.len() {
            while queue.front().map(|&j| j + k < i).unwrap_or(false) {
                queue.pop_front();
            }
            best[i] = nums[i] + queue.front().map(|&j| best[j].max(0)).unwrap_or(0);
            while queue.back().map(|&j| best[j] <= best[i]).unwrap_or(false) {
                queue.pop_back();
            }
            queue.push_back(i);
        }
        *best.iter().max().unwrap()
    }
}
