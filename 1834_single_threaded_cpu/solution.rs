// LeetCode 1834 - Single-Threaded CPU
// https://leetcode.com/problems/single-threaded-cpu/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

impl Solution {
    pub fn get_order(tasks: Vec<Vec<i32>>) -> Vec<i32> {
        let n = tasks.len();
        let mut indexed: Vec<(usize, i32, i32)> = tasks
            .iter()
            .enumerate()
            .map(|(i, t)| (i, t[0], t[1]))
            .collect();
        indexed.sort_by_key(|&(i, enqueue, _)| (enqueue, i));

        let mut i = 0;
        let mut heap: BinaryHeap<Reverse<(i32, usize)>> = BinaryHeap::new();
        let mut time: i64 = 0;
        let mut order = Vec::with_capacity(n);

        while i < n || !heap.is_empty() {
            if i < n && heap.is_empty() {
                time = time.max(indexed[i].1 as i64);
            }

            while i < n && indexed[i].1 as i64 <= time {
                let (idx, _, processing) = indexed[i];
                heap.push(Reverse((processing, idx)));
                i += 1;
            }

            if let Some(Reverse((duration, idx))) = heap.pop() {
                time += duration as i64;
                order.push(idx as i32);
            }
        }

        order
    }
}
