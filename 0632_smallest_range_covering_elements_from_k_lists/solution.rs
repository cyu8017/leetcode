// LeetCode 0632 - Smallest Range Covering Elements from K Lists
// https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn smallest_range(nums: Vec<Vec<i32>>) -> Vec<i32> {
        let mut heap: BinaryHeap<Reverse<(i32, usize, usize)>> = BinaryHeap::new();
        let mut current_max = i32::MIN;
        for (i, list) in nums.iter().enumerate() {
            heap.push(Reverse((list[0], i, 0)));
            current_max = current_max.max(list[0]);
        }
        let Reverse((first, _, _)) = *heap.peek().unwrap();
        let mut best_left = first;
        let mut best_right = current_max;
        loop {
            let Reverse((value, list_index, index)) = heap.pop().unwrap();
            if current_max - value < best_right - best_left {
                best_left = value;
                best_right = current_max;
            }
            if index + 1 == nums[list_index].len() {
                break;
            }
            let nxt = nums[list_index][index + 1];
            heap.push(Reverse((nxt, list_index, index + 1)));
            current_max = current_max.max(nxt);
        }
        vec![best_left, best_right]
    }
}
