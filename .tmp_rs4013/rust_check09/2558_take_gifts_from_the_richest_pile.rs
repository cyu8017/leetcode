struct Solution;

// LeetCode 2558 - Take Gifts From the Richest Pile
// https://leetcode.com/problems/take-gifts-from-the-richest-pile/

use std::collections::BinaryHeap;

impl Solution {
    pub fn pick_gifts(gifts: Vec<i32>, k: i32) -> i64 {
        let mut h = BinaryHeap::from(gifts);
        for _ in 0..k {
            let x = h.pop().unwrap();
            h.push((x as f64).sqrt() as i32);
        }
        h.into_iter().map(|x| x as i64).sum()
    }
}

fn main() {}
