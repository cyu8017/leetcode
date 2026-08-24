// LeetCode 2349 - Design a Number Container System
// https://leetcode.com/problems/design-a-number-container-system/

use std::collections::{BinaryHeap, HashMap};
use std::cmp::Reverse;

pub struct NumberContainers {
    idx: HashMap<i32, i32>,
    heap: HashMap<i32, BinaryHeap<Reverse<i32>>>,
}

impl NumberContainers {
    pub fn new() -> Self {
        Self {
            idx: HashMap::new(),
            heap: HashMap::new(),
        }
    }

    pub fn change(&mut self, index: i32, number: i32) {
        self.idx.insert(index, number);
        self.heap.entry(number).or_default().push(Reverse(index));
    }

    pub fn find(&mut self, number: i32) -> i32 {
        if let Some(h) = self.heap.get_mut(&number) {
            while let Some(&Reverse(i)) = h.peek() {
                if self.idx.get(&i) == Some(&number) {
                    return i;
                }
                h.pop();
            }
        }
        -1
    }
}
