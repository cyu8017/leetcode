// LeetCode 1962 - Remove Stones to Minimize the Total
// https://leetcode.com/problems/remove-stones-to-minimize-the-total/

use std::collections::BinaryHeap;

impl Solution {
    pub fn min_stone_sum(piles: Vec<i32>, k: i32) -> i32 {
        let mut heap: BinaryHeap<i32> = piles.into_iter().collect();
        for _ in 0..k {
            if let Some(x) = heap.pop() {
                heap.push(x - x / 2);
            }
        }
        heap.into_iter().sum()
    }
}
