// LeetCode 0716 - Max Stack
// https://leetcode.com/problems/max-stack/

pub struct MaxStack {
    stack: Vec<i32>,
    maxes: Vec<i32>,
}

impl MaxStack {
    pub fn new() -> Self {
        Self {
            stack: Vec::new(),
            maxes: Vec::new(),
        }
    }

    pub fn push(&mut self, x: i32) {
        self.stack.push(x);
        let max_val = self.maxes.last().copied().unwrap_or(x).max(x);
        self.maxes.push(max_val);
    }

    pub fn pop(&mut self) -> i32 {
        self.maxes.pop();
        self.stack.pop().unwrap()
    }

    pub fn top(&self) -> i32 {
        *self.stack.last().unwrap()
    }

    pub fn peek_max(&self) -> i32 {
        *self.maxes.last().unwrap()
    }

    pub fn pop_max(&mut self) -> i32 {
        let max_val = self.peek_max();
        let mut buffer = Vec::new();
        while self.top() != max_val {
            buffer.push(self.pop());
        }
        self.pop();
        while let Some(val) = buffer.pop() {
            self.push(val);
        }
        max_val
    }
}
