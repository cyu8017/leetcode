// LeetCode 2386 - Find the K-Sum of an Array
// https://leetcode.com/problems/find-the-k-sum-of-an-array/

use std::collections::BinaryHeap;

impl Solution {
    pub fn k_sum(nums: Vec<i32>, k: i32) -> i64 {
        let mut total = 0i64;
        let mut abs_nums: Vec<i32> = nums
            .iter()
            .map(|&x| {
                if x >= 0 {
                    total += x as i64;
                    x
                } else {
                    -x
                }
            })
            .collect();
        abs_nums.sort_unstable();
        let mut h = BinaryHeap::new();
        h.push((total, 0usize));
        for _ in 0..k - 1 {
            let Some((sum, i)) = h.pop() else { break };
            if i >= abs_nums.len() {
                continue;
            }
            h.push((sum - abs_nums[i] as i64, i + 1));
            if i > 0 {
                h.push((sum - abs_nums[i] as i64 + abs_nums[i - 1] as i64, i + 1));
            }
        }
        h.peek().map(|&(s, _)| s).unwrap_or(0)
    }
}
