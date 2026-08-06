// LeetCode 1116 - Print Zero Even Odd
// https://leetcode.com/problems/print-zero-even-odd/

use std::sync::{Condvar, Mutex};

struct ZeroEvenOdd {
    n: i32,
    state: Mutex<i32>,
    cv: Condvar,
}

impl ZeroEvenOdd {
    pub fn new(n: i32) -> Self {
        Self {
            n,
            state: Mutex::new(0),
            cv: Condvar::new(),
        }
    }

    pub fn zero(&self, print_number: impl Fn(i32)) {
        for i in 0..self.n {
            let mut s = self.state.lock().unwrap();
            while *s != 0 {
                s = self.cv.wait(s).unwrap();
            }
            print_number(0);
            *s = if i % 2 == 0 { 1 } else { 2 };
            self.cv.notify_all();
        }
    }

    pub fn even(&self, print_number: impl Fn(i32)) {
        let mut num = 2;
        while num <= self.n {
            let mut s = self.state.lock().unwrap();
            while *s != 2 {
                s = self.cv.wait(s).unwrap();
            }
            print_number(num);
            *s = 0;
            self.cv.notify_all();
            num += 2;
        }
    }

    pub fn odd(&self, print_number: impl Fn(i32)) {
        let mut num = 1;
        while num <= self.n {
            let mut s = self.state.lock().unwrap();
            while *s != 1 {
                s = self.cv.wait(s).unwrap();
            }
            print_number(num);
            *s = 0;
            self.cv.notify_all();
            num += 2;
        }
    }
}
