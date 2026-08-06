// LeetCode 1114 - Print in Order
// https://leetcode.com/problems/print-in-order/

use std::sync::{Condvar, Mutex};

struct Foo {
    state: Mutex<i32>,
    cv: Condvar,
}

impl Foo {
    pub fn new() -> Self {
        Self {
            state: Mutex::new(0),
            cv: Condvar::new(),
        }
    }

    pub fn first(&self, print_first: impl FnOnce()) {
        print_first();
        let mut s = self.state.lock().unwrap();
        *s = 1;
        self.cv.notify_all();
    }

    pub fn second(&self, print_second: impl FnOnce()) {
        let mut s = self.state.lock().unwrap();
        while *s < 1 {
            s = self.cv.wait(s).unwrap();
        }
        print_second();
        *s = 2;
        self.cv.notify_all();
    }

    pub fn third(&self, print_third: impl FnOnce()) {
        let mut s = self.state.lock().unwrap();
        while *s < 2 {
            s = self.cv.wait(s).unwrap();
        }
        print_third();
    }
}
