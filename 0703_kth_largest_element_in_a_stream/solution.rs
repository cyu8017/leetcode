// LeetCode 0703 - Kth Largest Element in a Stream
// https://leetcode.com/problems/kth-largest-element-in-a-stream/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

pub struct KthLargest {
    k: usize,
    heap: BinaryHeap<Reverse<i32>>,
}

impl KthLargest {
    pub fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut obj = Self {
            k: k as usize,
            heap: BinaryHeap::new(),
        };
        for num in nums {
            obj.add(num);
        }
        obj
    }

    pub fn add(&mut self, val: i32) -> i32 {
        self.heap.push(Reverse(val));
        if self.heap.len() > self.k {
            self.heap.pop();
        }
        self.heap.peek().unwrap().0
    }
}
