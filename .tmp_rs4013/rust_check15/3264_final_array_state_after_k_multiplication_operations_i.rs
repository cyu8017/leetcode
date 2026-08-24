struct Solution;
// LeetCode 3264 - Final Array State After K Multiplication Operations I
// https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn get_final_state(mut nums: Vec<i32>, k: i32, multiplier: i32) -> Vec<i32> {
        let mut h: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        for (i, &v) in nums.iter().enumerate() {
            h.push(Reverse((v, i)));
        }
        for _ in 0..k {
            if let Some(Reverse((v, i))) = h.pop() {
                let nv = v * multiplier;
                nums[i] = nv;
                h.push(Reverse((nv, i)));
            }
        }
        nums
    }
}

fn main() {}
