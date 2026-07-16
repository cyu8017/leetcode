// LeetCode 0295 - Find Median from Data Stream
// https://leetcode.com/problems/find-median-from-data-stream/

use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct MedianFinder {
    small: BinaryHeap<i32>,
    large: BinaryHeap<Reverse<i32>>,
}

impl MedianFinder {
    fn new() -> Self {
        Self {
            small: BinaryHeap::new(),
            large: BinaryHeap::new(),
        }
    }

    fn add_num(&mut self, num: i32) {
        self.small.push(num);
        if let Some(value) = self.small.pop() {
            self.large.push(Reverse(value));
        }
        if self.large.len() > self.small.len() {
            if let Some(Reverse(value)) = self.large.pop() {
                self.small.push(value);
            }
        }
    }

    fn find_median(&self) -> f64 {
        if self.small.len() > self.large.len() {
            return *self.small.peek().unwrap() as f64;
        }
        let left = *self.small.peek().unwrap() as f64;
        let right = self.large.peek().unwrap().0 as f64;
        (left + right) / 2.0
    }
}
