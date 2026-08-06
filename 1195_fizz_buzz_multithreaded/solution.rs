// LeetCode 1195 - Fizz Buzz Multithreaded
// https://leetcode.com/problems/fizz-buzz-multithreaded/

use std::sync::{Condvar, Mutex};

struct FizzBuzz {
    n: i32,
    state: Mutex<i32>,
    cv: Condvar,
}

impl FizzBuzz {
    pub fn new(n: i32) -> Self {
        Self {
            n,
            state: Mutex::new(1),
            cv: Condvar::new(),
        }
    }

    fn run(&self, pred: impl Fn(i32) -> bool, action: impl Fn(i32)) {
        loop {
            let mut cur = self.state.lock().unwrap();
            while *cur <= self.n && !pred(*cur) {
                cur = self.cv.wait(cur).unwrap();
            }
            if *cur > self.n {
                return;
            }
            action(*cur);
            *cur += 1;
            self.cv.notify_all();
        }
    }

    pub fn fizz(&self, print_fizz: impl Fn()) {
        self.run(|x| x % 3 == 0 && x % 5 != 0, |_| print_fizz());
    }

    pub fn buzz(&self, print_buzz: impl Fn()) {
        self.run(|x| x % 5 == 0 && x % 3 != 0, |_| print_buzz());
    }

    pub fn fizzbuzz(&self, print_fizz_buzz: impl Fn()) {
        self.run(|x| x % 15 == 0, |_| print_fizz_buzz());
    }

    pub fn number(&self, print_number: impl Fn(i32)) {
        self.run(|x| x % 3 != 0 && x % 5 != 0, |x| print_number(x));
    }
}
