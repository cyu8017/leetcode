// LeetCode 0232 - Implement Queue using Stacks
// https://leetcode.com/problems/implement-queue-using-stacks/

pub struct MyQueue {
    input_stack: Vec<i32>,
    output_stack: Vec<i32>,
}

impl MyQueue {
    pub fn new() -> Self {
        Self {
            input_stack: Vec::new(),
            output_stack: Vec::new(),
        }
    }

    fn move_values(&mut self) {
        if self.output_stack.is_empty() {
            while let Some(value) = self.input_stack.pop() {
                self.output_stack.push(value);
            }
        }
    }

    pub fn push(&mut self, x: i32) {
        self.input_stack.push(x);
    }

    pub fn pop(&mut self) -> i32 {
        self.move_values();
        self.output_stack.pop().unwrap()
    }

    pub fn peek(&mut self) -> i32 {
        self.move_values();
        *self.output_stack.last().unwrap()
    }

    pub fn empty(&self) -> bool {
        self.input_stack.is_empty() && self.output_stack.is_empty()
    }
}
