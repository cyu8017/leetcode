// LeetCode 1172 - Dinner Plate Stacks
// https://leetcode.com/problems/dinner-plate-stacks/

use std::collections::{BinaryHeap, HashSet};
use std::cmp::Reverse;

struct DinnerPlates {
    capacity: usize,
    stacks: Vec<Vec<i32>>,
    avail: BinaryHeap<Reverse<usize>>,
    in_avail: HashSet<usize>,
}

impl DinnerPlates {
    fn new(capacity: i32) -> Self {
        Self {
            capacity: capacity as usize,
            stacks: Vec::new(),
            avail: BinaryHeap::new(),
            in_avail: HashSet::new(),
        }
    }

    fn push(&mut self, val: i32) {
        while let Some(&Reverse(idx)) = self.avail.peek() {
            if idx < self.stacks.len() && self.stacks[idx].len() < self.capacity {
                break;
            }
            self.avail.pop();
            self.in_avail.remove(&idx);
        }
        if self.avail.is_empty() {
            self.stacks.push(Vec::new());
            let idx = self.stacks.len() - 1;
            self.avail.push(Reverse(idx));
            self.in_avail.insert(idx);
        }
        let idx = self.avail.peek().unwrap().0;
        self.stacks[idx].push(val);
        if self.stacks[idx].len() == self.capacity {
            self.avail.pop();
            self.in_avail.remove(&idx);
        }
    }

    fn pop(&mut self) -> i32 {
        self.pop_at_stack(self.stacks.len() as i32 - 1)
    }

    fn pop_at_stack(&mut self, index: i32) -> i32 {
        let index = index as usize;
        if index >= self.stacks.len() || self.stacks[index].is_empty() {
            return -1;
        }
        let val = self.stacks[index].pop().unwrap();
        if !self.in_avail.contains(&index) {
            self.avail.push(Reverse(index));
            self.in_avail.insert(index);
        }
        while !self.stacks.is_empty() && self.stacks.last().unwrap().is_empty() {
            let last = self.stacks.len() - 1;
            self.stacks.pop();
            self.in_avail.remove(&last);
        }
        val
    }
}
