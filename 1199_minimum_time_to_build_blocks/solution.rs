// LeetCode 1199 - Minimum Time to Build Blocks
// https://leetcode.com/problems/minimum-time-to-build-blocks/

use std::collections::BinaryHeap;
use std::cmp::Reverse;

impl Solution {
    pub fn min_build_time(blocks: Vec<i32>, split: i32) -> i32 {
        let mut heap: BinaryHeap<Reverse<i32>> = blocks.into_iter().map(Reverse).collect();
        while heap.len() > 1 {
            heap.pop();
            let b = heap.pop().unwrap().0;
            heap.push(Reverse(b + split));
        }
        heap.pop().unwrap().0
    }
}
