// LeetCode 0857 - Minimum Cost to Hire K Workers
// https://leetcode.com/problems/minimum-cost-to-hire-k-workers/

use std::collections::BinaryHeap;

impl Solution {
    pub fn mincost_to_hire_workers(quality: Vec<i32>, wage: Vec<i32>, k: i32) -> f64 {
        let n = quality.len();
        let mut workers: Vec<(f64, i32)> = (0..n)
            .map(|i| (wage[i] as f64 / quality[i] as f64, quality[i]))
            .collect();
        workers.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
        let mut heap = BinaryHeap::new();
        let mut total_q = 0i64;
        let mut ans = 1e18;
        for (ratio, q) in workers {
            heap.push(q);
            total_q += q as i64;
            if heap.len() as i32 > k {
                total_q -= heap.pop().unwrap() as i64;
            }
            if heap.len() as i32 == k {
                ans = ans.min(total_q as f64 * ratio);
            }
        }
        ans
    }
}
