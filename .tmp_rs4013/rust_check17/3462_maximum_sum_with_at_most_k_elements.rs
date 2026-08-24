struct Solution;
// LeetCode 3462 - Maximum Sum With at Most K Elements
// https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/

use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn max_sum(grid: Vec<Vec<i32>>, limits: Vec<i32>, k: i32) -> i64 {
        let mut h = BinaryHeap::new();
        let mut sum = 0i64;
        for i in 0..grid.len() {
            let mut r = grid[i].clone();
            r.sort_by(|a, b| b.cmp(a));
            let lim = limits[i].min(r.len() as i32) as usize;
            for j in 0..lim {
                h.push(Reverse(r[j]));
                sum += r[j] as i64;
                if h.len() > k as usize {
                    if let Some(Reverse(v)) = h.pop() {
                        sum -= v as i64;
                    }
                }
            }
        }
        sum
    }
}

fn main() {}
