// LeetCode 2336 - Smallest Number in Infinite Set
// https://leetcode.com/problems/smallest-number-in-infinite-set/

use std::collections::{BinaryHeap, HashSet};
use std::cmp::Reverse;

pub struct SmallestInfiniteSet {
    next: i32,
    added: HashSet<i32>,
    heap: BinaryHeap<Reverse<i32>>,
}

impl SmallestInfiniteSet {
    pub fn new() -> Self {
        Self {
            next: 1,
            added: HashSet::new(),
            heap: BinaryHeap::new(),
        }
    }

    pub fn pop_smallest(&mut self) -> i32 {
        if let Some(Reverse(x)) = self.heap.pop() {
            self.added.remove(&x);
            return x;
        }
        let x = self.next;
        self.next += 1;
        x
    }

    pub fn add_back(&mut self, num: i32) {
        if num < self.next && self.added.insert(num) {
            self.heap.push(Reverse(num));
        }
    }
}
