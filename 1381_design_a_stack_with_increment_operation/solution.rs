// LeetCode 1381 - Design a Stack With Increment Operation
// https://leetcode.com/problems/design-a-stack-with-increment-operation/

struct CustomStack {
    max_size: usize,
    a: Vec<i32>,
}

impl CustomStack {
    fn new(max_size: i32) -> Self {
        Self {
            max_size: max_size as usize,
            a: Vec::new(),
        }
    }

    fn push(&mut self, x: i32) {
        if self.a.len() < self.max_size {
            self.a.push(x);
        }
    }

    fn pop(&mut self) -> i32 {
        self.a.pop().unwrap_or(-1)
    }

    fn increment(&mut self, k: i32, val: i32) {
        let lim = (k as usize).min(self.a.len());
        for i in 0..lim {
            self.a[i] += val;
        }
    }
}
