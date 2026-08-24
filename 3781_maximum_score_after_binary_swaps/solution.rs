// LeetCode 3781 - Maximum Score After Binary Swaps
// https://leetcode.com/problems/maximum-score-after-binary-swaps/

use std::collections::BinaryHeap;

impl Solution {
    pub fn maximum_score(nums: Vec<i32>, s: String) -> i64 {
        let mut ans = 0i64;
        let mut pq = BinaryHeap::new();
        let bytes = s.as_bytes();
        for i in 0..nums.len() {
            pq.push(nums[i]);
            if bytes[i] == b'1' {
                ans += pq.pop().unwrap() as i64;
            }
        }
        ans
    }
}
