// LeetCode 0528 - Random Pick with Weight
// https://leetcode.com/problems/random-pick-with-weight/

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
    prefix: Vec<i32>,
    total: i32,
}

impl Solution {
    pub fn new(w: Vec<i32>) -> Self {
        let mut prefix = Vec::with_capacity(w.len());
        let mut total = 0;
        for weight in w {
            total += weight;
            prefix.push(total);
        }
        Self { prefix, total }
    }

    pub fn pick_index(&mut self) -> i32 {
        let mut target = UNIFORM.with(|uniform| uniform.borrow()(0.0, self.total as f64)) as i32;
        if target >= self.total {
            target = self.total - 1;
        }
        Self::bisect_right(&self.prefix, target)
    }

    fn bisect_right(values: &[i32], target: i32) -> i32 {
        let mut low = 0;
        let mut high = values.len() as i32 - 1;
        while low < high {
            let mid = low + (high - low) / 2;
            if values[mid as usize] <= target {
                low = mid + 1;
            } else {
                high = mid;
            }
        }
        low
    }
}
