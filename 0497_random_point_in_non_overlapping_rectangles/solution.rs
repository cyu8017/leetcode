// LeetCode 0497 - Random Point in Non-overlapping Rectangles
// https://leetcode.com/problems/random-point-in-non-overlapping-rectangles/

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
    rects: Vec<Vec<i32>>,
    prefix: Vec<i32>,
    total: i32,
}

impl Solution {
    pub fn new(rects: Vec<Vec<i32>>) -> Self {
        let mut prefix = Vec::new();
        let mut total = 0;
        for rect in &rects {
            total += (rect[2] - rect[0] + 1) * (rect[3] - rect[1] + 1);
            prefix.push(total);
        }
        Self { rects, prefix, total }
    }

    pub fn pick(&self) -> Vec<i32> {
        let mut index = UNIFORM.with(|uniform| uniform.borrow()(0.0, self.total as f64)) as i32;
        if index >= self.total {
            index = self.total - 1;
        }

        let mut lo = 0usize;
        let mut hi = self.prefix.len() - 1;
        while lo < hi {
            let mid = lo + (hi - lo) / 2;
            if index < self.prefix[mid] {
                hi = mid;
            } else {
                lo = mid + 1;
            }
        }
        if lo > 0 {
            index -= self.prefix[lo - 1];
        }

        let rect = &self.rects[lo];
        let width = rect[2] - rect[0] + 1;
        vec![rect[0] + index % width, rect[1] + index / width]
    }
}
