// LeetCode 1687 - Delivering Boxes from Storage to Ports
// https://leetcode.com/problems/delivering-boxes-from-storage-to-ports/

use std::collections::VecDeque;

impl Solution {
    pub fn box_delivering(
        boxes: Vec<Vec<i32>>,
        _ports_count: i32,
        max_boxes: i32,
        max_weight: i32,
    ) -> i32 {
        let n = boxes.len();
        let mut w = vec![0i32; n + 1];
        let mut changes = vec![0i32; n + 1];
        for i in 1..=n {
            w[i] = w[i - 1] + boxes[i - 1][1];
            changes[i] = changes[i - 1];
            if i > 1 && boxes[i - 1][0] != boxes[i - 2][0] {
                changes[i] += 1;
            }
        }
        let mut dp = vec![0i32; n + 1];
        let mut q = VecDeque::from([0usize]);
        for i in 1..=n {
            while !q.is_empty()
                && (i - q[0] > max_boxes as usize || w[i] - w[q[0]] > max_weight)
            {
                q.pop_front();
            }
            let j = q[0];
            dp[i] = dp[j] + changes[i] - changes[j + 1] + 2;
            if i < n {
                let val = dp[i] - changes[i + 1];
                while !q.is_empty()
                    && dp[*q.back().unwrap()] - changes[*q.back().unwrap() + 1] >= val
                {
                    q.pop_back();
                }
                q.push_back(i);
            }
        }
        dp[n]
    }
}
