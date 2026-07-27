// LeetCode 1696 - Jump Game VI
// https://leetcode.com/problems/jump-game-vi/

use std::collections::VecDeque;

impl Solution {
    pub fn max_result(nums: Vec<i32>, k: i32) -> i32 {
        let k = k as usize;
        let mut q = VecDeque::from([(0usize, nums[0])]);
        for i in 1..nums.len() {
            while q.front().unwrap().0 + k < i {
                q.pop_front();
            }
            let score = nums[i] + q.front().unwrap().1;
            while !q.is_empty() && q.back().unwrap().1 <= score {
                q.pop_back();
            }
            q.push_back((i, score));
        }
        q.back().unwrap().1
    }
}
