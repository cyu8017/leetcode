// LeetCode 0519 - Random Flip Matrix
// https://leetcode.com/problems/random-flip-matrix/

use std::cell::RefCell;
use std::rc::Rc;

type UniformFn = Rc<dyn Fn(f64, f64) -> f64>;

thread_local! {
    static UNIFORM: RefCell<UniformFn> = RefCell::new(Rc::new(|low, _| low));
}

pub fn set_uniform(uniform_fn: UniformFn) {
    UNIFORM.with(|uniform| *uniform.borrow_mut() = uniform_fn);
}

pub struct Solution {
    cols: i32,
    total: i32,
    available: Vec<i32>,
}

impl Solution {
    pub fn new(m: i32, n: i32) -> Self {
        let total = m * n;
        let mut available = Vec::with_capacity(total as usize);
        for index in 0..total {
            available.push(index);
        }
        Self { cols: n, total, available }
    }

    pub fn flip(&mut self) -> Vec<i32> {
        let mut index =
            UNIFORM.with(|uniform| uniform.borrow()(0.0, (self.available.len() - 1) as f64)) as i32;
        if index >= self.available.len() as i32 {
            index = self.available.len() as i32 - 1;
        }
        let value = self.available[index as usize];
        let last = self.available.len() - 1;
        self.available[index as usize] = self.available[last];
        self.available.pop();
        vec![value / self.cols, value % self.cols]
    }

    pub fn reset(&mut self) {
        self.available.clear();
        for index in 0..self.total {
            self.available.push(index);
        }
    }
}
