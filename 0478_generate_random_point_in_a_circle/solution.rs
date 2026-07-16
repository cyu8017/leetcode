// LeetCode 0478 - Generate Random Point in a Circle
// https://leetcode.com/problems/generate-random-point-in-a-circle/

use std::cell::RefCell;
use std::rc::Rc;

type UniformFn = Rc<dyn Fn(f64, f64) -> f64>;

thread_local! {
    static UNIFORM: RefCell<UniformFn> = RefCell::new(Rc::new(|low, high| {
        low + (high - low) * 0.5
    }));
}

pub fn set_uniform(uniform_fn: UniformFn) {
    UNIFORM.with(|uniform| *uniform.borrow_mut() = uniform_fn);
}

pub struct Solution {
    radius: f64,
    x_center: f64,
    y_center: f64,
}

impl Solution {
    pub fn new(radius: f64, x_center: f64, y_center: f64) -> Self {
        Self {
            radius,
            x_center,
            y_center,
        }
    }

    pub fn rand_point(&self) -> Vec<f64> {
        loop {
            let (x, y) = UNIFORM.with(|uniform| {
                let uniform = uniform.borrow();
                (
                    uniform(-self.radius, self.radius),
                    uniform(-self.radius, self.radius),
                )
            });
            if x * x + y * y <= self.radius * self.radius {
                return vec![
                    ((self.x_center + x) * 100000.0).round() / 100000.0,
                    ((self.y_center + y) * 100000.0).round() / 100000.0,
                ];
            }
        }
    }
}
