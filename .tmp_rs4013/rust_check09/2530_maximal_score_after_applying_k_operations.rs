struct Solution;

// LeetCode 2530 - Maximal Score After Applying K Operations
// https://leetcode.com/problems/maximal-score-after-applying-k-operations/

use std::collections::BinaryHeap;

impl Solution {
    pub fn max_kelements(nums: Vec<i32>, k: i32) -> i64 {
        let mut pq = BinaryHeap::from(nums);
        let mut ans = 0i64;
        for _ in 0..k {
            let x = pq.pop().unwrap();
            ans += x as i64;
            pq.push((x + 2) / 3);
        }
        ans
    }
}

fn main() {}
