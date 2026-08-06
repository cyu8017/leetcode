// LeetCode 1115 - Print FooBar Alternately
// https://leetcode.com/problems/print-foobar-alternately/

use std::sync::{Condvar, Mutex};

struct FooBar {
    n: i32,
    state: Mutex<i32>,
    cv: Condvar,
}

impl FooBar {
    pub fn new(n: i32) -> Self {
        Self {
            n,
            state: Mutex::new(0),
            cv: Condvar::new(),
        }
    }

    pub fn foo(&self, print_foo: impl Fn()) {
        for _ in 0..self.n {
            let mut s = self.state.lock().unwrap();
            while *s != 0 {
                s = self.cv.wait(s).unwrap();
            }
            print_foo();
            *s = 1;
            self.cv.notify_all();
        }
    }

    pub fn bar(&self, print_bar: impl Fn()) {
        for _ in 0..self.n {
            let mut s = self.state.lock().unwrap();
            while *s != 1 {
                s = self.cv.wait(s).unwrap();
            }
            print_bar();
            *s = 0;
            self.cv.notify_all();
        }
    }
}
