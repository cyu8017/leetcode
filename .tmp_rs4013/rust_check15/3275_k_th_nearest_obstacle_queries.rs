struct Solution;
// LeetCode 3275 - K-th Nearest Obstacle Queries
// https://leetcode.com/problems/k-th-nearest-obstacle-queries/

use std::collections::BinaryHeap;

impl Solution {
    pub fn results_array(queries: Vec<Vec<i32>>, k: i32) -> Vec<i32> {
        let mut h = BinaryHeap::new();
        let mut ans = vec![0; queries.len()];
        for (i, q) in queries.iter().enumerate() {
            let d = q[0].abs() + q[1].abs();
            h.push(d);
            if h.len() as i32 > k {
                h.pop();
            }
            ans[i] = if (h.len() as i32) < k { -1 } else { *h.peek().unwrap() };
        }
        ans
    }
}

fn main() {}
