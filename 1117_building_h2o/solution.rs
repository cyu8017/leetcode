// LeetCode 1117 - Building H2O
// https://leetcode.com/problems/building-h2o/

use std::sync::{Condvar, Mutex};

struct H2O {
    state: Mutex<(i32, i32)>,
    cv: Condvar,
}

impl H2O {
    pub fn new() -> Self {
        Self {
            state: Mutex::new((0, 0)),
            cv: Condvar::new(),
        }
    }

    pub fn hydrogen(&self, release_hydrogen: impl FnOnce()) {
        let mut s = self.state.lock().unwrap();
        while s.0 == 2 {
            s = self.cv.wait(s).unwrap();
        }
        s.0 += 1;
        release_hydrogen();
        if s.0 == 2 && s.1 == 1 {
            *s = (0, 0);
        }
        self.cv.notify_all();
    }

    pub fn oxygen(&self, release_oxygen: impl FnOnce()) {
        let mut s = self.state.lock().unwrap();
        while s.1 == 1 {
            s = self.cv.wait(s).unwrap();
        }
        s.1 += 1;
        release_oxygen();
        if s.0 == 2 && s.1 == 1 {
            *s = (0, 0);
        }
        self.cv.notify_all();
    }
}
