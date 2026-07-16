// LeetCode 0225 - Implement Stack using Queues
// https://leetcode.com/problems/implement-stack-using-queues/

use std::collections::VecDeque;

pub struct MyStack {
    queue: VecDeque<i32>,
}

impl MyStack {
    pub fn new() -> Self {
        Self {
            queue: VecDeque::new(),
        }
    }

    pub fn push(&mut self, x: i32) {
        self.queue.push_back(x);
        for _ in 0..self.queue.len() - 1 {
            let front = self.queue.pop_front().unwrap();
            self.queue.push_back(front);
        }
    }

    pub fn pop(&mut self) -> i32 {
        self.queue.pop_front().unwrap()
    }

    pub fn top(&self) -> i32 {
        *self.queue.front().unwrap()
    }

    pub fn empty(&self) -> bool {
        self.queue.is_empty()
    }
}
